# INFO
# black_moves/white_moves consist of all the turns each piece can make.
# Above objects are dictionaries with key being position of the piece (x, y) and the values being a list of moves (x, y)
# When reaching the end of the board, WHITE is promoted to KING using 'K', BLACK is promoted to QUEEN using 'Q'

# NOTE : If the move has 3 values, that means the move is a JUMP and the third value is the position (x, y) of the spot jumped over.
#        This 3rd value is used to remove the piece jumped over
#        A lot of the position indexes might be mixed up, i.e. (x, y) and (y, x) are both used

class Checkers:
    game_board = [['_', 'B', '_', 'B', '_', 'B', '_', 'B'], #0
                  ['B', '_', 'B', '_', 'B', '_', 'B', '_'],#1
                  ['_', 'B', '_', 'B', '_', 'B', '_', 'B'], #2
                  ['_',  '_',  '_',  '_',  '_',  '_',  '_',  '_'], #3
                  ['_',  '_',  '_',  '_',  '_',  '_',  '_',  '_'], #4
                  ['W', '_', 'W', '_', 'W', '_', 'W', '_'], #5
                  ['_', 'W', '_', 'W', '_', 'W', '_', 'W'], #6
                  ['W', '_', 'W', '_', 'W', '_', 'W', '_']] #7

    #this game board is for testing moves
    #game_board = [['_',  '_',  '_',  '_',  '_',  '_',  '_',  '_'], #0
    #              ['_',  '_',  '_',  'W',  '_',  '_',  '_',  '_'],#1
    #              ['_',  '_',  '_',  '_',  '_',  '_',  '_',  '_'], #2
    #              ['_',  '_',  '_',  '_',  '_',  '_',  '_',  '_'], #3
    #              ['_',  '_',  '_',  '_',  'B',  '_',  '_',  '_'], #4
    #              ['_',  '_',  '_',  '_',  '_',  '_',  '_',  '_'], #5
    #              ['_',  '_',  'B',  '_',  '_',  '_',  '_',  '_'], #6
    #              ['_',  'W',  '_',  '_',  '_',  '_',  '_',  '_']] #7

    def __init__(self, player, player2):
        self.turn = 'B'
        # stores all of the current moves of each piece on the board
        self.white_moves = {}
        self.black_moves = {}
        self.running = True
        self.player1 = player
        self.player2 = player2
        self.current_turn = 'W'

    # These apply to all direction methods below
    # pos : (y, x) aka (row, column)
    # returns open position in direction
    # if an opponent piece is in the space ahead, tries to return the spot over that opponent piece, but also returns the position of the piece jumped over as a 3rd parameter
    def down_right(self, pos):
        if pos[0] < 7 and pos[1] < 7:
            if self.game_board[pos[0] + 1][pos[1] + 1] == '_':
                return (pos[1] + 1, pos[0] + 1)
            # checking if piece to jump over is not a teammate
            elif self.game_board[pos[0] + 1][pos[1] + 1] != self.game_board[pos[0]][pos[1]]:
                if pos[0] < 6 and pos[1] < 6:
                    if self.game_board[pos[0] + 2][pos[1] + 2] == '_':
                        return (pos[1] + 2, pos[0] + 2, (pos[1] + 1, pos[0] + 1))
                else: return None
        else: return None

    def down_left(self, pos):
        if pos[0] < 7 and pos[1] > 0:
            if self.game_board[pos[0] + 1][pos[1] - 1] == '_':
                return (pos[1] - 1, pos[0] + 1)
            elif self.game_board[pos[0] + 1][pos[1] - 1] != self.game_board[pos[0]][pos[1]]:
                if pos[0] < 6 and pos[1] > 1:
                    if self.game_board[pos[0] + 2][pos[1] - 2] == '_':
                        return (pos[1] - 2, pos[0] + 2, (pos[1] - 1, pos[0] + 1))
                else: return None
        else: return None

    def up_right(self, pos):
        if pos[0] > 0 and pos[1] < 7:
            if self.game_board[pos[0] - 1][pos[1] + 1] == '_':
                return (pos[1] + 1, pos[0] - 1)
            elif self.game_board[pos[0] - 1][pos[1] + 1] != self.game_board[pos[0]][pos[1]]:
                if pos[0] > 1 and pos[1] < 6:
                    if self.game_board[pos[0] - 2][pos[1] + 2] == '_':
                        return (pos[1] + 2, pos[0] - 2, (pos[1] + 1, pos[0] - 1))
                else: return None
        else: return None

    def up_left(self, pos):
        if pos[0] > 0 and pos[1] > 0:
            if self.game_board[pos[0] - 1][pos[1] - 1] == '_':
                return (pos[1] - 1, pos[0] - 1)
            elif self.game_board[pos[0] - 1][pos[1] - 1] != self.game_board[pos[0]][pos[1]]:
                if pos[0] > 1 and pos[1] > 1:
                    if self.game_board[pos[0] - 2][pos[1] - 2] == '_':
                        return (pos[1] - 2, pos[0] - 2, (pos[1] - 1, pos[0] - 1))
                else: return None
        else: return None

    def print_board(self):
        print('---Game Board---')
        for row in self.game_board:
            for element in row:
                print(element, end=' ')
            print()
        print('----------------')

    # displays the moves of the player with the specified color
    def print_moves(self, color):
        if color == 'W': moves_list = self.white_moves
        elif color == 'B': moves_list = self.black_moves
        print('Available moves : ')
        for x, y in moves_list.keys():
            if moves_list[(x, y)] != []:
                print('Piece : (', y, x, ')', end=' | ')
                print('Moves :', end=' ')
                for move in moves_list[(x, y)]:
                    if len(move) == 3:
                        print(move[:-1], end=' ')
                    else: print(move, end=' ')
                print()

    # returns the valid moves of a piece at position (y, x) aka (row, col)
    # will need to modify this when a king piece is implemented
    def moves_of_piece(self, pos):
        moves = []
        if self.game_board[pos[0]][pos[1]] == 'B':
            DR = self.down_right(pos)
            DL = self.down_left(pos)
            if DR != None: moves.append(DR)
            if DL != None: moves.append(DL)

        elif self.game_board[pos[0]][pos[1]] == 'W':
            UR = self.up_right(pos)
            UL = self.up_left(pos)
            if UR != None: moves.append(UR)
            if UL != None: moves.append(UL)

        elif self.game_board[pos[0]][pos[1]] == 'K' or self.game_board[pos[0]][pos[1]] == 'Q':
            UR = self.up_right(pos)
            UL = self.up_left(pos)
            DR = self.down_right(pos)
            DL = self.down_left(pos)
            if UR != None: moves.append(UR)
            if UL != None: moves.append(UL)
            if DR != None: moves.append(DR)
            if DL != None: moves.append(DL)

        return moves

    # checks if a piece has reached the other side, promoting it to a king or queen
    # white is king, black is queen
    def promote_pieces(self):
        for y, row in enumerate(self.game_board):
            for x, elem in enumerate(row):
                if elem == 'W':
                    if y == 0: 
                        self.game_board[y][x] = 'K'
                elif elem == 'B':
                    if y == 7:
                        self.game_board[y][x] = 'Q'

    # returns a list of the positions of pieces of a certain color that can move
    # color is either 'W' or 'B'
    # resets the 2 move lists each time this is called
    def update_moves(self):
        self.white_moves = {}
        self.black_moves = {}
        for y, row in enumerate(self.game_board):
            for x, element in enumerate(row):
                piece = (y, x)
                if element == 'B' or element == 'Q':
                    self.black_moves[piece] = self.moves_of_piece(piece)
                elif element == 'W' or element == 'K':
                    self.white_moves[piece] = self.moves_of_piece(piece)

    # return true if move is valid
    # this is where pieces are 'captured' when jumped over
    def try_move(self, piece, move, color):
        if color == 'W' : move_list = self.white_moves
        elif color == 'B' : move_list = self.black_moves

        if piece in move_list:
            move_list = move_list[piece]
        else: return False

        for action in move_list:
            if move == action[0:2]: 
                if type(action[-1]) == tuple:
                    self.game_board[action[-1][1]][action[-1][0]] = '_'
                return True
        else: return False

    # executes a move
    # calls try_move() to make sure it is a valid move
    def make_move(self, piece, move, color):
        if self.try_move(piece, move, color):
            self.game_board[move[1]][move[0]] = color
            self.game_board[piece[0]][piece[1]] = '_'
            return True
        else:
            print('Invalid, try again...')
            return False

    # returns False if game is won
    def check_win(self):
        if len(self.white_moves) == 0: return 'B'
        elif len(self.black_moves) == 0: return 'W'
        else: return None

    # checking for chain jumps and promping player to select a jump or skip turn
    # runs its own input-checking loop
    def can_jump_again(self, piece, player):
        if player.color == 'W' : moves = self.white_moves[piece]
        elif player.color == 'B' : moves = self.black_moves[piece]
        
        while True:
            jumps = []

            for action in moves:
                if type(action[-1]) == tuple:
                    jumps.append(action[0:2])

            if len(jumps) != 0:
                self.print_board()

                print(piece[1] ,',', piece[0], ' selected, there is a jump available.')
                print('Jumps : ', jumps)
                user_in = input('Enter a square to jump to, or enter X to end turn : ')

                if user_in == 'X':
                    return False

                self.make_move(piece, (int(user_in[0]), int(user_in[-1])), player.color)

                self.update_moves()
            else: return False

    # return true if move was a jump
    def is_move_jump(self, piece, move, color):
        if color == 'W' : move_list = self.white_moves
        elif color == 'B' : move_list = self.black_moves

        if piece in move_list:
            move_list = move_list[piece]
        else: return False

        for action in move_list:
            if move == action[0:2]: 
                if type(action[-1]) == tuple:
                    return True
                return False
        else: return False

    # call this to start the game loop
    def run(self):
        # self.player1 starts first
        player = self.player1
        while self.running:
            print('Current Turn: ', player.color)
            self.print_board()
            self.update_moves()
            self.print_moves(player.color)
            
            making_turn = True

            # Executing a turn
            while making_turn == True:
                valid_move = False
                while not valid_move:
                    pos = player.get_piece()
                    pos = (pos[1], pos[0])
                    print(pos[1] ,',', pos[0], ' selected.')
                    to_pos = player.get_move()
                    
                    valid_move = self.make_move(pos, to_pos, player.color)
                    
                    # chain jumps
                    if valid_move:
                        # if previous move was a jump, allow chain jumps
                        if self.is_move_jump(pos, to_pos, player.color): chain_jumping = True
                        else: chain_jumping = False

                        while chain_jumping:
                            self.update_moves()
                            # pass the position of to_pos since make_move() is called before this
                            chain_jumping = self.can_jump_again((to_pos[1], to_pos[0]), player)
                
                print('Move ', pos, 'to', to_pos)

                # Ending turn
                # Human Players
                input('Press ENTER to end turn.')
                if type(self.player2) == CheckersPlayer: 
                    if player == self.player1: player = self.player2
                    else: player = self.player1
                    making_turn = False

                # AI Player
                elif type(self.player2) == CheckersAI:
                    AI_move = self.player2.get_move()
                    self.make_move(AI_move)
                    making_turn = False

                # checking if pieces reach the other end of the board
                self.promote_pieces()

                # checking win conditions after every turn end
                winner = self.check_win()
                if winner != None:
                    print(winner, ' wins!')
                    self.running = False

                print()


# human player that requires inputs to be made to make moves
# prompts the human player to enter positions of the game board in the for of (x, y) aka (col, row)
class CheckersPlayer:
    def __init__(self, player_name, color):
        self.name = player_name
        self.color = color

    # prompt player to select piece
    def get_piece(self):
        while True:
            pos = input('Enter the position, x,y of a piece to move : ')
            try:
                pos = pos.split(",")
                output = (int(pos[0]), int(pos[1]))
                return output
            except:
                print('Invalid input, try again.')

    # prompt player to select square to move to, after selecting a piece
    def get_move(self):
        while True:
            pos = input('Enter the position, x,y of a square to move to : ')
            try:
                pos = pos.split(",")
                output = (int(pos[0]), int(pos[1]))
                return output
            except:
                print('Invalid input, try again.')

# AI player
class CheckersAI(CheckersPlayer):
    def __init__(self, name, color, checkers):
        super().__init__(name, color)
        self.checkers = checkers
        self.game_board = self.checkers.game_board
        self.white_moves = checkers.white_moves
        self.black_moves = checkers.black_moves

        self.action = None

    def get_move(self):
        None


def main():
    player1 = CheckersPlayer('Human', 'W')
    player2 = CheckersPlayer('Human2', 'B')
    checkers = Checkers(player1, player2)
    #checkers.player2 = CheckersAI('Computer', 'B', checkers)
    
    checkers.run()
    
if __name__ == '__main__':
    main()
