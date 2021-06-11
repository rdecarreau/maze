import imageio
import time
import maze

raw = imageio.imread("mazes/png/20-20-Orthogonal.png")
t1 = time.time()
my_maze = maze.Maze(raw, 20, 20)
t2 = time.time()
print("It took {0} seconds to load".format(t2 - t1))
for index, node in my_maze.maze.items():
    my_maze.raw_maze[node.location["y"] + 1:node.location["y"] + 13, node.location["x"] + 1:node.location["x"] + 13] = [240, 0, 0, 255]
imageio.imwrite("mazes/png/output.png", my_maze.raw_maze)
