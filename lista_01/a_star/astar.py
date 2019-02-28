from PriorityQueue import PriorityQueue

def heuristic(node, values):
    return values[node]

# A* search
def a_star(graph, start, dest):

    open = PriorityQueue()

    # uses helper function for heuristics
    h = build_heuristic_dict()

    # path is a list of tuples of the form ('node', 'cost')
    open.put([(start, 0)], 0)
    closed = set()

    while not open.is_empty():

        # shortest available path
        path = open.get()

        # open contains paths with final node unclosed
        node = path[-1][0]
        g_cost = path[-1][1]
        closed.add(node)

        # testa se o objetivo foi alcançado:
        if node == dest:
            # return only path without cost
            print(path)
            return [x for x, y in path]

        for neighbor, distance in graph[node]:
            cumulative_cost = g_cost + distance
            f_cost = cumulative_cost + heuristic(neighbor, h)
            new_path = path + [(neighbor, cumulative_cost)]

            # adiciona um novo caminho para OPEN
            if neighbor not in closed:
                open.put(new_path, f_cost)

            # atualiza o custo de um caminho em aberto
            elif neighbor in open.elements:
                open.put(new_path, f_cost)
                print(path)
    return False

# Constroi o mapa de distancias
def build_heuristic_dict():
    h = {}
    with open("./distances.txt", 'r') as file:
        for line in file:
            line = line.strip().split(",")
            node = line[0].strip()
            sld = int(line[1].strip())
            h[node] = sld
    return h