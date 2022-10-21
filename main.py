import generator as g
import nearestNeighbour as nn

RAND_STARTING_POINT = False


#g.generate_Instance(5,10)
l = nn.loadData("a.bench")
nn.nearestN(l,RAND_STARTING_POINT)
