class MapColoring:
    def __init__(self, graph, num_colors):
        self.graph = graph
        self.num_colors = num_colors
        self.colors = [0] * len(graph)

    def is_safe(self, node, color):
        """Check if it's safe to color the node with the given color."""
        for neighbor in self.graph[node]:
            if self.colors[neighbor] == color:
                return False
        return True

    def solve_util(self, node):
        """Utilize backtracking to solve the map coloring problem."""
        if node == len(self.graph):
            return True

        for color in range(1, self.num_colors + 1):
            if self.is_safe(node, color):
                self.colors[node] = color
                if self.solve_util(node + 1):
                    return True
                self.colors[node] = 0

        return False

    def solve(self):
        """Solve the map coloring problem."""
        if not self.solve_util(0):
            print("Solution does not exist")
            return False
        
        print("Solution exists: Following are the assigned colors:")
        for idx, color in enumerate(self.colors):
            print(f"Region {chr(65 + idx)}: Color {color}")
        return True

# Define the map using an adjacency list
# Example map:
# A - B
# | |
# C - D - E
graph = [
    [1, 2],  # A is connected to B and C
    [0, 2, 3],  # B is connected to A, C, and D
    [0, 1, 3],  # C is connected to A, B, and D
    [1, 2, 4],  # D is connected to B, C, and E
    [3]  # E is connected to D
]
# Number of colors
num_colors = 3

# Create an instance of MapColoring and solve the problem
map_coloring = MapColoring(graph, num_colors)
map_coloring.solve()
