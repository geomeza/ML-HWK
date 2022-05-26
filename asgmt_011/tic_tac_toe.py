class Game:

    def __init__(self, strategies, board = None):
        self.make_board(board)
        self.current_player = 0
        self.player_move = ['1','2']
        self.strategies = strategies
        self.started = False
        self.winner = None

    def make_board(self, board):
        if board is None:
            self.board = "000000000"
            self.current_player = 0
        else:
            self.board = board
            self.update_current_player()

    def update_current_player(self):
        new_board = list(self.board)
        two_count = new_board.count("2")
        one_count = new_board.count("1")
        if two_count == one_count - 1:
            self.current_player = 1
        elif two_count == one_count:
            self.current_player = 0
        else:
            arr_board = list(self.board)
            print(arr_board[:3])
            print(arr_board[3:6])
            print(arr_board[6:9])
            raise Exception('Invalid Board Input')

    def make_copy(self, board):
        return "".join([str(x) for x in board])

    def make_move(self):
        self.update_current_player()
        strategy = None
        move_token = None
        if self.current_player == 0:
            move = "first"
            move_token = "1"
            strategy = self.strategies[0]
        if self.current_player == 1:
            move = "second"
            move_token = "2"
            strategy = self.strategies[1]
        move_index = strategy.get_move(self.board, move)
        self.board = list(self.board)
        if self.board[move_index] != "0":
            print(move_index, self.board)
            raise Exception("false move")
        self.board[move_index] = move_token
        self.board = "".join(self.board)

    def check_win(self):
        win_indices = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        for index_list in win_indices:
            board_spots = [self.board[index] for index in index_list]
            if board_spots.count("0") == 0:
                winner = board_spots[0]
                if board_spots.count(winner) == 3:
                    if int(winner)-1 != int(self.current_player):
                        print(int(winner)-1, self.current_player)
                        raise Exception("bruh you bubble gum dumb dumb ass")
                    self.winner = self.strategies[int(winner) - 1].name
                    return self.strategies[int(winner) - 1].name
                else:
                    continue
        return None

    def check_tie(self):
        if self.board.count("0") == 0:
            self.winner = "tie"
            return
        else:
            return

    def check_game_over(self):
        self.check_win()
        if self.winner is None:
            self.check_tie()
        return self.winner

    def play_game(self):
        while self.check_game_over() is None:
            self.make_move()
            if not self.started:
                self.started = True
        return self.winner
