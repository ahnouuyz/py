import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def assign(array_2d, centroids):
    """ Assign each point to the nearest centroid.
        Return a dictionary (of dictionaries) of centroids:
            Key: Centroid
            Value: Dictionary of coordinates
                Key: Coordinate
                Value: Value at coordinate
    """
    all_coords = np.array(tuple(np.ndindex(array_2d.shape)))
    diff = all_coords[:, None] - centroids[None, :]
    sq_dists = np.einsum('ijk,ijk->ij', diff, diff) # i -> coordinates, j -> centroids, k -> dimensions (y, x)
    
    cluster_dct = dict((tuple(centroid), {}) for centroid in centroids)
    for centroid, coord_value in zip(np.argmin(sq_dists, axis=1), np.ndenumerate(array_2d)):
        cluster_dct[tuple(centroids[centroid])][coord_value[0]] = coord_value[1]
    
    return cluster_dct

def update_centroids(cluster_dct):
    """ Calculate new positions of centroids based on assigned clusters.
        Still using the weighted-average method.
        Weighted-average method does not necessarily lead to highest score.
        Will be good to have another method.
    """
    new_centroids = []
    for cluster in cluster_dct.values():
        coords, values = map(np.array, tuple(zip(*cluster.items())))
        scaled_values = values / values.sum()
        mean_coord = np.einsum('ij,i->j', coords, scaled_values).round()
        new_centroids.append(tuple(mean_coord))
    return np.array(new_centroids)

def global_score(cluster_dct):
    """ Calculate the score for a given configuration.
    """
    global_score = 0
    for centroid, cluster in cluster_dct.items():
        centroid_score = cluster[centroid] # Store centroid's score first
        cluster_pts, values = tuple(zip(*filter(lambda t: t[0] != centroid, cluster.items()))) # Remove centroid
        centroid, cluster_pts, values = map(np.array, (centroid, cluster_pts, values))
        diff = centroid - cluster_pts
        distances = np.sqrt(np.einsum('ij,ij->i', diff, diff))
        distances += 1 # <-- For compatibility
        scores = values / distances
        global_score += scores.sum() + centroid_score - 2000000 # 1000
    return global_score
    
def k_means(array_2d, k=2, max_iter=10):
    initial_coords = random.sample(set(np.ndindex(array_2d.shape)), k=k)
    centroids = np.array(initial_coords)
    cluster_dct_frames = []
    scores_frames = []
    
    for iteration in range(max_iter):
        cluster_dct = assign(array_2d, centroids)
        current_score = global_score(cluster_dct)
        new_centroids = update_centroids(cluster_dct)
        distance_moved = np.linalg.norm(new_centroids - centroids, axis=1).sum()
        centroids = new_centroids
        cluster_dct_frames.append(cluster_dct)
        scores_frames.append(current_score)
        
        if current_score > scores_frames[iteration - 1]:
            sign = '(+)'
        elif current_score < scores_frames[iteration - 1]:
            sign = '(-)'
        else:
            sign = '(=)'
        
        print(f'k = {k} - Iteration {iteration + 1} - '
              f'Score = {current_score:.0f} {sign} - '
              f'Total displacement = {distance_moved:.5f}')
        
        if distance_moved < (0.001 * k):
            break
    
    print(f'Total number of iterations: {iteration + 1}')
    return tuple(cluster_dct_frames)

def get_final_centroids(cluster_dct_frames):
    return tuple(cluster_dct_frames[-1].keys())

def animate_k_means(cluster_dct_frames):
    # Unpack coordinates for each frame/iteration.
    centroids_frames = tuple(cluster_dct.keys() for cluster_dct in cluster_dct_frames)
    clusters_frames = []
    for cluster_dct in cluster_dct_frames:
        clusters_frame = tuple(cluster_points for cluster_points in cluster_dct.values())
        clusters_frames.append(clusters_frame)
    
    # Generate the figure.
    k = len(cluster_dct_frames[0])
    palette = sns.color_palette('tab10', n_colors=k)
    
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(array_2d, cmap="BuGn", square=True, ax=ax, alpha=1, cbar=False)
    
    centroid_artist, = ax.plot([], [], linestyle='None', markersize=100, marker='o', c='cyan', alpha=0.5)
    cluster_artists = []
    for i2 in range(k):
        artist, = ax.plot([], [], linestyle='None', marker='x', c=palette[i2], alpha=0.6)
        cluster_artists.append(artist)
    
    def animate(frame):
        centroids_disp = [tuple(map(round, centroid)) for centroid in centroids_frames[frame]]
        ax.set_title(f'Iteration {frame + 1}\n{centroids_disp}')
        for i2 in range(k):
            yxs = tuple(zip(*clusters_frames[frame][i2]))
            cluster_artists[i2].set_data(yxs[1], yxs[0])
        cyxs = tuple(zip(*centroids_frames[frame]))
        centroid_artist.set_data(cyxs[1], cyxs[0])
    
    ani = FuncAnimation(fig, animate, frames=len(cluster_dct_frames), interval=500)
    plt.close('all')
    
    return ani

