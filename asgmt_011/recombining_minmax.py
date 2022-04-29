class MinMaxNode:

    def __init__(self, board, player, parent, tree):
        self.winner = None
        self.tree = tree
        self.parent = parent
        self.children = []
        self.board = "" + board
        self.player = player
        self.get_opponent()
        self.create_children()
        if self.board not in tree.node_dict:
            tree.node_dict[self] = self.children

    def get_opponent(self):
        if self.player == '1':
            self.opponent = '2'
        elif self.player == '2':
            self.opponent = '1'

    def check_game_over(self):
        self.check_win()
        if self.winner is None:
            if self.check_tie():
                self.winner = "tie"
        return

    def check_win(self):
        win_indices = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        for index_list in win_indices:
            board_spots = [self.board[index] for index in index_list]
            if board_spots.count("0") == 0:
                winner = board_spots[0]
                if board_spots.count(winner) == 3:
                    self.winner = winner
                    return self.winner
                else:
                    continue
        return None
    
    def check_tie(self):
        for i in range(9):
            if "0" == self.board[i]:
                return False
        return True

    def create_children(self):
        self.check_game_over()
        if self.winner is not None:
            self.tree.nodes += 1
            return
        for i in range(9):
            if self.board[i] == "0":
                new_board = "" + self.board
                new_board = list(new_board)
                new_board[i] = self.player
                new_board = "".join(new_board)
                tree_nodes = [node for node in self.tree.node_dict.keys()]
                tree_boards = [node.board for node in self.tree.node_dict.keys()]
                if new_board in tree_boards:
                    self.children.append(tree_nodes[tree_boards.index(new_board)])
                    continue
                new_child = MinMaxNode("" + new_board, self.opponent, self, self.tree)
                self.children.append(new_child)

class GameTree:

    def __init__(self):
        self.name = "gametree"
        self.nodes = 0
        self.node_dict = {}
        self.root = MinMaxNode("000000000", "1", None, self)

    def print_nodes(self):
        print(len(self.node_dict))
        return len(self.node_dict)



test_tree = GameTree()
print(test_tree.print_nodes())