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

    @above.deleter
    def above(self):
        del self.neighbors[self.ABOVE]

    @property
    def below(self):
        return self._get_neighbor(self.BELOW)

    @below.setter
    def below(self, index):
        self.neighbors[self.BELOW] = index

    @below.deleter
    def below(self):
        del self.neighbors[self.BELOW]

    @property
    def left(self):
        return self._get_neighbor(self.LEFT)

    @left.setter
    def left(self, index):
        self.neighbors[self.LEFT] = index

    @left.deleter
    def left(self):
        del self.neighbors[self.LEFT]

    @property
    def right(self):
        return self._get_neighbor(self.RIGHT)

    @right.setter
    def right(self, index):
        self.neighbors[self.RIGHT] = index

    @right.deleter
    def right(self):
        del self.neighbors[self.RIGHT]

    def _get_neighbor(self, location):
        if location in self.neighbors:
            return self.neighbors[location]
        else:
            return None
