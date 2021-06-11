class Node:

    ABOVE = "above"
    BELOW = "below"
    LEFT = "left"
    RIGHT = "right"

    def __init__(self, index, location):
        """
        This Node will contain its own index in the Maze hashmap as well as all indexes of neighboring nodes.
        :param index:
        """
        self.index = index
        self.neighbors = {}  # This is a dictionary containing keys for each neighboring node
        self.location = location

    @property
    def above(self):
        return self._get_neighbor(self.ABOVE)

    @above.setter
    def above(self, index):
        self.neighbors[self.ABOVE] = index

    @property
    def below(self):
        return self._get_neighbor(self.BELOW)

    @below.setter
    def below(self, index):
        self.neighbors[self.BELOW] = index

    @property
    def left(self):
        return self._get_neighbor(self.LEFT)

    @left.setter
    def left(self, index):
        self.neighbors[self.LEFT] = index

    @property
    def right(self):
        return self._get_neighbor(self.RIGHT)

    @right.setter
    def right(self, index):
        self.neighbors[self.RIGHT] = index

    def _get_neighbor(self, location):
        if location in self.neighbors:
            return self.neighbors[location]
        else:
            return None
