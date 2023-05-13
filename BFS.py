import networkx as nx


def bfs_best_first_search(G, start, goal, h):
    visited = {start}
    queue = [(start, 0)]
    while queue:
        node, cost = queue.pop(0)
        if node == goal:
            return cost
        neighbors = sorted(list(G.neighbors(node)), key=lambda x: h[x])
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, cost + G[node][neighbor]["weight"]))
    return float("inf")


# Membuat objek Graph
G = nx.Graph()

# Menambahkan beberapa node dan edge ke dalam Graph dengan bobot
G.add_weighted_edges_from(
    [
        ("A", "B", 3),
        ("A", "C", 1),
        ("B", "D", 2),
        ("C", "D", 4),
        ("C", "E", 2),
        ("D", "E", 1),
    ]
)


# Fungsi heuristik
def h(node):
    h_map = {"A": 5, "B": 4, "C": 2, "D": 3, "E": 0}
    return h_map[node]


# Memanggil fungsi BFS dengan heuristik
shortest_path_cost = bfs_best_first_search(G, "A", "E", h)

# Menampilkan hasil
print("Shortest path cost:", shortest_path_cost)
