import imageio
import time
import maze

raw = imageio.imread("mazes/png/200-200-orthogonal-multipath-30.png")
t1 = time.time()
my_maze = maze.Maze(raw, 200, 200)
t2 = time.time()
print("It took {0} seconds to load".format(t2 - t1))
my_maze.draw_nodes()
my_maze.save_maze("mazes/png/output.png")
