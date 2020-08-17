from enum import Enum

class State(Enum):
    UNSELECTED = 0
    SELECTED = 1


class Graph:
    def __init__(self, vertices, edges_weights):
        self.INFINITY = 99999999999999999999
        self.vertices = vertices
        self.edge_weight_list = [None] * self.vertices
        self.costs = [None] * self.vertices
        self.selections = [State.UNSELECTED.value] * self.vertices
        self._construct_edge_list()
        self._fill_edge_list(edges_weights)
        self._set_costs()

    def _construct_edge_list(self):
        for index in range(self.vertices):
            self.edge_weight_list[index] = [[], []]
    def _fill_edge_list(self, edges_weights):
        for edge_weight in edges_weights:
            if len(edge_weight) > 0:
                edges_section = self.edge_weight_list[edge_weight[0][0] - 1][0]
                cost_section = self.edge_weight_list[edge_weight[0][0] - 1][1]
                edges_section.append(edge_weight[0][1])
                cost_section.append(edge_weight[1])
    def _set_costs(self):
        self.costs = [self.INFINITY for i in range(len(self.costs))]
        one_neigbors = self.edge_weight_list[0][0]
        neighbors_cost = self.edge_weight_list[0][1]
        for index in range(len(one_neigbors)):
            neighbor = one_neigbors[index]
            neighbor_cost = neighbors_cost[index]
            self.costs[neighbor - 1] = neighbor_cost

    def _getting_ready_to_traverse(self, stack, selected_point):
        self.costs[0] = 0
        stack.append(selected_point)
        self.selections[0] = State.SELECTED.value
        neighbors = self.edge_weight_list[0]
        current_index = neighbors[1].index(min(neighbors[1]))
        selected_neighbor = neighbors[0][current_index]
        self.selections[selected_neighbor - 1] = State.SELECTED.value
        stack.append(selected_neighbor)
        return selected_neighbor, neighbors[1][current_index]

    def _get_next_point(self, selected_point):
        neighbors_costs = [neighbor for neighbor in self.edge_weight_list[selected_point - 1]]
        neighbors = neighbors_costs[0]
        costs = neighbors_costs[1]

        while len(costs) > 0:
            cheapest_index = costs.index(min(costs))
            if self.selections[neighbors[cheapest_index] - 1] == State.SELECTED.value:
                costs.pop(cheapest_index)
                neighbors.pop(cheapest_index)

            else:
                return neighbors[cheapest_index], costs[cheapest_index]
        return -1, -1

    def traverse(self):
        stack = []
        previous_point = selected_point = 1
        previous_cost = 0
        going_back = False
        selected_point, accumulated_cost = self._getting_ready_to_traverse(stack, selected_point)
        #previous_cost = 0
        print(f'oriog stack {stack}')
        while len(stack) > 0:
            selected_point, cost_route = self._get_next_point(selected_point)
            if selected_point != -1:
                #TODO we need mark it and ask if the price is lower
                #we need to select
                if going_back:
                    stack.append(previous_point)
                    going_back = False
                self.selections[selected_point - 1] = State.SELECTED.value
                #we need to put it in stack
                stack.append(selected_point)
                #we need to check cost

                print(f'these are the costs {str(self.costs)}')
                print(f'heyhi {str(selected_point)} . -- {str(self.edge_weight_list[selected_point - 1])}')
                print('hey')
                #cost_route = self.edge_weight_list[selected_point - 1][1][selected_index]
                #TODO get the ccost from previous city
                if accumulated_cost + cost_route < self.costs[selected_point - 1]:
                    #we have to update the cost
                    previous_cost = accumulated_cost
                    self.costs[selected_point - 1] = accumulated_cost + cost_route
                    #and accumulated cost
                    accumulated_cost += cost_route
                print(f'hi {str(self.edge_weight_list[selected_point][1])} selected {str(selected_point)}')
                print(f'the stack {str(stack)}')
            else:
                #TODO backtrack
                selected_point = stack.pop()
                previous_point = selected_point
                going_back = True
                accumulated_cost = previous_cost

        return list(map(lambda cost: -1 if cost == self.INFINITY else cost, self.costs))

    def dfs_traversal(self, node):
        if self.visited[node - 1] == State.EXPLORING.value:
            return False
        self.visited[node - 1] = State.EXPLORING.value
        for neighbor in self.edge_list[node]:
            if not self.dfs_traversal(neighbor):
                return False
        self.visited[node - 1] = State.COMPLETE
        return True

def main():
    with open("test.txt", "r") as f:
            vertices, edges = map(int, f.readline().split())
            text_data = f.readlines()
            result = []
            edges_weights = []

            for line in range(len(text_data)):
                node_a, node_b, weight = map(int, text_data[line].split())
                edges_weights.append([[node_a, node_b], weight])
            g = Graph(vertices, edges_weights)
            result = g.traverse()

            print(result)

            """with open('./result.txt', 'w') as f:
                for item in result:
                    f.write("%d" % item)
                    f.write(" ")"""

if "__main__()":
    main()