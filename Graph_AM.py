class GraphAM:

    def __init__(self, initial_num_vertices, is_directed):
        self.adj_matrix = []

        for i in range(initial_num_vertices):  # Assumption / Design Decision: 0 represents non-existing edge
            self.adj_matrix.append([0] * initial_num_vertices)

        self.is_directed = is_directed

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.adj_matrix)

    def add_vertex(self):
        for lst in self.adj_matrix:
            lst.append(0)

        new_row = [0] * (len(self.adj_matrix) + 1)  # Assumption / Design Decision: 0 represents non-existing edge
        self.adj_matrix.append(new_row)

        return len(self.adj_matrix) - 1  # Return new vertex id

    def remove_edge(self, src, dest):
        self.add_edge(src,dest, 0)

    def get_num_vertices(self):
        return len(self.adj_matrix)

    def get_vertices_reachable_from(self, src):
        reachable_vertices = set()

        for i in range(len(self.adj_matrix)):
            if self.adj_matrix[src][i] != 0:
                reachable_vertices.add(i)

        return reachable_vertices

    def get_vertices_that_point_to(self, dest):
        vertices = set()

        for i in range(len(self.adj_matrix)):
            if self.adj_matrix[i][dest] != 0:
                vertices.add(i)

        return vertices

    def add_edge(self, src, dest, weight = 1.0):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        self.adj_matrix[src][dest] = weight

        if not self.is_directed:
            self.adj_matrix[dest][src] = weight

    def is_identical(self, graph):

        if len(self.adj_matrix) != len(graph.adj_matrix):
            return False

        for src in range(len(self.adj_matrix)):
            for dest in range(len(self.adj_matrix)):
                if self.adj_matrix[src][dest] != graph.adj_matrix[src][dest]:
                    return False

        return True

    def compute_in_degree(self, v):
        if not self.is_valid_vertex(v) or not self.is_valid_vertex(v):
            return

        in_degree_count = 0

        for i in range(len(self.adj_matrix)):
            if self.adj_matrix[i][v] != 0:
                in_degree_count += 1

        return in_degree_count
