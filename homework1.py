class PuzzleSolver:
    characters = 0
    algorithm = ""
    states = {}

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
        if (self.characters == 2):
            self.solveBFS2()
        elif (self.characters == 3):
            self.solveBFS3()

    def solveBFSwith2Chars(self):
        pass

    def solveBFSwith3Chars(self):
        pass

    # DFS
    def solveDFS(self):
        if (self.characters == 2):
            self.solveDFSwith2Chars()
        elif (self.characters == 3):
            self.solveDFSwith3Chars()

    def solveDFSwith2Chars(self):
        pass

    def solveDFSwith3Chars(self):
        pass

    # DLS
    def solveDLS(self):
        if (self.characters == 2):
            self.solveDLSwith2Chars()
        elif (self.characters == 3):
            self.solveDLSwith3Chars()

    def solveDLSwith2Chars(self):
        pass

    def solveDLSwith3Chars(self):
        pass

    # IDDFS
    def solveIDDFS(self):
        if (self.characters == 2):
            self.solveIDDFSwith2Chars()
        elif (self.characters == 3):
            self.solveIDDFSwith3Chars()

    def solveIDDFSwith2Chars(self):
        pass

    def solveIDDFSwith3Chars(self):
        pass

    # Print solution
    def printSolution(self):
        pass

puzzleSolver = PuzzleSolver(3, "BFS")
puzzleSolver.setStates()
puzzleSolver.eliminateIllegalStates()
puzzleSolver.buildGraph()
print(puzzleSolver.states)