import random as rd
from time import sleep

class Reversi:
    dirs = set((r, c) for r in (-1, 0, 1) for c in (-1, 0, 1)) - {(0, 0)}

    def __init__(self):
        self.dct = {(r, c): 0 for r in range(8) for c in range(8)}
        self.spaces = set(self.dct.keys())
        self.update((3, 3), 2)
        self.update((3, 4), 1)
        self.update((4, 3), 1)
        self.update((4, 4), 2)
        self.player = 1
        self.opponent = 2

    def __repr__(self):
        return (f'Current player: {self.player}\n'
                f'Current opponent: {self.opponent}\n'
                f'Current scores: {self.score}')

    @property
    def score(self):
        return {p: sum(n == p for n in self.dct.values()) for p in (1, 2)}

    @property
    def board(self):
        return [[self.dct[(r, c)] for c in range(8)] for r in range(8)]

    @property
    def valid_moves(self):
        poss = self.spaces
        dirs = Reversi.dirs
        encl = self.enclosing
        return set(pos for pos in poss for dir_ in dirs if encl(pos, dir_))

    @property
    def human_valid_moves(self):
        vps = ['abcdefgh'[c] + '12345678'[r] for r, c in self.valid_moves]
        return ' '.join(sorted(vps))

    def dpos(self, pos):
        r, c = pos
        return 'abcdefgh'[c] + '12345678'[r]

    def update(self, pos, player):
        self.dct[pos] = player
        self.spaces.discard(pos)

    def print_board(self):
        ll = self.board
        for r, c in self.valid_moves:
            ll[r][c] = 3

        board2 = [[str(i), '|'] + ['.BW*'[n] for n in row] 
                  for i, row in enumerate(ll, start=1)]
        board2.append('-,|,-,-,-,-,-,-,-,-,'.split(','))
        board2.append(' ,|,a,b,c,d,e,f,g,h,'.split(','))
        render = '\n'.join([' -'[row[0] == '-'].join(row) for row in board2])
        print('\n' + render + '\n')

    def get_line(self, pos, dir_):
        vsum = lambda v1, v2: tuple(map(lambda a, b: a + b, v1, v2))
        dct = {}
        while pos in self.dct.keys():
            dct[pos] = self.dct[pos]
            pos = vsum(pos, dir_)
        return dct

    def enclosing(self, pos, dir_):
        dct = self.get_line(pos, dir_)
        line = tuple(dct.values())
        coords = tuple(dct.keys())
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
        string = ''.join(string.strip().split()).lower()
        if string[0] in 'abcdefgh' and string[1] in '12345678':
            r = '12345678'.index(string[1])
            c = 'abcdefgh'.index(string[0])
            return r, c
        else:
            print('Invalid input, please try again.')

    def run_two_players(self, autoplay=False):
        while self.spaces:
            round_ = 61 - len(self.spaces)

            if len(self.valid_moves) <= 0:
                print(f'Player {self.player} has no moves!')
                break

            print(f'\nRound {round_} (of 60), Player {self.player}\'s turn:')
            print('Current scores:', self.score)
            self.print_board()
            print(f'Valid positions: {self.human_valid_moves}')

            if autoplay:
                pos = rd.sample(self.valid_moves, 1)[0]
            else:
                pos = self.position(input('Enter a position: '))

            if pos:
                print(f'Player {self.player} chose: {self.dpos(pos)}')
                self.next_state(pos)
            print('-' * 60)
            sleep(0.1)

        print('\nGame over!')
        self.print_board()
        print('Current scores:', self.score)
        if max(self.score.values()) > 32:
            print(f'Player {max(self.score, key=self.score.get)} wins!')
        else:
            print('It\'s a draw!')

    def run_single_player(self):
        """ UNDER CONNSTRUCTION!
        """
        while self.spaces:
            round_ = 61 - len(self.spaces)

            if len(self.valid_moves) <= 0:
                print(f'Player {self.player} has no moves!')
                break

            print(f'\nRound {round_} (of 60), Player {self.player}\'s turn:')
            print('Current scores:', self.score)
            self.print_board()
            print(f'Valid positions: {self.human_valid_moves}')

            if autoplay:
                pos = rd.sample(self.valid_moves, 1)[0]
            else:
                pos = self.position(input('Enter a position: '))

            if pos:
                print(f'Player {self.player} chose: {self.dpos(pos)}')
                self.next_state(pos)
            print('-' * 60)
            sleep(0.1)

        print('\nGame over!')
        self.print_board()
        print('Current scores:', self.score)
        if max(self.score.values()) > 32:
            print(f'Player {max(self.score, key=self.score.get)} wins!')
        else:
            print('It\'s a draw!')
        pass

def main():
    game = Reversi()
    game.run_two_players(autoplay=True)

if __name__ == '__main__':
    main()

