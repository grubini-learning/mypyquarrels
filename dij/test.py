import sys
from heapq import heappop,heappush

class Graph:
    def __init__(self,N):
        self.__adj_list_with_weight = {i:{} for i in range(1,N+1)}

    def add_edge_with_weight(self, u, v, w):
        self.__adj_list_with_weight[u][v] = w

    def get_graph(self):
    	return self.__adj_list_with_weight

def dijkstra(graph, source):
    distances = [-1] * (len(graph)+1)
    heap = [(0, source)]
    while heap:
        weight, v = heappop(heap)
        if distances[v] == -1:
            distances[v] = weight
            for negihbour, edge_cost in graph[v].items():
                if distances[negihbour] == -1:
                    heappush(heap, (weight + edge_cost, negihbour))

    return distances

def main():
    with open("test.txt", "r") as f:
        N,E = map(int,f.readline().split())
        g = Graph(N)
        while True:
            line = f.readline()
            if not line:
                break

            u,v,w = map(int,line.split())
            g.add_edge_with_weight(u,v,w)

    source = 1
    s = ' '.join(map(str,dijkstra(g.get_graph(),source)[1:]))

    with open('./result2.txt', 'w') as f:
        f.write(s)

if '__main()__':
    main()