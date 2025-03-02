class PuzzleSolver:
    characters = 0
    algorithm = ""
    states = {}
    answer = []

    # Constructor
    def __init__(self, characters, algorithm):
        self.characters = characters
        self.algorithm = algorithm

    # Set states
    def setStates(self):
        initialState = "NNNN"

        for i in range(16):
            state = ""
            for j in range(4):
                if (i & (1 << j)):
                    state += "F"
                else:
                    state += "N"
            self.states[state] = []

    # Eliminate illegal states
    def eliminateIllegalStates(self):
        for state in list(self.states.keys()):
            if (state[0] != state[1]) and (state[0] != state[2]):
                self.states.pop(state)
                continue
            if (state[0] != state[2]) and (state[0] != state[3]):
                self.states.pop(state)
                continue

    # Build graph
    def buildGraph(self):
        if (self.characters == 2):
            self.buildGraph2Chars()
        elif (self.characters == 3):
            self.buildGraph3Chars()
    
    # Build graph with 2 characters
    def buildGraph2Chars(self):
        for state in self.states:
            for otherState in self.states:
                if (state == otherState):
                    continue

                if (state[0] == otherState[0]):
                    continue

                if (state[1] != otherState[1]):
                    if (state[2] != otherState[2]):
                        continue
                    elif (state[3] != otherState[3]):
                        continue
                            
                if (state[2] != otherState[2]):
                    if (state[3] != otherState[3]):
                        continue
                    else:
                        self.states[state].append(otherState)
                        continue

                self.states[state].append(otherState)

    # Build graph with 3 characters
    def buildGraph3Chars(self):
        for state in self.states:
            for otherState in self.states:
                if (state == otherState):
                    continue

                if (state[0] == otherState[0]):
                    continue

                if (state[1] != otherState[1]):
                    if (state[1] != state[0]):
                        continue

                    if (state[2] != otherState[2]):
                        if (state[2] != state[0]):
                            continue

                        if (state[3] != otherState[3]):
                            continue
                        else:
                            self.states[state].append(otherState)
                            continue
                    else:
                        self.states[state].append(otherState)
                        continue
                
                if (state[2] != otherState[2]):
                    if (state[2] != state[0]):
                        continue

                    if (state[3] != otherState[3]):
                        if (state[3] != state[0]):
                            continue

                        self.states[state].append(otherState)
                        continue
                
                if (state[3] != otherState[3]):
                    if (state[3] != state[0]):
                        continue

                    self.states[state].append(otherState)
                    continue

                self.states[state].append(otherState)

    # Main Solve function
    def solve(self):
        self.setStates()
        self.eliminateIllegalStates()
        self.buildGraph()

        if (self.algorithm == "BFS"):
            self.solveBFS()
        elif (self.algorithm == "DFS"):
            self.solveDFS()
        elif (self.algorithm == "DLS"):
            self.solveDLS()
        elif (self.algorithm == "IDDFS"):
            self.solveIDDFS()

    # BFS
    def solveBFS(self):
        visited = set()
        queue = [("NNNN", ["NNNN"])]
        visited.add("NNNN")

        while queue:
            node, path = queue.pop(0)

            if node == "FFFF":
                self.answer = path
                return

            for neighbor in self.states.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        self.answer = []

    # DFS
    def solveDFS(self):
        visited = set()
        stack = [("NNNN", ["NNNN"])]

        while stack:
            node, path = stack.pop()

            if node == "FFFF":
                self.answer = path
                return

            if node not in visited:
                visited.add(node)

                for neighbor in reversed(self.states.get(node, [])):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))

    # DLS
    def solveDLS(self):
        pass

    # IDDFS
    def solveIDDFS(self):
        depth = 0

        while (True):
            result = self.depthLimitedSearch("NNNN", depth)
            depth += 1

            if (result != []):
                self.answer = result
                return

    def depthLimitedSearch(self, problem, l):
        frontier = [('NNNN', ['NNNN'], 0)]
        result = []

        while (frontier):
            node, path, depth = frontier.pop(0)

            if (node == "FFFF"):
                return path

            if (depth < l):
                for neighbor in self.states.get(node, []):
                    frontier.append((neighbor, path + [neighbor], depth + 1))

        return result

    # Print solution
    def printSolution(self):
        if self.answer == []:
            print("No solution found, use the solve() function to find a solution.")
            return
        
        print()
        for i in range(len(self.answer)):
            print(self.answer[i], end="")

            if (i != len(self.answer) - 1):
                print(" -> ", end="")
            else:
                print('\n')

puzzleSolver = PuzzleSolver(2, "DFS")
puzzleSolver.solve()
puzzleSolver.printSolution()