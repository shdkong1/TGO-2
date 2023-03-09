def graph_builder(filename):
    vertices = 0
    edges = []

    file = open(filename)
    for line in file:
        if 'vertices' in line:
            vertices = int(line.split()[1])
        else:
            start, end, weight = line.split()
            edges.append([int(start), int(end), int(weight)])

    return vertices, edges


def trace(tree: list):
    tree.sort(key=lambda vertex: vertex[0])

    print("Edges of spanning tree:")
    print(tree)

    length = 0
    for edge in tree:
        length += edge[2]
    print("Length of spanning tree: " + str(length))


def find_set(forest, vertex):
    for tree in forest:
        if vertex in tree:
            return tree


def find_edges(vertices, edges):
    connected_edges = []
    for edge in edges:
        if edge[0] in vertices or edge[1] in vertices:
            connected_edges.append(edge)

    connected_edges.sort(key=lambda edge: edge[2])
    return connected_edges
