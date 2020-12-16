import random
from os import getcwd
from collections import defaultdict
import sys


class Graph:

    def __init__(self, number_of_vertex=0, saturation=0.3):
        self.V = number_of_vertex
        self.graph = defaultdict()
        self.saturation = saturation

        number_of_all_possible_connections = (self.V * (self.V - 1)) / 2
        self.number_of_connections = int(saturation * number_of_all_possible_connections)

    def generate(self):
        not_connected_vertices = [x for x in range(1, self.V + 1)]
        for v in range(1, self.V + 1):
            self.graph[v] = []

        first_vertex = random.choice(not_connected_vertices)
        while len(not_connected_vertices) > 1:
            second_vertex = random.choice(not_connected_vertices)
            while second_vertex == first_vertex:
                second_vertex = random.choice(not_connected_vertices)
            self.graph[first_vertex].append(second_vertex)
            self.graph[second_vertex].append(first_vertex)
            not_connected_vertices.remove(first_vertex)
            first_vertex = second_vertex

        for i in range(self.number_of_connections - (self.V - 1)):
            first_vertex = random.randint(1, self.V)
            second_vertex = random.randint(1, self.V)
            while first_vertex == second_vertex or second_vertex in self.graph[first_vertex]:
                first_vertex = random.randint(1, self.V)
                second_vertex = random.randint(1, self.V)
            self.graph[first_vertex].append(second_vertex)
            self.graph[second_vertex].append(first_vertex)

        for key in self.graph.keys():
            self.graph[key].sort()

    def exportToFile(self, file_name="testgraph.txt", file_path=getcwd()+"/Instances"):
        original_stdout = sys.stdout
        file_place = file_path + "/" + file_name
        with open(file_place, 'w') as file:
            sys.stdout = file
            print(self.V)
            for key in self.graph.keys():
                for v in self.graph[key]:
                    if v > key:
                        print(str(key) + " " + str(v))
            sys.stdout = original_stdout

    def importFromFile(self, file_name="testgraph.txt", file_path=getcwd()+"/Instances"):
        file_place = file_path + "/" + file_name
        with open(file_place, 'r') as file:
            lines = file.readlines()
        self.V = int(lines[0])
        for v in range(1, self.V + 1):
            self.graph[v] = []
        for line in lines[1:]:
            first_vertex, second_vertex = map(int, line.split(" "))
            self.graph[first_vertex].append(second_vertex)
            self.graph[second_vertex].append(first_vertex)

    def exportEdgesDict(self):
        edgeDict = {'from': [], 'to': []}
        edgesList = []
        for v1 in self.graph.keys():
            for v2 in self.graph[v1]:
                edge = [v1, v2]
                if edge not in edgesList:
                    edgesList.append(edge)
        for edge in edgesList:
            edgeDict['from'].append(edge[0])
            edgeDict['to'].append(edge[1])
        return edgeDict
