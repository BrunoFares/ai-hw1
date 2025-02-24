class PuzzleSolver:
    characters = 0
    algorithm = ""

    # Constructor
    def __init__(self, characters, algorithm):
        self.characters = characters
        self.algorithm = algorithm

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