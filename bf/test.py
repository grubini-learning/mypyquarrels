class Graph:
    def __init__(self, vertices, source):
        self.source = source
        self.vertices = vertices
        self.INFINITY = 999999999
        self.edges_vertices = {vertex: [0, {}] for vertex in range(vertices + 1)}

    def set_init_distances(self):
        for vertex in range(len(self.edges_vertices)):
            if vertex == 0:
                continue
            else:
                if vertex == self.source:
                    self.edges_vertices[vertex][0] = 0
                else:
                    self.edges_vertices[vertex][0] = self.INFINITY

    def add_edge(self, nodea, nodeb, weight):
        self.edges_vertices[nodea][1].update({ nodeb: (weight, self.INFINITY)})

    def get_edge(self, nodea, nodeb):
        return self.edges_vertices[nodea][1][nodeb]

    def relaxation(self, nodea, nodeb):
        nodea_w = self.edges_vertices[nodea][0]
        edge = self.get_edge(nodea, nodeb)
        edge_w = edge[0]
        nodeb_w = edge[1]

        if nodea_w != self.INFINITY:
            if nodea_w + edge_w < nodeb_w:
                relaxed = (edge_w, nodea_w + edge_w)
                self.edges_vertices[nodea][1][nodeb] = relaxed
                self.edges_vertices[nodeb][0] = nodea_w + edge_w
                self.update_weight(nodeb, nodea_w + edge_w)
                return True
        return False

    def update_weight(self, node, weight):
        for vertex in self.edges_vertices:
            neighbors = self.edges_vertices[vertex][1]
            if node in neighbors:
                neighbors[node] = (neighbors[node][0], weight)

    def bellmont_ford(self):
        for _ in range(self.vertices - 1):
            for vertex in range(1, len(self.edges_vertices)):
                adjs = self.edges_vertices[vertex][1]
                if len(adjs) > 0:
                    for destination in adjs:
                        self.relaxation(vertex, destination)

    def negative_cycle(self):
        change = False
        for _ in range(1):
            for vertex in range(1, len(self.edges_vertices)):
                adjs = self.edges_vertices[vertex][1]
                if len(adjs) > 0:
                    for destination in adjs:
                        changed = self.relaxation(vertex, destination)
                        if changed:
                            change = True
                            break
        return change

    def is_reachable(self, graph, start, visited = None):
        if visited is None:
            visited = set()
        visited.add(start)

        print(start)
        adjs = graph[start]

        for key in set(adjs) - visited:
            self.is_reachable(graph, key, visited)
        return visited

    def get_graph(self):
        return self.edges_vertices

    def get_simple_graph(self):
        graph = {vertex: set([]) for vertex in range(self.vertices + 1)}

        for vertex in range(len(self.edges_vertices)):
            for adj in self.edges_vertices[vertex][1].keys():
                graph[vertex].add(adj)
        return graph


    def get_distances(self):
        s = ""
        if not self.negative_cycle():
            for vertex in range(1, len(self.edges_vertices)):
                if vertex in self.is_reachable(self.get_simple_graph(), self.source):
                    s += f"{self.edges_vertices[vertex][0]} "
                else:
                    s += "x "
        else:
            s = "x"
        return s

def main():
    g = Graph(9, 1)
    """g.add_edge(1, 2, 4)
    g.add_edge(1, 4, 5)
    g.add_edge(3, 2, -10)
    g.add_edge(4, 3, 3)
    g.set_init_distances()
    g.bellmont_ford()
    g.get_distances()"""
    """g.add_edge(1, 2, 6)
    g.add_edge(1, 4, 5)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 5, -1)
    g.add_edge(3, 2, -2)
    g.add_edge(3, 5, 1)
    g.add_edge(4, 3, -2)
    g.add_edge(4, 6, -1)
    g.add_edge(5, 7, 3)
    g.add_edge(6, 7, 3)"""
    g.add_edge(1, 2, 10)
    g.add_edge(3, 2, 1)
    g.add_edge(3, 4, 1)
    g.add_edge(4, 5, 3)
    g.add_edge(5, 6, -1)
    g.add_edge(7, 6, -1)
    g.add_edge(8, 7, 1)
    g.add_edge(1, 8, 8)
    g.add_edge(7, 2, -4)
    g.add_edge(2, 6, 2)
    g.add_edge(6, 3, -2)
    g.add_edge(9, 5, -10)
    g.add_edge(9, 4, 7)
    g.set_init_distances()
    g.bellmont_ford()
    g.get_distances()

if '__main__()':
    main()