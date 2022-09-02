from queue import Queue

graph = {
    'a': ['b','c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}


def traversal_depth_first(graph, start=None):
    stack = []
    if start: stack.append(start)

    while stack:
        current = stack.pop() # take last element
        for neighbor in graph.get(current):
            stack.append(neighbor)

        print(current)

traversal_depth_first(graph, 'a')
