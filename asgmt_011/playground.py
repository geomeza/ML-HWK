from strategy import Strategy
from recombining_minmax import MinMaxStrategy
from tic_tac_toe import Game

import numpy as np
import random
import matplotlib.pyplot as plt

def assess_scores(winner, strategies, score_dict):
    if winner == strategies[0].name:
        score_dict[winner] += 1
        score_dict[strategies[1].name] -= 1
    if winner == strategies[1].name:
        score_dict[winner] += 1
        score_dict[strategies[0].name] -= 1
    return score_dict

def run_games(strategies):
    score_dict = {}
    for strat in strategies:
        score_dict[strat] = 0
    for first_key, first_strat in strategies.items():
        for second_key, second_strat in strategies.items():
            if first_key == second_key:
                continue
            else:
                print("running game")
                game = Game([first_strat, second_strat]).play_game()
                if game != "tie":
                    assess_scores(game, [first_strat, second_strat], score_dict)
    return score_dict


print("generating strategies")
rando = Strategy("rando one")
minmax = MinMaxStrategy("min max two")

strats_dict = {"rando one": rando, "min max two": minmax}
print("starting games")
score_dict = run_games(strats_dict)
print(score_dict)

# # def get_top_five(strategies, score_dict):
# #     numpy_scores_arr = np.array(list(score_dict.values()))
# #     top_five_strats_indexes = list(np.argpartition(numpy_scores_arr, -5)[-5:])
    
# #     random_strats_keys = list(strategies.keys())
# #     top_five_strats = [random_strats_keys[index] for index in top_five_strats_indexes]
# #     return top_five_strats

# def get_top_strats(strategies, method = "hard cutoff", mode = "round robin"):
#     score_dict = {}
#     if method == "hard cutoff" or method == "stochastic" and mode == "round robin":
#         score_dict = run_games(strategies)
#     breeding_pop = []
#     strategy_num = len(strategies.keys())
#     breeding_amount = strategy_num/4
#     if method == "stochastic" or method == "tournament":
#         for i in range(breeding_amount):
#             random_sample = random.sample(list(score_dict.keys()), strategy_num/8)
#             if method == "tournament":
#                 score_dict = run_games(random_sample)
#             max_scores = [score_dict[strat] for strat in random_sample]
#             index_of_max = max_scores.index(max(max_scores)) 
#             breeding_pop.append(random_sample[index_of_max])
#             if method != "tournament":
#                 for strat in random_sample:
#                     score_dict.pop(strat)
#         return breeding_pop
#     if method == "hard cutoff":
#         numpy_scores_arr = np.array(list(score_dict.values()))
#         top_strats_indexes = list(np.argpartition(numpy_scores_arr, -1 * breeding_amount)[-1* breeding_amount:])
#         strats_keys = list(strategies.keys())
#         top_strats = [strats_keys[index] for index in top_strats_indexes]
#         return top_strats

# def check_win(board):
#         win_indices = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
#         for index_list in win_indices:
#             board_spots = [board[index] for index in index_list]
#             if board_spots.count("0") == 0:
#                 winner = board_spots[0]
#                 if board_spots.count(winner) == 3:
#                     return str(winner)
#                 else:
#                     continue
#         return None

# def return_move_index(board, first_move_list, second_move_list):
    
#     if board in first_move_list and board in second_move_list:
#         return random.choice([first_move_list[board], second_move_list[board]])
#     elif board in first_move_list:
#         return first_move_list[board]
#     elif board in second_move_list:
#         return second_move_list[board]
#     else:
#         raise Exception("should not be happening")

# def recursive_intersection(first_move_list, second_move_list, second_move, new_list = {}, board = None):
#     if board is None:
#         board = "000000000"
#     possible_moves = [index for index, element in enumerate(board) if element == "0"]
#     if len(possible_moves) == 0:
#         return new_list
#     if check_win(board) is not None:
#         return new_list
#     if not second_move:
#         if board.count("1") == board.count("2"):
#             move_index = return_move_index(board, first_move_list, second_move_list)
#             new_list[board] = move_index
#             new_board = [] + list(board)
#             new_board[move_index] = "1"
#             new_list = recursive_intersection(first_move_list, second_move_list, second_move, new_list, "".join(new_board))
#             return new_list
#         elif board.count("1")-1 == board.count("2"):
#             for move in possible_moves:
#                 new_board = [] + list(board)
#                 new_board[move] = "2"
#                 new_list = recursive_intersection(first_move_list, second_move_list, second_move, new_list, "".join(new_board))
#             return new_list
#         else:
#             raise Exception("invalid board")
#     if second_move:
#         if board.count("1") == board.count("2"):
#             for move in possible_moves:
#                 new_board = [] + list(board)
#                 new_board[move] = "1"
#                 new_list = recursive_intersection(first_move_list, second_move_list, second_move, new_list, "".join(new_board))
#             return new_list
#         elif board.count("1")-1 == board.count("2"):
#             move_index = return_move_index(board, first_move_list, second_move_list)
#             new_list[board] = move_index
#             new_board = [] + list(board)
#             new_board[move_index] = "2"
#             new_list = recursive_intersection(first_move_list, second_move_list, second_move, new_list, "".join(new_board))
#             return new_list
#         else:
#             raise Exception("invalid board")

# def make_strategies(strat_one, strat_two, name):
#     first_move_list = recursive_intersection(strat_one.first_move_list, strat_two.first_move_list, False, {}, None)
#     second_move_list = recursive_intersection(strat_one.second_move_list, strat_two.second_move_list, True, {}, None)
#     return Strategy(name, first_move_list, second_move_list)

# def breeding_algorithm(top_strats, generation, next_gen_num):
#     new_strategies = {}
#     pop_size = len(top_strats) * 3
#     old_gen_num = top_strats[0][4]
#     for num in pop_size:
#         strat_one = generation[random.choice(top_strats)]
#         strat_two = generation[random.choice(top_strats)]
#         strat_one_num = strat_one.name.replace("gen_" + old_gen_num + "_", "")
#         strat_two_num = strat_two.name.replace("gen_"+ old_gen_num + "_", "")
#         new_name = "gen_"+ str(next_gen_num)+ "_" + str(i) + "_" + str(j)
#         new_strat = make_strategies(strat_one, strat_two, new_name)
#         new_strategies[new_name] = new_strat
#     for strat in top_strats:
#         new_strategies[strat] = generation[strat]
#     return new_strategies

#     # # for i in range(len(top_strats)):
#     # #     for j in range(len(top_strats)):
#     # #         if i == j:
#     # #             continue
#     # #         old_gen_num = top_strats[0][4]
#     # #         strat_one = generation[top_strats[i]]
#     # #         strat_one_num = strat_one.name.replace("gen_"+ old_gen_num + "_", "")
#     # #         strat_two = generation[top_strats[j]]
#     # #         strat_two_num = strat_two.name.replace("gen_"+ old_gen_num + "_", "")
            
#     # #         new_name = "gen_"+ str(next_gen_num)+ "_" + str(i) + "_" + str(j)
#     # #         new_strat = make_strategies(strat_one, strat_two, new_name)
#     # #         new_strategies[new_name] = new_strat
#     # for strat in top_strats:
#     #     new_strategies[strat] = generation[strat]
#     # return new_strategies


# def versus_gens(strategies, generation, enem_gen):
#     scores = [0 for _ in range(len(strategies))]
#     for strat in strategies:
#         strat_obj = generation[strat]
#         for first_gen_strat in enem_gen.values():
#             game = Game([strat_obj, first_gen_strat]).play_game()
#             if game == strat_obj.name:
#                 scores[strategies.index(strat)] += 1
#             elif game == "tie":
#                 continue
#             else:
#                 scores[strategies.index(strat)] -= 1
#             game = Game([first_gen_strat, strat_obj]).play_game()
#             if game == strat_obj.name:
#                 scores[strategies.index(strat)] += 1
#             elif game == "tie":
#                 continue
#             else:
#                 scores[strategies.index(strat)] -= 1
#     return sum(scores)/5

# def can_win(board, winner):
#     win_indices = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
#     for index_list in win_indices:
#         board_spots = [board[index] for index in index_list]
#         if board_spots.count("0") != 1:
#             continue
#         board_spots.remove("0")
#         if board_spots.count(winner) == 2:
#             return index_list
#         else:
#             continue
#     return None

# def make_move(board, move_spot, player):
#     board = [] + list(board)
#     board[move_spot] = player
#     return "".join(board)

# def count_all_possible_wins(strategy, player = "1"):
#     possible_wins = 0
#     realized_wins = 0
#     move_list = strategy.first_move_list
#     if player == "2":
#         move_list = strategy.second_move_list
#     for board in move_list.keys():
#         possible_win = can_win(board, player)
#         if possible_win is not None:
#             possible_wins += 1
#             player_move = move_list[board]
#             new_board = make_move(board, player_move, player)
#             winner = strategy.check_win(new_board)
#             if winner is not None:
#                 realized_wins += 1
#     return realized_wins, possible_wins

# def return_total_wins_realized(strategies, generation):
#     total_realized = 0
#     total_possible = 0
#     strat_objs = [generation[strat] for strat in strategies]
#     for strat in strat_objs:
#         first_realized, first_possible = count_all_possible_wins(strat)
#         second_realized, second_possible = count_all_possible_wins(strat, "2")
#         total_realized += (first_realized + second_realized)
#         total_possible += (first_possible + second_possible)
#     return total_realized/total_possible

# def win_blocked(board, index_list, enemy, player):
#     board_spots = [board[index] for index in index_list]
#     if check_win(board) == player:
#         return True
#     if board_spots.count(player) == 1 and board_spots.count("0") == 0 and board_spots.count(enemy) == 2:
#         return True
#     return False

# def count_all_wins_blocked(strategy, player = "1"):
#     possible_wins = 0
#     blocked_wins = 0
#     move_list = strategy.first_move_list
#     enemy_player = "2"
#     if player == "2":
#         move_list = strategy.second_move_list
#         enemy_player = "1"
#     for board in move_list.keys():
#         possible_win = can_win(board, enemy_player)
#         if possible_win is not None:
#             possible_wins += 1
#             player_move = move_list[board]
#             new_board = make_move(board, player_move, player)
#             blocked = win_blocked(new_board, possible_win, enemy_player, player)
#             if blocked:
#                 blocked_wins += 1
#     return blocked_wins, possible_wins

# def return_total_wins_blocked(strategies, generation):
#     total_possible = 0
#     total_blocked = 0
#     strats = [generation[strategy] for strategy in strategies]
#     for strat in strats:
#         first_blocked, first_possible = count_all_wins_blocked(strat)
#         second_blocked, second_possible = count_all_wins_blocked(strat, "2")
#         total_possible += (first_possible + second_possible)
#         total_blocked += (first_blocked + second_blocked)
#     return total_blocked/total_possible

# print("generating first generation")

# gen_one_strats_dict = {}
# for i in range(16):
#     dict_key = "gen_1_" + str(i)
#     gen_one_strats_dict[dict_key] = Strategy(dict_key)

# print("first games")

# top_strats = get_top_strats(gen_one_strats_dict)

# next_gen = breeding_algorithm(top_strats, gen_one_strats_dict, 2)
# top_five_strats = get_top_strats(next_gen)

# realized_wins_percent = []

# blocked_wins_percent = []

# versus_gen_one_scores = []

# versus_previous_gen_scores = []
# generations = []

# print("genetic process occuring")

# modes = ["hard cutoff", "stochastic", "tournament"]

# for i in range(20):
#     next_gen = breeding_algorithm
# for i in range(20):
#     print("generation ", i+2)
#     versus_gen_one_scores.append(versus_gens(top_five_strats, next_gen, gen_one_strats_dict))
#     old_gen = next_gen.copy()
#     realized_wins_percent.append(return_total_wins_realized(top_five_strats, next_gen))
#     blocked_wins_percent.append(return_total_wins_blocked(top_five_strats, next_gen))
#     generations.append(2+i)
#     next_gen = breeding_algorithm(top_five_strats, next_gen, 3+ i)
#     scores = run_games(next_gen)
#     top_five_strats = get_top_strats(next_gen, scores)
#     versus_previous_gen_scores.append(versus_gens(top_five_strats, next_gen, old_gen))

# versus_gen_one_scores.append(versus_gens(top_five_strats, next_gen, gen_one_strats_dict))
# versus_previous_gen_scores.append(versus_gens(top_five_strats, next_gen, old_gen))
# realized_wins_percent.append(return_total_wins_realized(top_five_strats, next_gen))
# blocked_wins_percent.append(return_total_wins_blocked(top_five_strats, next_gen))

# generations.append(52)

# print("plotting realized wins")
# plt.plot(generations, realized_wins_percent)
# plt.savefig("possible_wins_realized.png")
# plt.clf()

# print("plotting initial genetic algorithm")
# plt.plot(generations, versus_gen_one_scores)
# plt.savefig("versus_gen_one.png")
# plt.clf()

# print("plotting versus the previous generation")
# plt.plot(generations, versus_previous_gen_scores)
# plt.savefig("previous_gen_versus.png")
# plt.clf()

# print("plotting possible wins blocked")
# plt.plot(generations, blocked_wins_percent)
# plt.savefig("wins_blocked.png")
# print("done")
