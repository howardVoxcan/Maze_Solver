import sys
from maze_with_aSearch import Maze

if len(sys.argv) != 2:
    sys.exit("Usage: python main.py maze.txt")

m = Maze(sys.argv[1])
print("Maze:")
m.print()
print("Solving...")
m.solve()
print("States Explored:", m.num_explored)
print("Solution:")
m.print()
m.output_image("maze.png", show_explored=True)
