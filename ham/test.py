class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.directions = {vertex: set() for vertex in range(vertices + 1)}
        self.seen = set()
        self.topological_sort = []
        self.stack = []

    def add_edge(self, nodea, nodeb):
        self.directions[nodea].add(nodeb)

    def get_graph(self):
        return self.directions

    def get_topological_sort(self):
        return self.topological_sort

    def get_seen(self):
        return self.seen

    def validation(self):
        for key in self.directions.keys():
            if len(self.directions[key]) > 0:
                if key not in self.seen:
                    self.seen.add(key)
                    self.dfs_traversal(key)

    def dfs_traversal(self, node):
        self.seen.add(node)
        for neighbor in self.directions[node]:
            if neighbor not in self.seen:
                self.dfs_traversal(neighbor)
        self.topological_sort.insert(0, node)

    def check_consecutive(self):
        for i in range(len(self.topological_sort) - 1):
            if self.topological_sort[i + 1] not in self.directions[self.topological_sort[i]]:
                return False
        return True

def main():
    with open("test2.txt", "r") as f:
        k = int(f.readline().strip())
        print(str(k))
        f.readline()

        for n in range(k):
            vertices, edges = list(map(int, f.readline().split(" ")))
            print(f' vs {vertices}  edgs {edges}')
            g = Graph(vertices)
            while True:
                line = f.readline()
                if line == '\n' or not line:
                    break
                print(f'the line {line}')
                nodea, nodeb = map(int, line.split())
                g.add_edge(nodea, nodeb)

            g.validation()

            if g.check_consecutive():
                print(1, end=" ")
                for i in g.get_topological_sort():
                    print(i, end=" ")
                print("")
            else:
                print(-1)

if '__main__()':
    main()