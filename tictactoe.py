class Tictactoe:
    def __init__(self):
        self.state = [[0 for _ in range(3)] for _ in range(3)]
        self.positions = set((r, c) for r in range(3) for c in range(3))
    
    def __repr__(self):
        sll = [list(map(str, row)) for row in self.state]
        cws = [max(map(len, col)) for col in zip(*sll)]
        hlst = [(cw + 2) * '-' + '|' for cw in cws]
        hline = '  ' + ''.join(hlst)[:-1]

        txt = '   1   2   3 \n'
        for i, row in enumerate(sll):
            line = f'{i + 1}  '
            for cw, val in zip(cws, row):
                pad = (cw - len(val)) * ' '
                line += ' XO'[int(val)] + pad + ' | '
            line = line[:-2] + ' '
            txt += line + '\n' + hline + '\n' if i < 2 else line + '\n'
        return txt
    
    def __str__(self):
        return self.__repr__()
    
    def show_positions(self):
        add_ones = lambda a: tuple(map(lambda b: b + 1, a))
        return sorted(list(map(add_ones, tuple(self.positions))))

    def input_postition(self):
        print(self.__repr__())
        print(f'Available positions: {self.show_positions()}')
        raw_input = input('Input a row,col ("q" to quit): ')
        
        if len(raw_input) > 0:
            if raw_input.lower().startswith('q'):
                return 'quit'
            
            delimiters = ',;:-_/.*~| '
            mask = [delimiter in raw_input for delimiter in delimiters]
            if any(mask):
                delimiter = delimiters[mask.index(True)]
                lst = raw_input.strip().split(delimiter)[:2]
                if all(x.isnumeric() for x in lst):
                    r, c = tuple(map(int, lst))
                    r, c = r - 1, c - 1
                    if (r, c) in self.positions:
                        return r, c

    def update_state(self, player, pos):
        r, c = pos
        self.state[r][c] = player
        self.positions -= {pos}
    
    def check_win(self):
        rows = self.state
        cols = list(zip(*rows))
        diag1 = [[rows[i][i] for i in range(3)]]
        diag2 = [[rows[2 - i][i] for i in range(3)]]
        trips = rows + cols + diag1 + diag2
        for trip in trips:
            if 0 in trip:
                continue
            elif all(val == 1 for val in trip):
                return 1
            elif all(val == 2 for val in trip):
                return 2

    def run_2_players(self):
        while len(self.positions) > 0:
            move = 10 - len(self.positions)
            player = (2, 1)[move % 2]
            print(f'\nRound {move}: It is Player {player}\'s turn:')

            pos = self.input_postition()
            if pos == 'quit':
                break
            elif pos:
                self.update_state(player, pos)
                winner = self.check_win()
                if winner:
                    break
            else:
                print('\nInvalid move! Please try again...')
        
        print(self.__repr__())
        if pos == 'quit':
            print('Game terminated.')
        elif winner:
            print(f'Game over! Player {winner} won!')
        else:
            print('Game over! It\'s a draw!')
    
    def run_1_player(self):
        pass

game = Tictactoe()
game.run_2_players()
