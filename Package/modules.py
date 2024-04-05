

def generateE(names,goals,goals_avoided,assists): 
    """This function takes 4 different ordered data structures and zips them into a single structure, which will be returned in list type"""
    names_lowered = names.lower ()
    names_list = names_lowered.split(', ')
    zipped_estructure = zip (names_list, goals, goals_avoided, assists)
    result_list =  list (zipped_estructure)
    return (result_list)



def calculate_scorer(hockey_data,stat):
    """This function finds the player who scored the most goals or who avoided the most goals
        or who made the most assists through the stat parameter that determines which stat we
        want to search for.
        1: goals
        2: goals avoided
        3: assists"""
    max_player = max(hockey_data, key=lambda x: x[stat])
    return max_player

def most_valuavle_player(hockey_data):
    """This function returns the most valuable player by sorting the list from most valuable player to least valuable player
       the mvp its calculated by three conditions: goals scored 1.5, goals avoided 1.25, assists 1"""
    sorted_players = sorted(hockey_data, key=lambda x: x[1]*1.5 + x[2]*1.25 + x[3], reverse=True)
    best_name = sorted_players[0][0]
    return best_name