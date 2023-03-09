import util


def kruskal(vertices, edges: list):
    span_tree = []
    forest = [[i + 1] for i in range(vertices)]

    edges.sort(key=lambda edge: edge[2])
    for edge in edges:
        set_1 = util.find_set(forest, edge[0])
        set_2 = util.find_set(forest, edge[1])
        if set_1 != set_2:
            span_tree.append(edge)
            set_1 += set_2
            forest.remove(set_2)
        if len(forest) == 1:
            break

    return span_tree
