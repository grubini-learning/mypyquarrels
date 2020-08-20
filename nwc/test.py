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

    def bellman_ford(self):
        for _ in range(self.vertices - 1):
            for vertex in range(1, self.vertices + 1):
                adjs = self.edges_vertices[vertex][1]
                if self.edges_vertices[vertex][0] != self.INFINITY:
                    for destination in adjs:
                        self.relaxation(vertex, destination)

    """def ngc(self):
        change = False
        for key, value in self.edges_vertices.items():
            adjs = value[1]
            for destination in adjs:
                changed = self.relaxation(key, destination)
                if changed:
                    change = True
                    return changed
        return change"""
    """def ngc(self):
        change = False
        for vertex in range(1, len(self.edges_vertices)):
                adjs = self.edges_vertices[vertex][1]
                for destination in adjs:
                    if self.relaxation(vertex, destination):
                        return True

        return change"""

    def ngc(self):
        change = False
        self.set_init_distances()
        self.bellman_ford()
        for vertex in range(1, len(self.edges_vertices)):
            adjs = self.edges_vertices[vertex][1]
            if self.edges_vertices[vertex][0] != self.INFINITY:
                    for destination in adjs:
                        changed = self.relaxation(vertex, destination)
                        if changed:
                            change = True
                            return "1"
        return "-1"

def main():
    with open("test.txt", "r") as f:
        source = 1
        s = ""
        graphs = int(f.readline().strip())
        #f.readline()
        result = []

        line = f.readline().split()
        vertices, edges = map(int, line)
        g = Graph(vertices, source)
        #for graph in range(graphs):
        while True:
            line = f.readline().split()
            if len(line) == 3:
                nodea, nodeb, weight = map(int, line)
                g.add_edge(nodea, nodeb,  weight)
            elif len(line) == 2:
                    s += f"{g.ngc()} "
                    vertices, edges = map(int, line)
                    g = Graph(vertices, source)
            else:
                s += f"{g.ngc()} "
                break

if '__main()__':
    main()