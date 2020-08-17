from enum import Enum

class Status(Enum):
    UNVISITED = 0
    EXPLORING = 1
    COMPLETE = 2

class Graph:
    def __init__(self, vertices, directions):
        self.vertices = vertices
        self.visited = [Status.UNVISITED.value] * self.vertices
        self.stack = []
        self.set_structure()
        self.fill_structure(directions)

    def set_structure(self):
        self.edge_list = [[] for _ in range(0, self.vertices)]

    def fill_structure(self, directions):
        for edge in directions:
            vertex_one, vertex_two = edge
            self.edge_list[vertex_one - 1].append(vertex_two)
            self.edge_list[vertex_two - 1].append(vertex_one)

    def detect_cycle(self):
        for nodes in self.edge_list:
            for index in range(self.vertices):
                self.stack.append(index + 1)
                if self.visited[index] == Status.UNVISITED.value and not self.dfs_traversal(index):
                    return -1
                self.stack.clear()
        return 1

    def dfs_traversal(self, node):
        """if self.visited[node] == Status.EXPLORING.value and len(self.stack) == 4:
            return False"""

        #self.visited[node] = Status.EXPLORING.value
        for neighbor in self.edge_list[node]:
            if neighbor not in self.stack:
                self.stack.append(neighbor)
                self.visited[neighbor - 1] = Status.EXPLORING.value
            else:
                found_at = self.stack.index(neighbor)
                is_cycle = (len(self.stack) - 1) - found_at == 3
                if is_cycle and visited[neighbors - 1] == Status.COMPLETE.value:
                    return False
                continue
            if not self.dfs_traversal(neighbor - 1):
                return False

        self.visited[node - 1] = Status.COMPLETE.value
        return True


def main():
    with open("test.txt", "r") as my_file:
        text_data = my_file.readlines()
        graphs = int(text_data[0].strip())
        data = ""
        result = []
        for line in text_data:
            data += line.replace("\n", "|")
        data = [[pair for pair in text.split("|")] for text in data.split("||")]

        datastest = [[[int(nu) for nu in num.split()]
                      for num in number] for number in data[1:]]

        for index in range(0, graphs):
            vertices, edges = datastest[index][0]
            g = Graph(vertices, datastest[index][1:])
            answer = g.detect_cycle()
            result.append(answer)
    with open('./result.txt', 'w') as f:
        for item in result:
            f.write("%d" % item)
            f.write(" ")

if '__main()__':
    main()