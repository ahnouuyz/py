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
#                f'Spaces left: {sorted(self.spaces)}')

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
        board2 = [[str(i), '|'] + ['-BW12'[n] for n in row] 
                  for i, row in enumerate(self.board, start=1)]
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
        self.map_valid_moves(vmoves)
        return vmoves

    def map_valid_moves(self, vmoves):
        for pos in vmoves:
            self.dct[pos] = self.player + 2

    def next_state(self, pos):
        vmoves = self.valid_moves()
        if pos in vmoves:
            for dir_ in Reversi.alldirs:
                self.flip_stones(vmoves, pos, dir_)
            self.update(pos, self.player)

            if self.spaces:
                self.player, self.opponent = self.opponent, self.player
            else:
                self.player, self.opponent = 0, 0
            return self.board, self.player
        else:
            print('Invalid move.')
            return False

    def position(self, string):
        if string[0] in 'abcdefgh' and string[1] in '12345678':
            r = '12345678'.index(string[1])
            c = 'abcdefgh'.index(string[0])
            return r, c
        else:
            print('Invalid input.')

    def run_two_players(self):
        pass

    def run_single_player(self):
        pass

def main():
    pass

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
    test()
    main()

