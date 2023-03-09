import util


def prim(vertices, edges: list):
    span_tree = []
    free_vertices = [i + 1 for i in range(vertices)]
    used_vertices = []
    source = 1

    edges.sort(key=lambda edge: edge[2])
    while len(free_vertices) != 0:
        if len(used_vertices) == 0:
            free_vertices.remove(source)
            used_vertices.append(source)
        connected_edges = util.find_edges(used_vertices, edges)
        for edge in connected_edges:
            if edge[0] in free_vertices or edge[1] in free_vertices:
                span_tree.append(edge)
                if edge[0] in free_vertices:
                    free_vertices.remove(edge[0])
                    used_vertices.append(edge[0])
                else:
                    free_vertices.remove(edge[1])
                    used_vertices.append(edge[1])
                break

    return span_tree
