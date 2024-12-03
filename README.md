# Maze Solver 🗺️

## 1. Introduction
Maze is one of the most well-known game, this repository will tell how to solution to win the game.

![Maze Game](https://i.pinimg.com/originals/4f/75/df/4f75df7999c8eb8405e9a5c6b6271e27.jpg)

---

## 2. Features
Here are the key features of this project:

- A Algorithm*: The program uses the A* search algorithm to find the shortest path from start (A) to goal (B).
- Heuristic-Based Search: Leverages the Manhattan distance heuristic to efficiently explore paths.
- Graphical Output: Generates a .png image that visually represents:
  - The maze structure.
  - Explored states.
- The optimal solution path.
- Customizable Mazes: Supports user-defined maze files in plain text format.
- Error Handling: Ensures the maze has valid start and goal points and gracefully handles edge cases.

---

## 3. How to Use
### Step 1: Clone repository 
```bash
git clone https://github.com/howardVoxcan/Maze_Solver.git
cd Maze_Solver
```

### Step 2: Run code
```bash
python main.py <maze_file.txt>
```

---

## 4. Requirements
Ensure the following are installed:
- Python 3.x
- Pillow library for generating images (pip install pillow)
- Prepare a maze file in plain text format, like `maze1.txt`, `maze2.txt` or `maze3.txt`

### About `txt` file
- `A`: the starting destination
- `B`: the goal destination
- `#`: the wall
