from graph import Graph as g
import random
import math
from collections import deque


class ColorGraph:

    def __init__(self, graph: g):
        self.graph = graph
        self.colors = [str(x) for x in self.graph.graph.keys()]
        self.colorOfVertex = {x: None for x in self.graph.graph.keys()}
        self.numberOfUsedColor = 0
        self.usedColors = []
        self.TABU = deque()
        self.sizeOfTABU = 7

    def colorVertex(self, notColoredVertex):
        availableColors = [color for color in self.colors]
        vertexConnectedWithNCV = [v for v in self.graph.graph[notColoredVertex]]

        for vConnect in vertexConnectedWithNCV:
            if self.colorOfVertex[vConnect] and self.colorOfVertex[vConnect] in availableColors:
                availableColors.remove(self.colorOfVertex[vConnect])

        self.colorOfVertex[notColoredVertex] = availableColors[0]

        if self.colorOfVertex[notColoredVertex] not in self.usedColors:
            self.usedColors.append(self.colorOfVertex[notColoredVertex])
            self.numberOfUsedColor += 1

    def greedyColoring(self, showSteps=False):
        notColoredVertex = [v for v in self.graph.graph.keys()]

        if showSteps: print("Colors", self.colors)

        for ncv in notColoredVertex:
            if showSteps: print("Color of vertex ", self.colorOfVertex)
            self.colorVertex(ncv)

        if showSteps: print("Color of vertex ", self.colorOfVertex)

    def greedyImproved(self, searchingTime=10):

        TAB = []
        currentV = 1
        numberToColor = self.graph.V
        while numberToColor:
            neighbours = []
            if not self.colorOfVertex[currentV]: neighbours = [[currentV, len(self.graph.graph[currentV])]]
            for connectedWithCurrentV in self.graph.graph[currentV]:
                if not self.colorOfVertex[connectedWithCurrentV]: neighbours.append([connectedWithCurrentV, len(self.graph.graph[connectedWithCurrentV])])
            if not neighbours:
                currentV = TAB.pop(0)
                continue
            neighbours = sorted(neighbours, key=lambda s: s[1], reverse=True)
            # print("Neighbours: ", neighbours)
            indexOfBest = 0
            bestV = neighbours[indexOfBest][0]
            while bestV in TAB:
                indexOfBest += 1
                bestV = neighbours[indexOfBest][0]
            TAB.append(bestV)
            # print("TAB:  ", TAB)
            # print("BestV: ", bestV)
            availableColors = [color for color in self.colors]
            vertexConnectedWithBest = [v for v in self.graph.graph[bestV]]
            # print("connected with Best: ", vertexConnectedWithBest)
            for vConnect in vertexConnectedWithBest:
                if self.colorOfVertex[vConnect] and self.colorOfVertex[vConnect] in availableColors:
                    availableColors.remove(self.colorOfVertex[vConnect])
            self.colorOfVertex[bestV] = availableColors[0]
            if self.colorOfVertex[bestV] not in self.usedColors:
                self.usedColors.append(self.colorOfVertex[bestV])
                self.numberOfUsedColor += 1
            currentV = bestV
            neighbours = []
            numberToColor -= 1

    def randomColoring(self):
        nCol = int(math.log(self.graph.V, 2)) * int(math.log(self.graph.V, 10))
        self.colors = [str(color) for color in range(0, nCol)]
        self.colorOfVertex = {v: self.colors[random.randrange(0, nCol)] for v in self.graph.graph.keys()}

    def reloadTabu(self, bannedMove):
        if len(self.TABU) < self.sizeOfTABU:
            self.TABU.append(bannedMove)
        else:
            self.TABU.remove(self.TABU[0])
            self.TABU.append(bannedMove)

    def tabuColoring(self, maxIterations=2000, singleIterations=50):

        self.randomColoring()
        currentIteration = 0
        numberOfConflicts = 0
        candidates = []
        aspirationOfSolution = {}


        while currentIteration < maxIterations:

            for vertex in self.graph.graph.keys():
                for vertexConnected in self.graph.graph[vertex]:
                    if self.colorOfVertex[vertex] == self.colorOfVertex[vertexConnected]:
                        numberOfConflicts += 1
                        if vertexConnected not in candidates:
                            candidates.append(vertexConnected)
                        if vertex not in candidates:
                            candidates.append(vertex)

            if numberOfConflicts == 0: break
            vertex = None
            newSolution = {}
            for tryImprove in range(singleIterations):
                vertex = candidates[random.randrange(0, len(candidates))]
                newColor = self.colors[random.randrange(1, len(self.colors))]
                if self.colorOfVertex[vertex] == newColor:
                    newColor = self.colors[0]

                newSolution = self.colorOfVertex.copy()
                newConflicts = 0
                for vertex in self.graph.graph.keys():
                    for vertexConnected in self.graph.graph[vertex]:
                        if self.colorOfVertex[vertex] == self.colorOfVertex[vertexConnected]:
                            newConflicts += 1

                if newConflicts < numberOfConflicts:
                    if newConflicts <= aspirationOfSolution.setdefault(numberOfConflicts, numberOfConflicts -1):
                        aspirationOfSolution[numberOfConflicts] = newConflicts - 1

                        if (vertex, newColor) in self.TABU:
                            self.TABU.remove((vertex, newColor))
                        break

                    else:
                        if (vertex, newColor) in self.TABU:
                            continue
            self.TABU.append((vertex, self.colorOfVertex[vertex]))
            if len(self.TABU) > self.sizeOfTABU:
                self.TABU.popleft()
            self.colorOfVertex = newSolution
            currentIteration += 1



