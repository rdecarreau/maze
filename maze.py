import node


class Maze:

    def __init__(self, raw_data, num_columns, num_rows):
        # RGBA formats here
        self.pathway_color = [255, 255, 255, 255]
        self.wall_color = [0, 0, 0, 255]
        self.maze = dict()  # Dictionary of Nodes indexed by (Col,Row) tuple
        self.max_wall_thickness = 3
        self.wall_thickness = 0
        self.row_height = 0
        self.column_width = 0

        self.num_columns = num_columns
        self.num_rows = num_rows
        self.raw_maze = raw_data  # initial image
        self.location = {}  # X, Y Pixel Coordinates for location in raw image
        self._parse_wall_thickness()
        self._parse_nodes()

    def _parse_nodes(self):
        """
        This function will take the raw maze and parse it down to just nodes which are interesting. Row and Column
        here define the node (key) in self.maze.
        'location' is the x,y coordinates in pixels of the upper-left location in the node's image. Once this function
        is done, the raw maze can be removed from memory because the self.maze dictionary should have only interesting
        nodes in it.
        :return:
        """
        self.column_width = int((len(self.raw_maze) - ((self.num_columns + 1) * self.wall_thickness)) / self.num_columns)
        self.row_height = int((len(self.raw_maze[0]) - ((self.num_rows + 1) * self.wall_thickness)) / self.num_rows)

        curr_row, curr_column = 0, 0
        previous_left_index = None
        previous_above_indexes = [None] * self.num_columns  # Store list of previous vertical nodes
        self._update_location(curr_column, curr_row)
        while curr_row < self.num_rows:
            curr_column = 0
            self._update_location(curr_column, curr_row)
            while curr_column < self.num_columns:
                walls = self._get_walls(self.location["x"], self.location["y"])
                """
                If the current cell has no top/bottom walls it is a Node, as it will need to connect to something later. 
                """
                if (not walls["top"] or not walls["bottom"]) and not (walls["left"] and walls["right"]):
                    curr_index = (curr_column, curr_row)
                    new_node = node.Node(curr_index, self.location)
                    if previous_left_index:
                        # Connect to the node to the left
                        new_node.left = previous_left_index
                        # Inform that node that you're its neighbor (doubly-linked-list)
                        self.maze[previous_left_index].right = curr_index
                    #  If there is a wall to the right then we're the last node in this part of the row
                    if walls["right"]:
                        previous_left_index = None
                    #  Otherwise we're now the previous
                    else:
                        previous_left_index = curr_index

                    if previous_above_indexes[curr_column]:
                        # Connect to the node above
                        new_node.above = previous_above_indexes[curr_column]
                        # Inform that node that you're its neighbor (doubly-linked-list)
                        self.maze[previous_above_indexes[curr_column]].below = curr_index
                    #  If there is a wall below then we're the last node in this part of the column
                    if walls["bottom"]:
                        previous_above_indexes[curr_column] = None
                    #  Otherwise we're now the previous
                    else:
                        previous_above_indexes[curr_column] = curr_index
                    self.maze[(curr_column, curr_row)] = new_node
                curr_column += 1
                self._update_location(curr_column, curr_row)
            curr_row += 1
            self._update_location(curr_column, curr_row)

    def _get_walls(self, x, y):
        # Given a current lower-left location in the raw maze, return how many walls
        half_row_height = int(self.row_height / 2)
        half_column_width = int(self.column_width / 2)
        half_wall_thickness = int(self.wall_thickness / 2)

        left_x = x - half_wall_thickness
        left_y = y + half_row_height
        right_x = x + self.column_width + half_wall_thickness
        right_y = y + half_row_height
        bottom_x = x + half_column_width
        bottom_y = y + self.row_height + half_wall_thickness
        top_x = x + half_column_width
        top_y = y - half_wall_thickness
        return {
            "left": self._is_wall(self.raw_maze[left_y][left_x]),
            "right": self._is_wall(self.raw_maze[right_y][right_x]),
            "bottom": self._is_wall(self.raw_maze[bottom_y][bottom_x]),
            "top": self._is_wall(self.raw_maze[top_y][top_x])
        }

    def _parse_wall_thickness(self):
        # fixme this does not work if walls and borders are different
        i = 0
        while self._is_wall(self.raw_maze[i, i]):
            i += 1
            if i > self.max_wall_thickness:
                raise ValueError("Wall is too thick, or pathway not found")
        self.wall_thickness = int(i)

    def _update_location(self, curr_column, curr_row):
        self.location = {"x": int(curr_column * self.column_width) + ((curr_column + 1) * self.wall_thickness),
                         "y": int(curr_row * self.row_height) + ((curr_row + 1) * self.wall_thickness)}

    def _is_pathway(self, pixel):
        return (pixel == self.pathway_color).all()

    def _is_wall(self, pixel):
        return (pixel == self.wall_color).all()
