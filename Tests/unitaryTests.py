import graph as g
import draw


def testGraphGenerator():
    number_of_vertex = 10
    saturation = 0.4
    test_graph = g.Graph(number_of_vertex, saturation)
    test_graph.generate()
    file_name = "test_graph.txt"
    test_graph.exportToFile(file_name)
    print("Test graph saved to file \"\\Instances\\{}\"".format(file_name))
    print(test_graph.graph)


def testGraphImporting():
    test_graph = g.Graph()
    file_name = "machowiakInstance.txt"
    test_graph.importFromFile(file_name)
    print("Test graph from file \"\\Instances\\{}\"".format(file_name))
    print(test_graph.graph)
    edgesDict = test_graph.exportEdgesDict()
    draw.plotGraph(edgesDict)


def plottingTest():
    test_graph = g.Graph(8)
    test_graph.generate(0.4)
    edgesDict = test_graph.exportEdgesDict()
    draw.plotGraph(edgesDict)
