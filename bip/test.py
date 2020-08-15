from enum import Enum


class State(Enum):
    UNCOLORED = -1
    GREEN = 0
    RED = 1


class Graph:
    def __init__(self, vertices, directions):
        self.vertices = vertices
        self.edge_list = [None] * self.vertices
        self.visited = [State.UNCOLORED.value] * self.vertices
        self.q = []
        self.construct_edge_list()
        self.fill_edge_list(directions)

    def construct_edge_list(self):
        for index in range(self.vertices):
            self.edge_list[index] = []

    def fill_edge_list(self, directions):
        for edge in directions:
            if len(edge) > 0:
                vertex_one, vertex_two = edge
                self.edge_list[vertex_one - 1].append(vertex_two)
                self.edge_list[vertex_two - 1].append(vertex_one)

    def validation(self):
        for index in range(self.vertices):
            if self.visited[index] == State.UNCOLORED.value:
                color = State.UNCOLORED.value
                length = self.vertices
                if not self.bfs_traversal(length, index, color):
                    return -1
        return 1

    def bfs_traversal(self, length, node, color):
        self.q.append(node)
        self.visited[node] = State.GREEN.value

        while len(self.q) > 0:
            current = self.q.pop(0)
            for element in self.edge_list[current]:
                if self.visited[element - 1] == self.visited[current]:
                    return False
                if self.visited[element - 1] == State.UNCOLORED.value:
                    self.visited[element - 1] = 1 - self.visited[current]
                    self.q.append(element)
        return True


def main():
    with open("test.txt", "r") as my_file:
        text_data = my_file.readlines()
        graphs = int(text_data[0].strip())
        data = ""
        result = []
        for line in text_data:
            data += line.replace("\n", "|")
        data = [[pair for pair in text.split("|")]
                for text in data.split("||")]

        datastest = [[[int(nu) for nu in num.split()]
                      for num in number] for number in data[1:]]

        for index in range(0, graphs):
            """vertices, edges = datastest[index][0]
            g = Graph(vertices, datastest[index][1:])
            answer = g.validation()
            result.append(answer)"""
            # result.append(is_bipartite(datastest[index][1:]))
            vertices, edges = datastest[index][0]
            g = Graph(vertices, datastest[index][1:])
            result.append(g.validation())


    with open('./result.txt', 'w') as f:
        for item in result:
            f.write("%s" % item)
            f.write(" ")


if "__main__()":
    main()
