import graph as g


def testGraphGenerator():
    number_of_vertex = 10
    saturation = 0.4
    test_graph = g.Graph(number_of_vertex, saturation)
    test_graph.generate()
    test_graph.exportToFile("test_graph.txt")
    print("Test graph saved to file \"test_graph.txt\"")
    print(test_graph.graph)
