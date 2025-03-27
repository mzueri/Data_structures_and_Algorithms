"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""

def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    # use Kahn's algorithm

    def get_neighbors(nodes,edges):
        neighbors={node:[] for node in nodes}
        for edge in edges:
            neighbors[edge[1]].append(edge[0])
        return neighbors
    
    def get_indegrees(nodes,edges):
        indegrees={node:0 for node in nodes}
        for edge in edges: 
            indegrees[edge[0]]+=1
        return indegrees

    nodes=list(range(numCourses))
    neighbors=get_neighbors(nodes,prerequisites)
    indegrees=get_indegrees(nodes,prerequisites)
    
    queue=[]
    # add nodes with indegree 0 to the queue.
    for node in indegrees.keys():
        if indegrees[node]==0:
            queue.append(node)
    
    if queue==[]: # if there is no node with indegree 0, then there must be a directed cycle and thus, no topological sorting.
        return []

    topological_sorting=[]
    while queue!=[]:
        curr=queue.pop()
        # add the nodes with remaining indegree 0 to the topolocial sorting
        topological_sorting.append(curr)
        # Remove the node curr from the graph. Note that it suffices to only remove the outgoing edges of curr since it has no incoming edges. 
        for node in neighbors[curr]:
            indegrees[node]-=1
            if indegrees[node]==0:
                queue.append(node)
        del neighbors[curr]
    
    if len(topological_sorting)==len(nodes):
        return topological_sorting
    else:
        return []