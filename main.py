import boruvka
import kruskal
import prim
import util

if __name__ == '__main__':
    vertices, edges = util.graph_builder("graph.txt")

    kruskal_tree = kruskal.kruskal(vertices, edges)
    print("-- Kruskal's Algorithm --")
    util.trace(kruskal_tree)
    print(" ")

    print("-- Prim's Algorithm --")
    prim_tree = prim.prim(vertices, edges)
    util.trace(prim_tree)
    print(" ")

    print("-- Borůvka's Algorithm --")
    boruvka_tree = boruvka.boruvka(vertices, edges)
    util.trace(boruvka_tree)
    print(" ")
