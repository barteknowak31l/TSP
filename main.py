import generator as g
import nearestNeighbour as nn


g.generate_Instance(5,10)
l = nn.loadData("a.bench")
nn.nearestN(l)
