from astar import a_star

def build_graph_weighted(file):
    """Builds a weighted, undirected graph"""
    graph = {}
    for line in file:
        v1, v2, w = line.split(',')
        v1, v2 = v1.strip(), v2.strip()
        w = int(w.strip())
        if v1 not in graph:
            graph[v1] = []
        if v2 not in graph:
            graph[v2] = []
        graph[v1].append((v2,w))
        graph[v2].append((v1,w))
    return graph


with open('./graph.txt', 'r') as file:
    lines = file.readlines()

start = lines[1].strip()
dest = lines[2].strip()
graph = build_graph_weighted(lines[4:])

print(graph)
print(a_star(graph, start, dest), "\n\n")