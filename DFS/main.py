# https://www.tutorialspoint.com/python_data_structure/python_graph_algorithms.htm

'''
## Depth First Traversal :
Also called depth first search(DFS), this algorithm traverses a graph in a depth
ward motion and uses a stack to remember to get the next vertex to start a search,
when a dead end occurs in any iteration. We implement DFS for a graph in python
using the set data types as they provide the required functionalities to keep track
of visited and unvisited nodes.
'''

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


gdict = {"a": set(["b"]),
        "b": set(["a", "d"]),
        "c": set(["a", "d"]),
        "d": set(["e"]),
        "e": set(["a", "c"])
        }


dfs(gdict, 'a')
