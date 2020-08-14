# attempt 3
from enum import Enum



class State(Enum):
    UNVISITED = 1
    PASSING = 2
    VISITED = 3


class Graph:
    def __init__(self, vertices):
        self.directions = {node + 1: [] for node in range(vertices)}
        self.vertices = vertices
        self.stack = []

    def add_edge(self, origin, destination):
        if origin in self.directions:
            if destination in self.directions[origin]:
                return
        self.directions[origin].append(destination)

    def get_graph(self):
        return self.directions

    def validate(self, visited):
        node = self.stack.pop()
        visited[node - 1] = State.PASSING
        neighbors = self.directions[node]
        for neighbor in neighbors:
            if visited[neighbor - 1] == State.UNVISITED.value:
                return neighbor
        return None

    def explore_adjacent(self, neighbors, visited):
        current = 0
        while len(self.stack) > 0:
            neighbor = neighbors[current]
            if visited[neighbor - 1] == State.VISITED.value:
                return -1
            else:
                visited[neighbor - 1] = State.VISITED.value
                self.stack.append(neighbor)
                neighbors = self.directions[neighbor]

                while len(neighbors) == 0 or visited[neighbor - 1] == State.PASSING.value:
                    visited[neighbor - 1] = State.PASSING.value
                    neighbor = self.validate(visited)
                    if len(self.stack) > 0 and neighbor != None:
                        neighbor = self.stack.pop()
                        visited[neighbor - 1] = State.PASSING.value
                    else:
                        return None

    def check_for_cycles(self):
        visited = [State.UNVISITED.value for _ in range(self.vertices)]
        node = min(self.directions)
        index = node

        for index in range(index, len(self.directions)):
            self.stack.clear()
            visited = list(map((lambda x: State.UNVISITED.value), visited))
            visited[index - 1] = State.VISITED.value
            self.stack.append(index)
            neighbors = self.directions[index]

            if len(neighbors) > 0:
                result = self.explore_adjacent(neighbors, visited)
                if result == -1:
                    return -1
            else:
                self.stack.clear()
                continue
        return 1




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

        for index in range(graphs):
            vertices, edges = datastest[index][0]
            g = Graph(vertices)

            for pair in range(1, edges + 1):
                u, v = datastest[index][pair]
                g.add_edge(u, v)
            result.append(g.check_for_cycles())
    with open('./result.txt', 'w') as f:
        for item in result:
            f.write("%d" % item)
            f.write(" ")


if '__main()__':
    main()
