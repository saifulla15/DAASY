class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def is_safe(self, v, colour, c):
        for i in range(self.vertices):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    def graph_coloring_util(self, m, colour, v):
        if v == self.vertices:
            return True
        for c in range(1, m + 1):
            if self.is_safe(v, colour, c):
                colour[v] = c
                if self.graph_coloring_util(m, colour, v + 1):
                    return True
                colour[v] = 0

    def graph_coloring(self, m):
        colour = [0] * self.vertices
        if not self.graph_coloring_util(m, colour, 0):
            print("Solution does not exist")
            return False
        print("Solution exists. The coloring is:")
        for c in colour:
            print(c, end=" ")
        return True


g = Graph(4)
g.graph = [[0, 1, 1, 1],
           [1, 0, 1, 0],
           [1, 1, 0, 1],
           [1, 0, 1, 0]]
m = 3
g.graph_coloring(m)
