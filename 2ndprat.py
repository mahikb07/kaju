###Practical No.02
##########Aim: Implement Recursive Best First Search Algorithm to solve given problem.

import sys
romania_map={
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Lugoj':{'Timisoara': 111, 'Mehadia': 70},
    'Fagaras':{'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu':80 , 'Craiova': 146, 'Pitesti': 97},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova':{'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Pitesti':{'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest':{'Fagaras': 211, 'Pitesti': 101}
}
heuristics ={
    'Arad': 366,
    'Zerind': 374,
    'Timisoara': 329,
    'Sibiu':253,
    'Oradea': 380,
    'Lugoj': 244,
    'Fagaras': 176,
    'Rimnicu Vilcea': 193,
    'Mebadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Pitesti': 100,
    'Bucharest': 0
}
def rbfs_search(start, goal, path, f_limit):
    if start==goal:
        return path
    successors = romania_map[start]
    if len(successors) == 0:
        return None
    sorted_successors= sorted(successors, key=lambda x: successors[x]+ heuristics[x])
    for city in sorted_successors:
        new_path = path + [city]
        f_value = successors [city] + heuristics[city]
        if f_value> f_limit:
            return None
        result=rbfs_search(city, goal, new_path, min(f_limit, f_value))
        if result is not None:
            return result
    return None
def recursive_best_first_search(start, goal):
    f_limit=sys.maxsize
    path=[start]
    while True:
        result= rbfs_search(start, goal, path, f_limit)
        if result is not None:
            return result
        f_limit=sys,maxsize
start_city='Arad'
goal_city='Bucharest'
path=recursive_best_first_search(start_city, goal_city)
if path is None:
    print("Path not found!")
else:
    print("Path:", path)
    print("Cost:",sum(romania_map[path[i]][path[i+1]] for i in range(len(path)-1)))
