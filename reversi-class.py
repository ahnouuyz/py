import random as rd
from time import sleep

class Reversi:
    dirs = set((r, c) for r in (-1, 0, 1) for c in (-1, 0, 1)) - {(0, 0)}

    def __init__(self):
        rs = '12345678'
        cs = 'abcdefgh'
        self.dct = {(r, c): 0 for r in range(8) for c in range(8)}
        self.hpos = {(r, c): cs[c] + rs[r] for r, c in self.dct}
        self.spaces = set(self.dct)
        self.round = 1
        self.player = 1
        self.opponent = 2
        self.score = {1: 0, 2: 0}
        self.update((3, 3), 2)
        self.update((3, 4), 1)
        self.update((4, 3), 1)
        self.update((4, 4), 2)

    @property
    def valid_moves(self):
        poss = self.spaces
        dirs = Reversi.dirs
        encl = self.enclosing
        return set(pos for pos in poss for dir_ in dirs if encl(pos, dir_))

    def update(self, pos, player):
        if self.dct[pos] == self.opponent:
            self.score[self.opponent] -= 1
        self.dct[pos] = player
        self.score[player] += 1
        self.spaces.discard(pos)

    def print_board(self):
        ll = [[self.dct[(r, c)] for c in range(8)] for r in range(8)]
        for r, c in self.valid_moves:
            ll[r][c] = 3

        sll = [[str(i), '|'] + ['.BW*'[n] for n in row] 
                  for i, row in enumerate(ll, start=1)]
        sll.append('-,|,-,-,-,-,-,-,-,-,'.split(','))
        sll.append(' ,|,a,b,c,d,e,f,g,h,'.split(','))
        render = '\n'.join([' -'[row[0] == '-'].join(row) for row in sll])
        print('\n' + render + '\n')

    def enclosing(self, pos, dir_):
        dct = {}
        while pos in self.dct:
            dct[pos] = self.dct[pos]
            pos = tuple(map(int.__add__, pos, dir_))

        if len(dct) < 3:
            return False

        coords, line = tuple(zip(*dct.items()))
        if line[1] == self.player:
            return False

        if self.player in line[2:]:
            k = line[2:].index(self.player) + 2
            if all(val == self.opponent for val in line[1:k]):
                return coords[1:k]
            else:
                return False
        else:
            return False

    def next_state(self, pos):
        if pos in self.valid_moves:
            for dir_ in Reversi.dirs:
                to_flip = self.enclosing(pos, dir_)
                if to_flip:
                    for coord in to_flip:
                        self.update(coord, self.player)
            self.update(pos, self.player)
            self.player, self.opponent = self.opponent, self.player
        else:
            print('Invalid move, please try again.')

    def position(self, string):
        string = ''.join(string.split()).lower()
        if string in self.hpos.values():
            r = '12345678'.index(string[1])
            c = 'abcdefgh'.index(string[0])
            return r, c
        else:
            print('Invalid input, please try again.')

    def run_two_players(self, autoplay=False):
        """ 
            Add an option to quit.
        """
        while self.spaces:
            if len(self.valid_moves) <= 0:
                print(f'Player {self.player} has no moves!')
                break

            print(f'\nRound {self.round} (of 60), Player {self.player}\'s turn:')
            print('Current scores:', self.score)
            self.print_board()
            hvm = ' '.join(self.hpos[p] for p in self.valid_moves)
            print(f'Valid positions: {hvm}')

            if autoplay:
                pos = rd.sample(self.valid_moves, 1)[0]
            else:
                pos = self.position(input('Enter a position: '))

            if pos:
                print(f'Player {self.player} chose: {self.hpos[pos]}')
                self.next_state(pos)
            self.round += 1
            print('-' * 60)
            sleep(0.1)

        print('\nGame over!')
        self.print_board()
        print('Current scores:', self.score)
        if self.score[1] == self.score[2]:
            print('It\'s s draw!')
            return 0
        else:
            winner = max(self.score, key=self.score.get)
            print(f'Player {winner} wins!')
            return winner

    def best_move(self):
        """ Loop through all valid moves, 
            calculate change in score for all choices, 
            return the choice that gives the highest score.
        """
        scores = {}
        for pos in self.valid_moves:
            score = 0
            for dir_ in Reversi.dirs:
                to_flip = self.enclosing(pos, dir_)
                if to_flip:
                    score += len(to_flip)
            scores[pos] = score
        print(scores)
        best_score = max(scores.values())
        best_move = max(scores, key=scores.get)
        print('Best move:', best_move, ' | Best score:', best_score)
        return best_move

    def run_single_player(self, autoplay=False):
        """ 
            UNDER CONNSTRUCTION
            Add a option to quit.
        """
        while self.spaces:
            if len(self.valid_moves) <= 0:
                print(f'Player {self.player} has no moves!')
                break

            print(f'\nRound {self.round} (of 60), Player {self.player}\'s turn:')
            print('Current scores:', self.score)
            self.print_board()
            hvm = ' '.join(self.hpos[p] for p in self.valid_moves)
            print(f'Valid positions: {hvm}')

            if self.player == 2:
                pos = self.best_move()
            else:
                if autoplay:
                    pos = rd.sample(self.valid_moves, 1)[0]
                else:
                    pos = self.position(input('Enter a position: '))

            if pos:
                print(f'Player {self.player} chose: {self.hpos[pos]}')
                self.next_state(pos)
            self.round += 1
            print('-' * 60)

        print('\nGame over!')
        self.print_board()
        print('Current scores:', self.score)
        if self.score[1] == self.score[2]:
            print('It\'s s draw!')
            return 0
        else:
            winner = max(self.score, key=self.score.get)
            print(f'Player {winner} wins!')
            return winner

def player_2_win_rate(nrounds=10):
    wins = 0
    for i in range(nrounds):
        if Reversi().run_single_player(autoplay=True) == 2:
            wins += 1
    print(f'Player 2 win rate: {wins / nrounds}')

def main():
    game = Reversi()
#    game.run_two_players(autoplay=True)
    game.run_single_player(autoplay=True)
#    player_2_win_rate(nrounds=20)

if __name__ == '__main__':
    main()

