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

        print(current, end='\t')

traversal_depth_first(graph, 'a')
print()
print('<---Depth First Recursively ------>')
def traversal_depth_first_recursively(graph, current):
    if current == None:
        return
    print(current, end='\t')
    for neighor in graph.get(current):
        traversal_depth_first_recursively(graph, neighor)

traversal_depth_first_recursively(graph, 'a')
print()