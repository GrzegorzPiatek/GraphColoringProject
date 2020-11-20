import graph as g


class ColorGraph:

    def __init__(self, graph: g.Graph):
        self.colors = [str(x+1) for x in range(graph.V)]
        self.colorOfVertex = {}
        self.colorOfVertex = {x+1: None for x in range(graph.V)}
        print("Color of vertex ", self.colorOfVertex)

    # def greedyColoring(self, graph: g.Graph):
    #     for key in graph.graph.keys():

