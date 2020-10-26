def floydwarshall(graph):
 
    # Initialize dist and pred:
    # copy graph into dist, but add infinite where there is
    # no edge, and 0 in the diagonal
    dist = {}
    pred = {}
    for u in graph:
        dist[u] = {}
        pred[u] = {}
        for v in graph:
            dist[u][v] = 1000
            pred[u][v] = -1
        dist[u][u] = 0
        for neighbor in graph[u]:
            dist[u][neighbor] = graph[u][neighbor]
            pred[u][neighbor] = u
 
    for t in graph:
        # given dist u to v, check if path u - t - v is shorter
        for u in graph:
            for v in graph:
                newdist = dist[u][t] + dist[t][v]
                if newdist &lt; dist[u][v]:
                    dist[u][v] = newdist
                    pred[u][v] = pred[t][v] # route new path through t
 
    return dist, pred
 
 
 
graph = {0 : {1:6, 2:8},
         1 : {4:11},
         2 : {3: 9},
         3 : {},
         4 : {5:3},
         5 : {2: 7, 3:4}}
 
dist, pred = floydwarshall(graph)
print &quot;Predecesors in shortest path:&quot;
for v in pred: print &quot;%s: %s&quot; % (v, pred[v])
print &quot;Shortest distance from each vertex:&quot;
for v in dist: print &quot;%s: %s&quot; % (v, dist[v])
 
 
 
 
 
python floydwarshall.py 
Predecesors in shortest path:
0: {0: -1, 1: 0, 2: 0, 3: 2, 4: 1, 5: 4}
1: {0: -1, 1: -1, 2: 5, 3: 5, 4: 1, 5: 4}
2: {0: -1, 1: -1, 2: -1, 3: 2, 4: -1, 5: -1}
3: {0: -1, 1: -1, 2: -1, 3: -1, 4: -1, 5: -1}
4: {0: -1, 1: -1, 2: 5, 3: 5, 4: -1, 5: 4}
5: {0: -1, 1: -1, 2: 5, 3: 5, 4: -1, 5: -1}
Shortest distance from each vertex:
0: {0: 0, 1: 6, 2: 8, 3: 17, 4: 17, 5: 20}
1: {0: 1000, 1: 0, 2: 21, 3: 18, 4: 11, 5: 14}
2: {0: 1000, 1: 1000, 2: 0, 3: 9, 4: 1000, 5: 1000}
3: {0: 1000, 1: 1000, 2: 1000, 3: 0, 4: 1000, 5: 1000}
4: {0: 1000, 1: 1000, 2: 10, 3: 7, 4: 0, 5: 3}
5: {0: 1000, 1: 1000, 2: 7, 3: 4, 4: 1000, 5: 0}
