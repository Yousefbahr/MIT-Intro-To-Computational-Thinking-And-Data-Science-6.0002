from graph import *
from ps2 import*


g = Digraph()

na = Node('a')
nb = Node('b')
nc = Node('c')
nd = Node('d')
g.add_node(na)
g.add_node(nb)
g.add_node(nc)
g.add_node(nd)
e1 = WeightedEdge(na, nb, 10, 7)
e2 = WeightedEdge(na, nc, 10, 6)
e3 = WeightedEdge(nb, nc, 3, 1)
e4 = WeightedEdge(nb, nd, 5, 2)
e5 = WeightedEdge(nc, nd, 8, 3)
g.add_edge(e1)
g.add_edge(e2)
g.add_edge(e3)
g.add_edge(e4)
g.add_edge(e5)

print(g)
print()

for node in g.nodes:
    if node.name == "a":
        print(node)

#print(g.has_node(na))

l = get_best_path(g, "a", "d", [[], 0 ,0], 999, 999, None)
print(l)





