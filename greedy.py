from collections import deque,defaultdict
import random


class GraphColoring:

    def __init__(self, g, colored=None, max_colors=4):
        self.g = g
        self.colored = colored if colored else set()
        self.max_colors = max_colors
        self.node_color = dict()

    def colorize(self, start_node=None, randomize=False, max_colors=4, collision_threshold=0):

        if self.g is None:
            print('Null Graph!')
            return self.node_color

        if start_node is None:
            print('Need a starting node of connected components')
            return self.node_color

        if collision_threshold == 0:
            collision_threshold = len(self.g) ** 2

        self.max_colors = max_colors

        unexplored = deque(start_node)
        color = random.randrange(1, self.max_colors) if randomize else self.max_colors
        collisions = 0

        def assign_color(_color, _node):
            self.node_color[_node] = _color

        def get_next_color(_color):
            _color -= 1
            if _color < 1:
                _color = self.max_colors
            return _color

        while unexplored:
            node = unexplored.popleft()
            if node not in self.colored:
                assign_color(color, node)
                self.colored.add(node)
                color = get_next_color(color)

            collision = False
            for adj_node in self.g[node]:
                if adj_node not in self.colored:
                    assign_color(color, adj_node)
                    self.colored.add(adj_node)
                    unexplored.append(adj_node)
                elif self.node_color[node] == self.node_color[adj_node]:
                    collision = True
                    collisions += 1
                    self.colored.remove(adj_node)
                    unexplored.append(adj_node)
            if collision:
                if collisions % collision_threshold == 0:
                    self.max_colors += 1
                color = get_next_color(color)

        print(f'\nCollisions: {collisions}')

        return self.node_color

    def validate(self):
        for node in self.g:
            for adj_node in self.g[node]:
                if self.node_color[node] == self.node_color[adj_node]:
                    print('Collision: ', {self.node_color[node]: (node, adj_node)})
                    return False
        return True

if __name__ == '__main__':
    points = dict()
    points['a']=['b','c','d']
    points['b']= ['a','c']
    points['c']= ['a','b','d','e','f']
    points['d']= ['a','c','e']
    points['e']= ['c','d','f']
    points['f']= ['c','e']
    MapColor = GraphColoring(points)

    print('Coloring points:', list(points.keys()), len(points))
    states_colored = MapColor.colorize(start_node=['a'], randomize=True, max_colors=4)

    color_groups = defaultdict(list)
    for state in points:
        if state in states_colored:
            color_groups[states_colored[state]].append(state)

    if MapColor.validate():
        print(f'\nDone using {len(color_groups)} colors: {len(states_colored)} points')
        print(color_groups)
    else:
        print('\nFailed!')
