import sys
import igraph as ig
import time

def read_graph(filename):
    graph = ig.Graph(directed=False)
    with open(filename) as file:
        lines = file.readlines()
    graph.add_vertices(int(lines[0]))

    for i in range(len(graph.vs)):
        graph.vs[i]["id"] = i
        graph.vs[i]["label"] = str(i)

    edges = []
    for line in lines[1:]:
        a, b = line.split()
        edges.append((int(a), int(b)))
    graph.add_edges(edges)

    file.close()
    return graph


def main():
    graph1 = read_graph(sys.argv[1])
    graph2 = read_graph(sys.argv[2])

    t = time.time()
    print("BLISS:")
    if graph1.isomorphic_bliss(graph2):
        print("Graphs are isomorphic.")
        print("Time is " + str(time.time() - t))
    else:
        print("Graphs are not isomorphic.")

    t = time.time()
    print("VF2:")
    if graph1.isomorphic_vf2(graph2):
        print("Graphs are isomorphic.")
        print("Time is " + str(time.time() - t))
    else:
        print("Graphs are not isomorphic.")

    t = time.time()
    print("LAD:")
    if graph1.subisomorphic_lad(graph2) and graph2.subisomorphic_lad(graph1):
        print("Graphs are isomorphic.")
        print("Time is " + str(time.time() - t))
    else:
        print("Graphs are not isomorphic.")


if __name__ == "__main__":
    main()