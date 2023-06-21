import heapq

def dijkstra(graph,vertex):
    dist = { v : float('inf') for v in graph.keys()}
    dist[vertex] = 0
    heap = []
    for v,w in graph[vertex]:
        heapq.heappush(heap,[w,v])
    while heap:
        curr_weigth, curr_vertex = heapq.heappop(heap)
        if dist[curr_vertex] > curr_weigth:
            dist[curr_vertex] = curr_weigth
            for v,w in graph[curr_vertex]:
                heapq.heappush(heap,[dist[curr_vertex]+w,v])
    return dist




if __name__=='__main__':
    graph = {
        'A' : [['B',2],['C',6],['F',1]],
        'B' : [['A',2],['D',1],['E',8]],
        'C' : [['A',6],['E',3],['F',3]],
        'D' : [['B',1]],
        'E' : [['B',8],['C',3],['F',4],['H',3]],
        'F' : [['A',1],['C',3],['E',4],['G',2]],
        'G' : [['F',2],['H',1]],
        'H' : [['E',3],['G',1]]
    }
    ans = dijkstra(graph,'A')
    print(ans)
