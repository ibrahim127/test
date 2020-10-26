import heapq
from sys import stdin, stdout
 
# Dijktra's shortest path algorithm. Prints the path from source to target.
 
 
def dijkstra(adj, source, target):
    INF = ((1<<63) - 1)//2
    pred = { x:x for x in adj }
    dist = { x:INF for x in adj }
    dist[ source ] = 0
    PQ = []
    heapq.heappush(PQ, [dist[ source ], source])
 
    while(PQ):
        u = heapq.heappop(PQ)  # u is a tuple [u_dist, u_id]
        u_dist = u[0]
        u_id = u[1]
        if u_dist == dist[u_id]:
            #if u_id == target:
            #    break
            for v in adj[u_id]:
               v_id = v[0]
               w_uv = v[1]
               if dist[u_id] +  w_uv < dist[v_id]:
                   dist[v_id] = dist[u_id] + w_uv
                   heapq.heappush(PQ, [dist[v_id], v_id])
                   pred[v_id] = u_id
                
    if dist[target]==INF:
        stdout.write("There is no path between ", source, "and", target)
    else:
        st = []
        node = target
        while(True):
            st.append(str(node))
            if(node==pred[node]):
                break
            node = pred[node]
        path = st[::-1]
        stdout.write("The shortest path is: " + " ".join(path) + "\n\n")
        stdout.write("The distance from 'a' to 'i' is: " + str(dist['i']) + "\n\n")
        stdout.write("distance dictionary: " + str(dist) + "\n\n")
        stdout.write("predecessor dictionary: " + str(pred))
     
#----------------------------------------------------------
 
def main():
     
    adj = {'c': [('b', 0.32), ('e', 0.17), ('f', 0.91)],
         'g': [('d', 0.17), ('e', 0.27), ('h', 0.92)],
         'i': [('e', 1.98), ('f', 0.13), ('h', 0.22)],
         'f': [('c', 0.91), ('e', 0.33), ('i', 0.13)],
         'h': [('e', 0.18), ('g', 0.92), ('i', 0.22)],
         'd': [('a', 0.72), ('e', 0.29), ('g', 0.17)],
         'a': [('b', 0.95), ('d', 0.72), ('e', 1.75)],
         'e': [('a', 1.75), ('b', 0.82), ('c', 0.17), ('d', 0.29), ('f', 0.33), ('g', 0.27), ('h', 0.18), ('i', 1.98)],
         'b': [('a', 0.95), ('c', 0.32), ('e', 0.82)]}
         
    dijkstra(adj, 'a', 'i')
 
#----------------------------------------------------------
 
if __name__ == "__main__":
    main()
