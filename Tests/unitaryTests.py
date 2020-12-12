import graph as g
import coloring as c
import draw
import time


def graphGenerator():
    number_of_vertex = 10
    saturation = 0.4
    test_graph = g.Graph(number_of_vertex, saturation)
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
    test_graph = g.Graph(10)  # initialize graph with 8 vertex
    test_graph.generate(0.2)  # generate random graph
    edgesDict = test_graph.exportEdgesDict()  # export for visualisation
    draw.plotGraph(edgesDict)  # draw graph
    coloring = c.ColorGraph(test_graph)  # initialize graph coloring object which take test_graph
    coloring.greedyColoring(showSteps=True)  # greedy coloring of taken graph
    print("Colored vertex: ", coloring.colorOfVertex)
    print("Number of colors: ", coloring.numberOfUsedColor)


def graphQueenGreedy():
    test_graph = g.Graph()
    file_name = "queen6.txt"
    test_graph.importFromFile(file_name)
    coloring = c.ColorGraph(test_graph)
    coloring.greedyColoring(showSteps=False)
    print(file_name, "Number of colors: ", coloring.numberOfUsedColor)


def graphGC100Greedy():
    test_graph = g.Graph()
    file_name = "gc1000_300013.txt"
    test_graph.importFromFile(file_name)
    coloring = c.ColorGraph(test_graph)
    coloring.greedyColoring(showSteps=False)
    print(file_name, "Number of colors: ", coloring.numberOfUsedColor)


def graphMilesGreedy():
    test_graph = g.Graph()
    file_name = "miles250.txt"
    test_graph.importFromFile(file_name)
    coloring = c.ColorGraph(test_graph)
    coloring.greedyColoring(showSteps=False)
    print(file_name, "Number of colors: ", coloring.numberOfUsedColor)


def graphGC500Greedy():
    test_graph = g.Graph()
    file_name = "gc500.txt"
    test_graph.importFromFile(file_name)
    coloring = c.ColorGraph(test_graph)
    coloring.greedyColoring(showSteps=False)
    print(file_name, "Number of colors: ", coloring.numberOfUsedColor)


def graphLE450Greedy():
    test_graph = g.Graph()
    file_name = "le450_5a.txt"
    test_graph.importFromFile(file_name)
    coloring = c.ColorGraph(test_graph)
    coloring.greedyColoring(showSteps=False)
    print(file_name, "Number of colors: ", coloring.numberOfUsedColor)


def greedyImproved():
    test_graph = g.Graph()
    file_name = "gc500.txt"
    test_graph.importFromFile(file_name)

    coloring = c.ColorGraph(test_graph)
    coloring.greedyImproved()
    print(file_name, "Number of colors: ", coloring.numberOfUsedColor)
    print(file_name, "Number of colors: ", coloring.colorOfVertex)


def machowiakGreedy():
    test_graph = g.Graph()
    file_name = "machowiakInstance.txt"
    test_graph.importFromFile(file_name)
    # edgesDict = test_graph.exportEdgesDict()
    # draw.plotGraph(edgesDict)
    # print("Graph: ", test_graph.graph)
    coloring = c.ColorGraph(test_graph)
    coloring.greedyColoring()
    print(file_name, "Number of colors: ", coloring.numberOfUsedColor)
    print(file_name, "Number of colors: ", coloring.colorOfVertex)


def machowiakTabu():
    test_graph = g.Graph()
    file_name = "machowiakInstance.txt"
    test_graph.importFromFile(file_name)
    # edgesDict = test_graph.exportEdgesDict()
    # draw.plotGraph(edgesDict)
    # print("Graph: ", test_graph.graph)
    coloring = c.ColorGraph(test_graph)
    coloring.tabuColoring()
    print(file_name, "Number of colors: ", coloring.numberOfUsedColor)
    print(file_name, "Number of colors: ", coloring.colorOfVertex)
# def timerTesting():
#     start = time.perf_counter()
#
#     stop = time.perf_counter()
#     print(f"Time of coloring for {n} random graph: {stop - start:0.4f} seconds")



def queenTabu():
    test_graph = g.Graph()
    file_name = "queen6.txt"
    test_graph.importFromFile(file_name)
    coloring = c.ColorGraph(test_graph)
    coloring.tabuColoring(maxIterations=100, singleIterations=20)
    coloring.countColors()
    print(file_name, "Number of colors: ", coloring.numberOfUsedColor)
    print(file_name, "colors: ", coloring.colorOfVertex)


def miles250Tabu():
    test_graph = g.Graph()
    file_name = "miles250.txt"
    test_graph.importFromFile(file_name)
    coloring = c.ColorGraph(test_graph)
    coloring.tabuColoring(maxIterations=500, singleIterations=50)
    coloring.countColors()
    print(file_name, "Number of colors: ", coloring.numberOfUsedColor)
    print(file_name, "colors: ", coloring.colorOfVertex)


def le450Tabu():
    test_graph = g.Graph()
    file_name = "le450_5a.txt"
    test_graph.importFromFile(file_name)
    coloring = c.ColorGraph(test_graph)
    coloring.tabuColoring(maxIterations=2000, singleIterations=20)
    coloring.countColors()
    print(file_name, "Number of colors: ", coloring.numberOfUsedColor)
    print(file_name, "colors: ", coloring.colorOfVertex)