import imageio
import time
import logging
import pytest

import maze


@pytest.mark.parametrize("maze_path, num_col, num_row, runtime, repeat", [

    ("mazes/png/20-20-orthogonal-low-r.png", 20, 20, 0.0005, 10),
    ("mazes/png/20-20-orthogonal.png", 20, 20, 0.0005, 10),
    ("mazes/png/200-200-orthogonal-high-e.png", 200, 200, 0.0005, 5),
    ("mazes/png/200-200-orthogonal-low-e.png", 200, 200, 0.0005, 5),
    ("mazes/png/200-200-orthogonal-low-r.png", 200, 200, 0.0005, 5),
    ("mazes/png/200-200-orthogonal.png", 200, 200, 0.0005, 5)
])
def test_runtime(maze_path, num_col, num_row, runtime, repeat):
    tsum = 0
    my_maze = None
    raw = imageio.imread(maze_path)
    for i in range(0, repeat):
        if my_maze is not None:
            del my_maze
        t1 = time.time()
        my_maze = maze.Maze(raw, num_col, num_row)
        t2 = time.time()
        tsum += (t2 - t1)
    my_maze.draw_nodes()
    my_maze.save_maze("solutions/{}".format(maze_path))
    average = tsum / repeat
    efficiency = average / (num_col * num_row)
    logging.info("It took {0} seconds to load {1} times".format(average, repeat))
    logging.info("Average time was {0} cells per second".format(efficiency))
    assert efficiency < runtime
