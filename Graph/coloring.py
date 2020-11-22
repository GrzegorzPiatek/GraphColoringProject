from graph import Graph as g


class ColorGraph:

    def __init__(self, graph: g):
        self.graph = graph
        self.colors = [str(x + 1) for x in range(graph.V)]
        self.colorOfVertex = {}
        self.colorOfVertex = {x: None for x in graph.graph.keys()}
        self.numberOfUsedColor = 0
        self.usedColors = []

    def greedyColoring(self, showSteps=False):
        notColoredVertex = [v for v in range(1, self.graph.V + 1)]

        if showSteps: print("Colors", self.colors)

        for ncv in notColoredVertex:
            if showSteps: print("Color of vertex ", self.colorOfVertex)

            availableColors = [color for color in self.colors]
            vertexConnectedWithNCV = [v for v in self.graph.graph[ncv]]

            for vConnect in vertexConnectedWithNCV:
                if self.colorOfVertex[vConnect] and self.colorOfVertex[vConnect] in availableColors:
                    if showSteps: print("Removed color", self.colorOfVertex[vConnect])
                    availableColors.remove(self.colorOfVertex[vConnect])

            self.colorOfVertex[ncv] = availableColors[0]

            if self.colorOfVertex[ncv] not in self.usedColors:
                self.usedColors.append(self.colorOfVertex[ncv])
                self.numberOfUsedColor += 1
        if showSteps: print("Color of vertex ", self.colorOfVertex)
