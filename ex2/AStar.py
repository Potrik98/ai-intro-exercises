# A modified version of astar pathfinding by
# Christian Careaga (christian.careaga7@gmail.com)
# found on
# http://code.activestate.com/recipes/578919-python-a-pathfinding-with-binary-heap/

import numpy
from heapq import heappush, heappop

wall = 1

# manhattan distance as heuristic
def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def is_inside(node, array):
    return 0 <= node[0] < array.shape[0] and 0 <= node[1] < array.shape[1]

def astar(array, start, goal):
    neighbors = [(0,1),(0,-1),(1,0),(-1,0)] # 4-connected grid

    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))
    
    while oheap:
        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j            
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if is_inside(neighbor, array):
                if array[neighbor[0]][neighbor[1]] == wall:
                    continue # skip if cell is a wall
                
                if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                    continue # skip if cell is already visited and has a with a better score
                    
                if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heappush(oheap, (fscore[neighbor], neighbor))
                
    return False # False if no path was found
