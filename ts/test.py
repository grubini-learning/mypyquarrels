class Graph:
    def __init__(self, vertices):
        self.directions = {vertex: set() for vertex in range(vertices + 1)}
        self.visited = set()
        self.topological_sort = []
        self.stack = [1]

    def add_edge(self, nodea, nodeb):
        self.directions[nodea].add(nodeb)

    def get_graph(self):
        return self.directions

    def get_topological_sort(self):
        return self.topological_sort

    def get_visited(self):
        return self.visited

    def traverse(self, current):#1 |
        if len(self.stack) == 0:
            return print('we are done')
        #mark the node we have visited
        #print(f'this is the current {current}')
        self.visited.add(current)
        previous = current
        #self.visited[previous] = Status.COMPLETED.value
        #need to get the adj of the node
        #choose one that has not been selected
        nexting = self._get_next_step(previous)
        #if there isn't a adj neighbor of curr node then
        #print(f"the next city is {str(nexting)} cost {next_cost}")

        if nexting == -1:
            nexting = self.stack.pop()
            self.topological_sort.append(previous)
        else:
            #append to stack to keep track
            self.stack.append(previous)
            print(f'stack {self.stack}')
            #pop out of the stack
        #repeat the cycle with the new current
        self.traverse(nexting)

    def _get_next_step(self, current):
        #get adjacents
        adjs = self.directions[current]
        print(f'these are the adjs {adjs} of {current}')
        if current >= 1:
            for neighbour in adjs:
                if neighbour not in self.visited:
                    return neighbour
        return -1

    def validation(self):
        for key in self.directions.keys():
            #self.visited[index] == State.UNVISITED
            if len(self.directions[key]) > 0:
                if key not in self.visited:
                    self.visited.add(key)
                    self.dfs_traversal(key)

    def dfs_traversal(self, node):
        #self.visited[node - 1] = State.EXPLORING.value
        for neighbor in self.directions[node]:
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                self.dfs_traversal(neighbor)
        self.stack.append(node)


def main():
    g = Graph(6)
    g.add_edge(1,2)
    g.add_edge(3,1)
    g.add_edge(3,2)
    g.add_edge(4,3)
    g.add_edge(4,2)

    

if '__main()__':
    main()