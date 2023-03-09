import util


def boruvka(vertices, edges: list):
    span_tree = []
    forest = [[i + 1] for i in range(vertices)]

    while len(forest) > 1:
        cheapest_edges = []
        for tree in forest:
            current_edges = util.find_edges(tree, edges)
            for edge in current_edges:
                if util.find_set(forest, edge[0]) != util.find_set(forest, edge[1]):
                    cheapest_edges.append(edge)
                    break

        for edge in cheapest_edges:
            if edge not in span_tree:
                span_tree.append(edge)
                set1 = util.find_set(forest, edge[0])
                set2 = util.find_set(forest, edge[1])
                set1 += set2
                forest.remove(set2)

    return span_tree
