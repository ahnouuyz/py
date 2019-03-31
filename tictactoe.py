class Tictactoe:
    def __init__(self):
        self.state = [[0 for _ in range(3)] for _ in range(3)]
    
    def __repr__(self):
        sll = [list(map(str, row)) for row in self.state]
        cws = [max(map(len, col)) for col in zip(*sll)]
        hline = '---|---|---'

        txt = '\n'
        for i, row in enumerate(sll):
            line = ' '
            for cw, val in zip(cws, row):
                pad = (cw - len(val)) * ' '
                line += ' XO'[int(val)] + pad + ' | '
            line = line[:-2] + ' '
            txt += line + '\n'
            if i < 2:
                txt += hline + '\n'
        return txt
    
    def __str__(self):
        return self.__repr__()

    def update_state(self, player, r, c):
        if self.state[r][c] == 0:
            self.state[r][c] = player
        else:
            print('Invalid move!')
    
    def run_2_players(self):
        move = 1
        while move < 10:
            player = (2, 1)[move % 2]
            print(f'Round {move}, it is Player {player}\'s turn:')
            pos = input('Enter a position (row,col): ')


            move += 1
        pass


game1 = Tictactoe()
print(game1)
game1.update_state(1, 1, 1)
game1.update_state(2, 0, 1)
print(game1)
# game1.run_2_players()
