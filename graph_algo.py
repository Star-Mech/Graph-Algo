from queue import SimpleQueue

graph = {
    'a': ['b', 'c'],
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
        current = stack.pop()  # take last element
        for neighbor in graph.get(current):
            stack.append(neighbor)

        print(current, end='->\t')


traversal_depth_first(graph, 'a')
print()

print('<---Breadth First Iterative--->')


def traversal_breadth_first(graph, start):
    que = SimpleQueue()
    if start: que.put(start)

    while not que.empty():  # While something in there
        current = que.get()
        for neighbor in graph.get(current):
            que.put(neighbor)

        print(current, end='->\t')


traversal_breadth_first(graph, 'a')
print()

print('<---Depth First Recursively ------>')


def traversal_depth_first_recursively(graph, current):
    if current == None:
        return
    print(current, end='->\t')
    for neighor in graph.get(current):
        traversal_depth_first_recursively(graph, neighor)


traversal_depth_first_recursively(graph, 'a')
print()


g1 = {
    'f':['g','i'],
    'g':['h'],
    'h':[],
    'i':['g', 'k'],
    'j':['i'],
    'k':[],
}
def has_path_depth_recursive(graph, src, dst) -> bool:
    if src == dst:
        return True

    for neigbor in graph.get(src):
        r = has_path_depth_recursive(g1, neigbor, dst)
        if r: # if path found
            return r

    return False

print('<---Has Path Recursively ------>')
print(has_path_depth_recursive(g1, 'f', 'k'))
print(has_path_depth_recursive(g1, 'f', 'h'))
print(has_path_depth_recursive(g1, 'g', 'i'))
print(has_path_depth_recursive(g1, 'j', 'k'))
print(has_path_depth_recursive(g1, 'j', 'h'))
print(has_path_depth_recursive(g1, 'j', 'f'))

# Now give the edges, convert it into undirected graph where we can traverse both forward and backward
e1 = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n'],
]
def edge_to_graph(edges: list):
    graph = {}
    for edge in edges:
        for node_index in range(len(edge)):
            if edge[node_index] not in graph:
                graph[edge[node_index]] = []
            # print([edge[i] for i in range(node_index + 1, len(edge))])
            for i in range(len(edge)):
                if edge[i] != edge[node_index]:
                    graph[edge[node_index]].append(edge[i])

    return graph
print(edge_to_graph(e1))