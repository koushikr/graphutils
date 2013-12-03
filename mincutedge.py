'''
	The minimum cut problem is to cut a graph into two disjoint subgraphs by removing a minimum number of edges
	http://en.wikipedia.org/wiki/Karger's_algorithm - Implementation of Karger's algorithm
	
	Notes : Running this algorithm once wont generate a min cut. But running it a fair number of times (log(N) ^ 2)
	will reduce the error rate to O(1/n^2)
'''
from random import choice

def mincut(g):
	while len(g) &gt; 2:
        v1 = choice(g.keys())
        gv1 = g[v1]
        v2 = gv1.most_common(1)[0][0]
        gv2 = g[v2]
        #1. remove v2's list
        del g[v2]
        #2. remove self-loop
        del gv2[v1]
        del gv1[v2]
        #3. attach v2's list to v1
        gv1.update(gv2)
        #4. replace all appearance of v2 as v1
        for v3 in gv2:
            gv3 = g[v3]
            gv3[v1] += gv3[v2]
            del gv3[v2]
        return g.itervalues().next().most_common(1)[0][1]

g = {}
with open('data.txt') as f:
    for line in f:
        ints = [int(x) for x in line.split()]
    from collections import Counter
    g[ints[0]] = Counter(ints[1:])

from copy import deepcopy
cuts = [mincut(deepcopy(g)) for i in range(5)]
print min(cuts), cuts
