import graph as g
import coloring as c
import draw


def graphGenerator():
    number_of_vertex = 10
    saturation = 0.4
    test_graph = g.Graph(number_of_vertex, saturation )
    test_graph.generate()
    file_name = "test_graph.txt"
    test_graph.exportToFile(file_name)
    print("Test graph saved to file \"\\Instances\\{}\"".format(file_name))
    print(test_graph.graph)


def graphImporting():
    test_graph = g.Graph()
    file_name = "machowiakInstance.txt"
    test_graph.importFromFile(file_name)
    print("Test graph from file \"\\Instances\\{}\"".format(file_name))
    print(test_graph.graph)
    edgesDict = test_graph.exportEdgesDict()
    draw.plotGraph(edgesDict)


def plotting():
    test_graph = g.Graph(8)
    test_graph.generate(0.4)
    edgesDict = test_graph.exportEdgesDict()
    draw.plotGraph(edgesDict)


def coloring():
    test_graph = g.Graph(8)     # initialize graph with 8 vertex
    test_graph.generate()       # generate random graph
    edgesDict = test_graph.exportEdgesDict()    # export for visualisation
    draw.plotGraph(edgesDict)                   # draw graph
    coloring = c.ColorGraph(test_graph)         # initialize graph coloring object which take test_graph
    coloring.greedyColoring(showSteps=True)     # greedy coloring of taken graph
    print("Colored vertex: ", coloring.colorOfVertex)
    print("Number of colors: ", coloring.numberOfUsedColor)
