####Practical No.04
##Aim: Implement Iterative Depth First Search Algorithm to solve given problem.

romania_map = {
'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
'Zerind': ['Arad', 'Oradea'],
'Oradea': ['Zerind', 'Sibiu'],
'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
'Timisoara': ['Arad', 'Lugoj'],
'Lugoj': ['Timisoara', 'Mehadia'],
'Mehadia': ['Lugoj', 'Drobeta'],
'Drobeta': ['Mehadia', 'Craiova'],
'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
'Fagaras': ['Sibiu', 'Bucharest'],
'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
'Giurgiu': ['Bucharest'],
'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
'Hirsova': ['Urziceni', 'Eforie'],
'Eforie': ['Hirsova'],
'Vaslui': ['Urziceni', 'Iasi'],
'Iasi': ['Vaslui', 'Neamt'],
'Neamt': ['Iasi']
}
def iterative_deepening_dfs(start, goal, depth_limit):
    for depth in range(depth_limit + 1):
        visited = set()
        result = depth_limited_dfs(start, goal, depth, visited)
        if result is not None:
            return result
    return None
def depth_limited_dfs(node, goal, depth, visited):
    if node == goal:
        return [node]
    if depth == 0:
        return None
    visited.add(node)
    for neighbor in romania_map[node]:
        if neighbor not in visited:
            result = depth_limited_dfs(neighbor, goal, depth - 1, visited)
            if result is not None:
                return [node] + result
    return None
start_city = 'Arad'
goal_city = 'Bucharest'
depth_limit = 10
path = iterative_deepening_dfs(start_city, goal_city, depth_limit)
if path is not None:
    print("Path found:", ' -> '.join(path))
else:
    print("Path not found within depth limit.")
