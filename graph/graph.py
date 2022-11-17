class Graph:

    def __init__(self, graf=None):
        if graf is not None:
            pass
        else:
            graf = {}

        self.graph = graf

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex2 in self.graph and vertex2 in self.graph:  # Czy oba wierzchołki należą do grafu
            if vertex1 != vertex2:  # Można usunąć, jeżeli dopuszczamy krawędź z wierzchołka do niego samego
                # można usunąć, jeżeli dopuszczamy krawędzie wielokrotne
                if vertex2 not in self.graph[vertex1] and vertex1 not in self.graph[vertex2]:
                    self.graph[vertex1].append(vertex2)
                    self.graph[vertex2].append(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for key, values in self.graph.items():
                temp = values

                if vertex in temp:
                    temp.remove(vertex)

                self.graph[key] = temp

            self.graph.pop(vertex)

    def remove_edge(self, vertex1, vertex2):
        for key, values in self.graph.items():
            temp = values
            if key == vertex1:
                temp.remove(vertex2)
                self.graph[key] = temp

            if key == vertex2:
                temp.remove(vertex1)
                self.graph[key] = temp

    def get_neighbours(self, vertex):
        temp = []

        for neighbour in self.graph:
            if neighbour in self.graph[vertex]:
                temp.append(neighbour)

        print(temp)
        print('')

    def print_graph(self):
        print(self.graph)
        print('')

    def bfs(self, vertex):
        queue = [vertex]
        visited = [vertex]
        while queue:
            vertex = queue.pop(0)

            for ver in self.graph[vertex]:
                if ver not in visited:
                    queue.append(ver)
                    visited.append(ver)
        print(visited)
        print('')

    def dfs(self, root, visited=None):
        if visited is None:
            visited = []
        visited.append(root)
        if root in self.graph:
            for node in self.graph[root]:
                if node not in visited:
                    self.dfs(node, visited)
            return visited


######################### MAIN #########################

graph = Graph()

graph.add_vertex('i')
graph.add_vertex(1)
graph.add_vertex(7)
graph.add_vertex('2')
graph.add_vertex('Kraków')
graph.add_vertex('Wrocław')

graph.add_edge(1, 'i')
graph.add_edge('2', 'i')
graph.add_edge(1, 'Kraków')
graph.add_edge('2', 1)
graph.add_edge(7, 1)
graph.add_edge('Wrocław', 'Kraków')

graph.print_graph()  # 1. wyświetlamy gotowy graf
graph.get_neighbours(1)  # 2. wyświetlamy sąsiadów 1

graph.remove_edge('i', 1)
graph.print_graph()  # 3. wyświetlamy graf z usuniętą krawędzią
graph.remove_vertex('Kraków')
graph.print_graph() # 4. wyświetlamy graf z usuniętym wierzchołkiem

graph.bfs('2')  # 5. wyświetlamy bfs od '2'
print(graph.dfs(1))  # 6. wyświetlamy dfs od 1
