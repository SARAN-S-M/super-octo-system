class FarmerWolfGoatCabbagePuzzle:
    def __init__(self):
        self.start_state = (0, 0, 0, 0)  # All are on the left side (0 = left, 1 = right)
        self.goal_state = (1, 1, 1, 1)   # Goal is to get all to the right side
        self.visited = set()  # To keep track of visited states and avoid cycles
        self.solution = []

    def is_safe(self, state):
        """Check if the current state is safe."""
        farmer, wolf, goat, cabbage = state
        # Goat cannot be left with the wolf, and cabbage cannot be left with the goat
        if goat == wolf and farmer != goat:
            return False
        if goat == cabbage and farmer != goat:
            return False
        return True

    def get_possible_moves(self, state):
        """Generate all possible moves from the current state."""
        farmer, wolf, goat, cabbage = state
        possible_moves = []
        
        # Farmer can move alone
        possible_moves.append((1 - farmer, wolf, goat, cabbage))
        
        # Farmer can move with wolf, goat, or cabbage (if they're on the same side)
        if farmer == wolf:
            possible_moves.append((1 - farmer, 1 - wolf, goat, cabbage))
        if farmer == goat:
            possible_moves.append((1 - farmer, wolf, 1 - goat, cabbage))
        if farmer == cabbage:
            possible_moves.append((1 - farmer, wolf, goat, 1 - cabbage))
        
        return possible_moves

    def dfs(self, state):
        """Depth-first search to find a solution."""
        if state in self.visited:
            return False
        
        # Mark state as visited
        self.visited.add(state)
        self.solution.append(state)
        
        # Check if goal state is reached
        if state == self.goal_state:
            return True
        
        # Explore all safe moves
        for move in self.get_possible_moves(state):
            if self.is_safe(move) and self.dfs(move):
                return True
        
        # Backtrack if no solution found
        self.solution.pop()
        return False

    def solve(self):
        """Solve the puzzle and print the solution if it exists."""
        if self.dfs(self.start_state):
            print("Solution found:")
            for state in self.solution:
                farmer, wolf, goat, cabbage = state
                print(
                    f"Farmer: {'Right' if farmer else 'Left'}, "
                    f"Wolf: {'Right' if wolf else 'Left'}, "
                    f"Goat: {'Right' if goat else 'Left'}, "
                    f"Cabbage: {'Right' if cabbage else 'Left'}"
                )
        else:
            print("No solution exists")

# Instantiate and solve the puzzle
puzzle = FarmerWolfGoatCabbagePuzzle()
puzzle.solve()
