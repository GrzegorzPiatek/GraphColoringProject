from graph import Graph as g
import random
import math
import copy


class ColorGraph:

    def __init__(self, graph: g):
        self.graph = graph
        self.colors = [str(x) for x in self.graph.graph.keys()]
        self.colorOfVertex = {x: None for x in self.graph.graph.keys()}
        self.numberOfUsedColor = 0
        self.usedColors = []
        self.TABU = []
        self.sizeOfTABU = 7

    def colorVertex(self, notColoredVertex):
        availableColors = [color for color in self.colors]
        vertexConnectedWithNCV = [v for v in self.graph.graph[notColoredVertex]]

        for vConnect in vertexConnectedWithNCV:
            if self.colorOfVertex[vConnect] and self.colorOfVertex[vConnect] in availableColors:
                availableColors.remove(self.colorOfVertex[vConnect])

        self.colorOfVertex[notColoredVertex] = availableColors[0]

        if int(self.colorOfVertex[notColoredVertex]) > len(self.usedColors):
            self.usedColors.append(1)
            self.numberOfUsedColor += 1
        else:
            self.usedColors[int(self.colorOfVertex[notColoredVertex]) - 1] += 1

    def greedyColoring(self, showSteps=False):
        notColoredVertex = [v for v in self.graph.graph.keys()]

        if showSteps: print("Colors", self.colors)

        for ncv in notColoredVertex:
            if showSteps: print("Color of vertex ", self.colorOfVertex)
            self.colorVertex(ncv)
        if showSteps: print("used colors ", self.usedColors)
        if showSteps: print("Color of vertex ", self.colorOfVertex)

        self.numberOfUsedColor = 0
        self.colors = []
        for k, c in self.colorOfVertex.items():
            if c not in self.colors:
                self.colors.append(c)
                self.numberOfUsedColor += 1

    def greedyImproved(self):

        TAB = []
        currentV = 1
        numberToColor = self.graph.V
        while numberToColor:
            neighbours = []
            if not self.colorOfVertex[currentV]: neighbours = [[currentV, len(self.graph.graph[currentV])]]
            for connectedWithCurrentV in self.graph.graph[currentV]:
                if not self.colorOfVertex[connectedWithCurrentV]: neighbours.append(
                    [connectedWithCurrentV, len(self.graph.graph[connectedWithCurrentV])])
            if not neighbours:
                currentV = TAB.pop(0)
                continue
            neighbours = sorted(neighbours, key=lambda s: s[1], reverse=True)
            indexOfBest = 0
            bestV = neighbours[indexOfBest][0]
            while bestV in TAB:
                indexOfBest += 1
                bestV = neighbours[indexOfBest][0]
            TAB.append(bestV)
            availableColors = [color for color in self.colors]
            vertexConnectedWithBest = [v for v in self.graph.graph[bestV]]
            for vConnect in vertexConnectedWithBest:
                if self.colorOfVertex[vConnect] and self.colorOfVertex[vConnect] in availableColors:
                    availableColors.remove(self.colorOfVertex[vConnect])
            self.colorOfVertex[bestV] = availableColors[0]
            if int(self.colorOfVertex[bestV]) > len(self.usedColors):
                self.usedColors.append(1)
                self.numberOfUsedColor += 1
            else:
                self.usedColors[int(self.colorOfVertex[bestV]) - 1] += 1
            currentV = bestV
            numberToColor -= 1

        self.numberOfUsedColor = 0
        self.colors = []
        for k, c in self.colorOfVertex.items():
            if c not in self.colors:
                self.colors.append(c)
                self.numberOfUsedColor += 1

    def randomColoring(self):
        nCol = int(math.log(self.graph.V, 2)) * int(math.log(self.graph.V, 10))
        self.colors = [str(color) for color in range(0, nCol)]
        self.colorOfVertex = {v: self.colors[random.randrange(0, nCol)] for v in self.graph.graph.keys()}

    def tabuColoring(self, maxIterations, singleIterations, debug=False):
        self.greedyImproved()
        # self.greedyColoring()
        for maxI in range(maxIterations):

            bestColor = str(random.randint(1, len(self.usedColors)))

            if debug: print("NEW bestColor= ", bestColor)
            if debug: print("ITERACJA maxI= ", maxI)

            conflicts = set()
            candidateColor = bestColor
            for v, vCol in self.colorOfVertex.items():
                if debug: print("v, vCol", v, ", ", vCol)
                if vCol == bestColor:
                    conflicts.add(v)

            newColorOfVertex = copy.deepcopy(self.colorOfVertex)

            currentIteration = 0
            self.TABU = []
            while conflicts and currentIteration < singleIterations:

                if debug: print("newColorOfVertex= ", newColorOfVertex)
                if debug: print("conflicts= ", conflicts)

                if debug: print("bestColor= ", bestColor)
                if debug: print("self.TABU= ", self.TABU)

                vertex = conflicts.pop()
                if debug: print("vertex= ", vertex)

                vertexNeighboors = self.graph.graph[vertex]

                availableColors = [color for color in self.colors if self.usedColors[int(color) - 1] > 0]
                availableColors.remove(bestColor)
                bannedColors = set()
                bannedColors.add(bestColor)

                for neighboor in vertexNeighboors:
                    if newColorOfVertex[neighboor] in availableColors:
                        availableColors.remove(newColorOfVertex[neighboor])
                        if neighboor in self.TABU:
                            bannedColors.add(newColorOfVertex[neighboor])
                if debug: print("availableColors= ", availableColors)
                if len(availableColors) > 0:
                    candidateColor = availableColors[0]
                else:
                    neighboorColors = []
                    colorsWeights = []
                    for neighboor in vertexNeighboors:
                        if newColorOfVertex[neighboor] not in neighboorColors and newColorOfVertex[
                            neighboor] not in bannedColors:
                            neighboorColors.append(newColorOfVertex[neighboor])
                            colorsWeights.append(1)
                        elif newColorOfVertex[neighboor] not in bannedColors:
                            index = neighboorColors.index(newColorOfVertex[neighboor])
                            colorsWeights[index] += 1

                        if len(neighboorColors) > 0:
                            candidateColor = neighboorColors[colorsWeights.index(min(colorsWeights))]
                        else:
                            break
                    if debug: print("candidateColor= ", candidateColor)
                    if debug: print("vertexNeighboors= ", vertexNeighboors)

                    for neighboor in vertexNeighboors:
                        if newColorOfVertex[neighboor] == candidateColor:
                            conflicts.add(neighboor)

                newColorOfVertex[vertex] = candidateColor
                if len(self.TABU) < self.sizeOfTABU:
                    self.TABU.append(vertex)
                else:
                    self.TABU.pop(0)
                    self.TABU.append(vertex)
                if debug: print("\n newColorOfVertex= ", newColorOfVertex)

                currentIteration += 1

            if debug: print("conflicts= ", conflicts)

            if len(conflicts) == 0:
                if debug: print("# conflicts= 0,  usedColors(bestColor)", self.usedColors[int(bestColor) - 1])
                self.colorOfVertex = copy.deepcopy(newColorOfVertex)
                self.usedColors[int(bestColor) - 1] -= 1

            if debug: print("self.usedColors ", self.usedColors)
            if debug: print("int(bestColor)-1 ", int(bestColor) - 1)

            if debug: print("\n\n")

    def countColors(self):
        colors = []
        self.numberOfUsedColor = 0
        for k, c in self.colorOfVertex.items():
            if c not in colors:
                colors.append(c)
                self.numberOfUsedColor += 1
