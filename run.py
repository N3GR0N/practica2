from Package.data import * 
from Package.modules import *  


hockey_data = generateE(names,goals,goals_avoided,assists)


for player in hockey_data:
    print(player)  



goal_scorer = calculate_scorer(hockey_data,1)
print(f'El/La mayor goleador/a fue: {goal_scorer[0]} y anoto: {goal_scorer[1]} goles. ')


mvp = most_valuavle_player(hockey_data)
print (f'El/La jugador/a mas influyente del equipo es: {mvp}')


total_goals = sum(goals)
goals_match = total_goals/matchs
print (f'El promedio de goles anotados fue: {goals_match}.\nEl promedio personal de {goal_scorer[0]} fue de: {goal_scorer[1]/matchs} ') 
