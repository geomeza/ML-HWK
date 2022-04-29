import random

class Strategy:

    def __init__(self, name, first_move = None, second_move = None):
        self.name = name
        self.winner = None
        self.first_move_list = {}
        self.second_move_list = {}
        if first_move is None:
            self.make_move_list(False)
        else:
            self.first_move_list = first_move
        if second_move is None:
            self.make_move_list(True)
        else:
            self.second_move_list = second_move

    def get_move(self, board, move):
        if move == "first":
            return self.first_move_list[board]
        if move == "second":
            return self.second_move_list[board]

    def make_move_list(self, second_move, board = None):
        if board is None:
            board = "000000000"
        possible_moves = [index for index, element in enumerate(board) if element == "0"]
        if len(possible_moves) == 0:
            return
        if self.check_win(board) is not None:
            return
        if not second_move:
            if board.count("1") == board.count("2"):
                move_index = random.choice(possible_moves)
                self.first_move_list[board] = move_index
                new_board = [] + list(board)
                new_board[move_index] = "1"
                self.make_move_list(second_move, "".join(new_board))
            elif board.count("1")-1 == board.count("2"):
                for move in possible_moves:
                    new_board = [] + list(board)
                    new_board[move] = "2"
                    self.make_move_list(second_move, "".join(new_board))
            else:
                raise Exception("invalid board")
        if second_move:
            if board.count("1") == board.count("2"):
                for move in possible_moves:
                    new_board = [] + list(board)
                    new_board[move] = "1"
                    self.make_move_list(second_move, "".join(new_board))
            elif board.count("1")-1 == board.count("2"):
                move_index = random.choice(possible_moves)
                self.second_move_list[board] = move_index
                new_board = [] + list(board)
                new_board[move_index] = "2"
                self.make_move_list(second_move, "".join(new_board))
            else:
                raise Exception("invalid board")

    def check_win(self, board):
        win_indices = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        for index_list in win_indices:
            board_spots = [board[index] for index in index_list]
            if board_spots.count("0") == 0:
                winner = board_spots[0]
                if board_spots.count(winner) == 3:
                    return str(winner)
                else:
                    continue
        return None
