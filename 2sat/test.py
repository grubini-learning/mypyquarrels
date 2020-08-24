def contains_negation(scc_group):
    for index in scc_group:
        if -index in scc_group:
            return True
    return False

def search_adjs(adjacent_lists, visited, finishing_order, adjacents, city):
    visited[city] = True
    for adj in adjacent_lists[city]:
        if not visited[adj]:
            search_adjs(adjacent_lists, visited, finishing_order, adjacents, adj)
    finishing_order.append(city)
    adjacents.add(city)

def dfs(adjacent_lists, sources=None):
    if sources == None:
        sources = adjacent_lists.keys()

    visited = {index: False for index in adjacent_lists}
    finishing_order = []
    stack = []
    for source in sources:
        if not visited[source]:
            adjacents = set()
            search_adjs(adjacent_lists, visited, finishing_order, adjacents, source)
            stack.append(adjacents)
    return finishing_order, stack

def reverse_graph(adjacent_lists):
    vertices = len(adjacent_lists) // 2
    reversed_adjacent_lists = {x: [] for x in range(-vertices, vertices + 1) if x != 0}
    for from_destination in adjacent_lists:
        for to_destination in adjacent_lists[from_destination]:
            reversed_adjacent_lists[to_destination].append(from_destination)
    return reversed_adjacent_lists

def get_scc(adjacent_lists):
    finishing_order = dfs(adjacent_lists)[0]
    print(f'leave sequences {finishing_order}')
    scc = dfs(reverse_graph(adjacent_lists), finishing_order[::-1])[1]
    print(scc)
    return scc

def missing_assignments(variables, strongly_connected_component):
    assign = any(map(lambda x: variables[x] != None, strongly_connected_component))
    print(f'the variables {variables}')
    print(f'none {strongly_connected_component}')
    print(f'assigning {list(map(lambda x: variables[x] != None, strongly_connected_component))}')
    print(f'asssign {assign}')
    return assign

def find_assignment(premises, adjacent_lists):
    scc_groups = get_scc(adjacent_lists)

    if any(map(contains_negation, scc_groups)):
        return None

    permises_value_assignments = {}
    print(f'i am the ssccccccc {scc_groups}')
    for group in scc_groups:
        for element in group:
            permises_value_assignments[element] = group

    for group in scc_groups[::-1]:
        if not missing_assignments(premises, group):
            print(f'xxx {element}')
            for element in group:
                premises[-element] = True
                premises[element] = False

    number_of_premises = len(premises) // 2
    return [value if premises[value] else -value for value in range(1, number_of_premises + 1)]

def main():
    with open("2sat_test.txt", "r") as f:
        graphs = int(f.readline())
        result = []

        for graph in range(graphs):
            f.readline()
            vertices, edges = map(int, f.readline().split())

            cities = {index: None for index in range(-vertices, vertices + 1) if index != 0}
            adjacent_lists = {index: [] for index in range(-vertices, vertices + 1) if index != 0}

            for edge in range(edges):
                nodea, nodeb = map(int, f.readline().split())
                adjacent_lists[-nodea].append(nodeb)
                adjacent_lists[-nodeb].append(nodea)

            assignment = find_assignment(cities, adjacent_lists)
            s = ""
            if assignment != None:
                s = "1 "
                for element in assignment:
                    s += str(element)
                    s += " "
            else:
                s = "0"
            s.rstrip()
            result.append(s)

if '__main()__':
    main()