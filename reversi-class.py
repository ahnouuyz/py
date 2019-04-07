import random as rd

class Reversi:
    alldirs = set((r, c) for r in (-1, 0, 1) for c in (-1, 0, 1)) - {(0, 0)}

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

    def update(self, pos, player):
        self.dct[pos] = player
        self.spaces.discard(pos)

    def print_board(self):
        ll = self.board
        vmoves = self.valid_moves()
        for r, c in vmoves:
            ll[r][c] = 3

        board2 = [[str(i), '|'] + ['.BW*'[n] for n in row] 
                  for i, row in enumerate(ll, start=1)]
        board2.append('-,|,-,-,-,-,-,-,-,-,'.split(','))
        board2.append(' ,|,a,b,c,d,e,f,g,h,'.split(','))
        render = '\n'.join([' -'[row[0] == '-'].join(row) for row in board2])
        print('\n' + render + '\n')

    def enclosing(self, pos, dir_):
        vsum = lambda v1, v2: tuple(map(lambda a, b: a + b, v1, v2))

        line = []
        while pos in self.dct.keys():
            line.append(self.dct[pos])
            pos = vsum(pos, dir_)

        if self.player in line[2:]:
            k = line[2:].index(self.player) + 2
            if all(val == self.opponent for val in line[1:k]):
                return True
            else:
                return False
        else:
            return False

    def flip_stones(self, vmoves, pos, dir_):
        vsum = lambda v1, v2: tuple(map(lambda a, b: a + b, v1, v2))

        line = []
        coords = []
        while pos in self.dct.keys():
            line.append(self.dct[pos])
            coords.append(pos)
            pos = vsum(pos, dir_)

        if self.player in line[2:]:
            k = line[2:].index(self.player) + 2
            if all(val == self.opponent for val in line[1:k]):
                for pos in coords[1:k]:
                    self.update(pos, self.player)

    def valid_moves(self):
        vmoves = [pos 
                  for pos in self.spaces 
                  for dir_ in Reversi.alldirs 
                  if self.enclosing(pos, dir_)]
        return vmoves

    def next_state(self, pos):
        vmoves = self.valid_moves()
        if pos in vmoves:
            for dir_ in Reversi.alldirs:
                self.flip_stones(vmoves, pos, dir_)
            self.update(pos, self.player)
            self.player, self.opponent = self.opponent, self.player
        else:
            print('Invalid move, please try again.')

    def position(self, string):
        if string[0] in 'abcdefgh' and string[1] in '12345678':
            r = '12345678'.index(string[1])
            c = 'abcdefgh'.index(string[0])
            return r, c
        else:
            print('Invalid input, please try again.')

    def dpos(self, pos):
        r, c = pos
        return 'abcdefgh'[c] + '12345678'[r]

    def run_two_players(self, autoplay=False):
        while self.spaces:
            round_ = 61 - len(self.spaces)
            self.print_board()
            vmoves = self.valid_moves()

            if len(vmoves) <= 0:
                print(f'Player {self.player} has no moves!')
                break

            print(f'It\'s round {round_} (of 60):')
            print(f'It\'s Player {self.player}\'s turn.')

            if autoplay:
                pos = rd.sample(vmoves, 1)[0]
            else:
                pos = self.position(input('Enter a position: '))

            if pos:
                print(f'Player {self.player} chose: {self.dpos(pos)}')
                self.next_state(pos)

        self.print_board()
        print('Game over!')
        print(self.__repr__())
        print(f'Player {max(self.score, key=self.score.get)} wins!')

    def run_single_player(self):
        pass

def main():
    game = Reversi()
    game.run_two_players(autoplay=True)

def test():
    game = Reversi()
    game.print_board()
    print(game)
    game.next_state((4, 5))
    game.print_board()
    print(game)
    game.next_state((5, 5))
    game.print_board()
    print(game)

if __name__ == '__main__':
#    test()
    main()

