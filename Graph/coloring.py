import graph as g


class ColorGraph:

    def __init__(self, graph: g.Graph):
        self.colors = [str(x+1) for x in range(graph.V)]
        self.colorOfVertex = {}
        self.colorOfVertex = [x:"" for x in range(graph.V)]
        # self.names_of_colors = {1: 'red', 2: 'green', 3: 'blue', 4: 'yellow', 5: 'brown'}
        print("All colors allow to use for this graph: ", self.colors)

    def greedyColoring(self, graph: g.Graph):
        for key in graph.graph.keys():

