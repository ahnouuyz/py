class Tictactoe:
    def __init__(self):
        initial_state = [[0 for _ in range(3)] for _ in range(3)]
        self.state = initial_state
    
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
    
    def get_postition(self):
        print(self.__repr__())
        raw_input = input('Please choose a position (row,col): ')
        
        if len(raw_input) > 0:
            if raw_input.lower().startswith('q'):
                return 'quit'
            
            delimiters = ',.;:| '
            for delimiter in delimiters:
                if delimiter in raw_input:
                    break
            else:
                return False
            
            r, c = tuple(map(int, raw_input.strip().split(delimiter)))
            r, c = r - 1, c - 1
            if r in (0, 1, 2) and c in (0, 1, 2) and self.state[r][c] == 0:
                return r, c

    def update_state(self, player, pos):
        r, c = pos
        self.state[r][c] = player
    
    def run_2_players(self):
        move = 1
        while move < 10:
            player = (2, 1)[move % 2]
            print(f'Round {move}: It is Player {player}\'s turn:')

            pos = self.get_postition()
            if pos == 'quit':
                break
            elif pos:
                self.update_state(player, pos)
                move += 1
            else:
                print('Invalid move! Please try again...')
        
        print(self.__repr__())
        print('GAME OVER!')

game1 = Tictactoe()
game1.run_2_players()
