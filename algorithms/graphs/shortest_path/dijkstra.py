
# Given a graph G=(V,E_l) where E_l is a set of 2-tuples, first tuple element being a directed edge in G and the second 
# being the non-negative weight of the edge. Let s be an element in V. 
# For each node return it the shortes path to this node. 

def dijkstra(V,E_l,s):
    assert isinstance(V,set), "Make sure that V is given as a set"
    assert s in V, "s is not in V."
    assert all(edge[1]>=0 for edge in E_l), "Only non-negative weights are allowed for the Dijkstra algorithm."

    visited=set()
    distances={node:distance for node,distance in zip(V,[0 if v==s else float("inf") for v in V])}
    prev_node={node:None for node in V}

    while visited!=V:
        # find the next non-visited node with minimal distance from s. 
        distances_to_nonvisited={node:distance for node,distance in distances.items() if node not in visited}
        min_distance=min(list(distances_to_nonvisited.values()))
        for node in list(distances_to_nonvisited.keys()):
            if distances_to_nonvisited[node]==min_distance:
                curr=node
        visited.add(curr)

        # get the directed edges pointing away from curr to a non-visited node and update the distances.
        for edge in E_l:
            if edge[0][0]==curr and edge[0][1] not in visited:
                if distances[edge[0][1]]>distances[curr]+edge[1]:
                    distances[edge[0][1]]=distances[curr]+edge[1]
                    prev_node[edge[0][1]]=edge[0][0]

    return distances,prev_node



# test example
V=set(["a","b","c","d","e"])
E_l=set([
        (("a","b"),4),
       (("a","c"),2),
       (("b","c"),3),
       (("b","d"),2),
       (("b","e"),3),
       (("c","b"),1),
       (("c","d"),4),
       (("c","e"),5),
       (("e","d"),1)
       ])
d,p=dijkstra(V,E_l,"a")
print(d)
print(p)
