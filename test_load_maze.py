import imageio
import pytest

import maze
import node

node_0_0_20_20 = node.Node((0, 0))
node_0_0_20_20.left = None
node_0_0_20_20.right = (2, 0)
node_0_0_20_20.above = None
node_0_0_20_20.below = (0, 1)

node_9_0_20_20 = node.Node((0, 0))
node_9_0_20_20.left = None
node_9_0_20_20.right = (12, 0)
node_9_0_20_20.above = None
node_9_0_20_20.below = None

expected_cells_200_200 = [
    {"index": (1, 0), "walls": {'left': False, 'right': False, 'bottom': False, 'top': True}},
]

expected_cells_20_20 = [
    {"index": (0, 0), "walls": {'left': True, 'right': False, 'bottom': False, 'top': True}},
    {"index": (15, 12), "walls": {'left': False, 'right': True, 'bottom': True, 'top': False}},
    {"index": (0, 19), "walls": {'left': True, 'right': False, 'bottom': True, 'top': False}},
]


@pytest.mark.parametrize("maze_png, num_col, num_row, expected_cells", [
    ("mazes/png/200-200-orthogonal.png", 200, 200, expected_cells_200_200),
    ("mazes/png/20-20-orthogonal.png", 20, 20, expected_cells_20_20)
])
def test_load_square(maze_png, num_col, num_row, expected_cells):
    raw = imageio.imread(maze_png)
    my_maze = maze.Maze(raw, num_row, num_col)
    assert my_maze.wall_thickness == 2
    assert my_maze.row_height == 14
    assert my_maze.column_width == 14
    for cells in expected_cells:
        assert my_maze.maze[cells["index"]] == cells["walls"]
