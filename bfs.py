# Name: Johan Cruz Hernandez
# Description: contains BFS implementation.

from collections import deque

# Purpose: returns a list of the shortest path between the
# start vertex object and the end vertex object
# Parameters: receives references to vertex objects and
# a dictionary of strings as keys and vertex objects as
# values
def breadth_first_search(start, end, vertex_dictionary):
    frontier = deque()
    backpointer = {}

    frontier.append(start)
    backpointer[start] = None

    while len(frontier) > 0:
        x = frontier.popleft()
        if x == end:
            path = []
            while x is not None:
                path.append(x)
                x = backpointer[x]
            return path
        else:
            for adj_vertices in x.adj_list:
                if adj_vertices not in backpointer:
                    frontier.append(adj_vertices)
                    backpointer[adj_vertices] = x

    return []
