import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання станцій та їх з'єднань
# Червона лінія
red_line = ['Академмістечко', 'Університет', 'Театральна', 'Хрещатик', 'Лісова']
# Синя лінія
blue_line = ['Героїв Дніпра', 'Майдан Незалежності', 'Площа Льва Толстого', 'Теремки']
# Зелена лінія
green_line = ['Сирець', 'Золоті Ворота', 'Палац Спорту', 'Видубичі']

# Додавання вершин і ребер для кожної лінії
for line in [red_line, blue_line, green_line]:
    nx.add_path(G, line)

# Пересадочні станції
interchanges = {
    ('Театральна', 'Золоті Ворота'): {'color': 'black', 'width': 2},
    ('Хрещатик', 'Майдан Незалежності'): {'color': 'black', 'width': 2},
    ('Площа Льва Толстого', 'Палац Спорту'): {'color': 'black', 'width': 2},
}

# Додавання пересадочних станцій як ребер
G.add_edges_from(interchanges.keys())

# Визначення кольорів для кожної лінії
edge_colors = []
for u, v, data in G.edges(data=True):
    if data.get('color') == 'black':
        edge_colors.append('black')
    elif u in red_line and v in red_line:
        edge_colors.append('red')
    elif u in blue_line and v in blue_line:
        edge_colors.append('blue')
    elif u in green_line and v in green_line:
        edge_colors.append('green')
    else:
        edge_colors.append('grey')  # на випадок, якщо є ребра, які не підходять під жодну категорію

# Візуалізація графа
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)  # для візуальної стабільності розміщення вершин
nx.draw(G, pos, with_labels=True, edge_color=edge_colors, width=2, node_size=2000, node_color='lightgrey')
plt.title("Схема метро Києва (спрощена)")
plt.show()


# Аналіз графа
# Кількість вершин та ребер у графі
num_vertices = G.number_of_nodes()
num_edges = G.number_of_edges()

# Ступінь кожної вершини
vertex_degrees = dict(G.degree())

num_vertices, num_edges, vertex_degrees

# Task №2
# Визначення початкової і кінцевої станцій
start_station = 'Академмістечко'
end_station = 'Теремки'

# Використання DFS для знаходження одного з можливих шляхів
dfs_path = list(nx.all_simple_paths(G, source=start_station, target=end_station))[0]

# Використання BFS для знаходження найкоротшого шляху
bfs_path = nx.shortest_path(G, source=start_station, target=end_station)

# Вивід результатів
print("DFS шлях:", dfs_path)
print("BFS шлях:", bfs_path)

# Task №3 

# Додавання ваг до ребер графу
weights = {
    ('Академмістечко', 'Університет'): 5,
    ('Університет', 'Театральна'): 3,
    ('Театральна', 'Хрещатик'): 2,
    ('Хрещатик', 'Лісова'): 7,
    ('Героїв Дніпра', 'Майдан Незалежності'): 6,
    ('Майдан Незалежності', 'Площа Льва Толстого'): 4,
    ('Площа Льва Толстого', 'Теремки'): 8,
    ('Сирець', 'Золоті Ворота'): 5,
    ('Золоті Ворота', 'Палац Спорту'): 3,
    ('Палац Спорту', 'Видубичі'): 4,
    ('Театральна', 'Золоті Ворота'): 15,
    ('Хрещатик', 'Майдан Незалежності'): 15,
    ('Площа Льва Толстого', 'Палац Спорту'): 15,
}

for (u, v), weight in weights.items():
    G[u][v]['weight'] = weight

# Використання алгоритму Дейкстри для знаходження найкоротшого шляху між усіма парами вершин
all_pairs_shortest_path = dict(nx.all_pairs_dijkstra_path(G))
all_pairs_shortest_path_length = dict(nx.all_pairs_dijkstra_path_length(G))

all_pairs_shortest_path_length
