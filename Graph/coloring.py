from graph import Graph as g
import time


class ColorGraph:

    def __init__(self, graph: g):
        self.graph = graph
        self.colors = [str(x) for x in self.graph.graph.keys()]
        self.colorOfVertex = {}
        self.colorOfVertex = {x: None for x in self.graph.graph.keys()}
        self.numberOfUsedColor = 0
        self.usedColors = []

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
        self.colorVertex(ncv)

    def tabuSearchColoring(self, searchingTime=10):
        # start_timer = time.perf_counter()
        # while time.perf_counter() - start_timer < searchingTime:
        #
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
