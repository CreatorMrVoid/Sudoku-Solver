# Intelligent Sudoku Solver and Analyzer

A Sudoku game enhanced with artificial intelligence techniques, featuring multiple solving algorithms and interactive gameplay.

## Project Overview

This project presents a Sudoku-based game enhanced with artificial intelligence techniques. The player can attempt to solve Sudoku puzzles manually or request assistance from AI solvers. The system supports multiple difficulty levels and includes algorithm performance comparison features.

## Features

### Core Functionality
- **Interactive Sudoku Gameplay**: Manual puzzle solving with real-time validation
- **Multiple Board Sizes**: Support for 3x3 mini-Sudoku and 9x9 standard Sudoku
- **Difficulty Levels**: Easy, Medium, and Hard puzzles
- **Real-time Error Highlighting**: Visual feedback for conflicting cells

### AI Algorithms
The system implements three distinct solving algorithms:

1. **Constraint Propagation**
   - Progressively reduces domains through logical elimination
   - Removes impossible values using Sudoku constraints
   - Propagates information when cells become single-valued

2. **AC-3 (Arc Consistency Algorithm 3)**
   - Enforces binary consistency between related cells
   - Represents puzzle as a CSP (Constraint Satisfaction Problem)
   - Maintains arc consistency through domain revision

3. **Brute-force Backtracking**
   - Depth-first search with backtracking
   - Optional MRV (Minimum Remaining Values) heuristic
   - Systematic trial-and-error approach

### Additional Features
- **Hint System**: Get suggestions using the selected algorithm
- **Algorithm Comparison**: Compare performance of all three algorithms
- **Performance Metrics**: Track runtime, nodes visited, backtracks, and domain reductions
- **Step-by-step Visualization**: See how algorithms solve puzzles
- **Score Tracking**: Monitor time and hints used

## Installation

### Requirements
- Python 3.7 or higher
- tkinter (usually included with Python)

### Setup
1. Clone or download this repository
2. Ensure Python 3.7+ is installed
3. No additional packages required (uses only standard library)

## Usage

### Running the Game
```bash
python sudoku_game.py
```

### Game Controls

1. **New Puzzle**: Generate a new puzzle with selected size and difficulty
2. **Get Hint**: Click on an empty cell and click "Get Hint" for a suggestion
3. **Solve**: Automatically solve the puzzle using the selected algorithm
4. **Compare Algorithms**: Run all three algorithms and compare their performance
5. **Clear**: Reset the board to the original puzzle state
6. **Check**: Verify if your current solution is correct

### Selecting Options
- **Board Size**: Choose between 3x3 (mini) and 9x9 (standard) Sudoku
- **Difficulty**: Select Easy, Medium, or Hard
- **Algorithm**: Choose which AI algorithm to use for hints and solving

## Project Structure

```
.
├── sudoku_board.py      # Sudoku board class with validation
├── algorithms.py         # Three AI solving algorithms
├── puzzle_generator.py  # Puzzle generation logic
├── sudoku_game.py       # Main game application with GUI
├── requirements.txt      # Dependencies (none required)
└── README.md           # This file
```

## Algorithm Details

### Constraint Propagation
- Initializes domains based on puzzle constraints
- Removes impossible values from related cells
- Propagates single-valued cells to neighbors
- Continues until no further reductions are possible

### AC-3 Algorithm
- Represents puzzle as a CSP with variables, domains, and constraints
- Maintains a queue of arcs (binary constraints)
- Revises domains to maintain arc consistency
- Re-adds related arcs when domains change

### Backtracking
- Selects empty cells (optionally using MRV heuristic)
- Tries values sequentially
- Checks consistency after each assignment
- Backtracks when contradictions arise

## Performance Comparison

The system tracks and compares:
- **Runtime**: Time taken to solve
- **Nodes Visited**: Number of states explored
- **Backtrack Count**: Number of backtrack operations
- **Domain Reductions**: Number of domain value removals

### Expected Observations
- **Easy puzzles**: All algorithms perform efficiently
- **Hard puzzles**: Backtracking becomes slower with many backtracks
- **AC-3 and Constraint Propagation**: Significantly reduce search space
- **Hybrid approaches**: Show best performance

## Gameplay Mechanics

### Winning Condition
A puzzle is successfully completed when:
- Every row contains digits 1-N exactly once
- Every column contains digits 1-N exactly once
- Every sub-grid contains digits 1-N exactly once
- No constraints are violated

### Difficulty Scaling
- **Level 1 (Easy)**: 50% of cells pre-filled
- **Level 2 (Medium)**: 35% of cells pre-filled
- **Level 3 (Hard)**: 25% of cells pre-filled

## Technical Details

### Classes
- `SudokuBoard`: Handles board state, validation, and domain calculation
- `ConstraintPropagationSolver`: Implements constraint propagation algorithm
- `AC3Solver`: Implements AC-3 arc consistency algorithm
- `BacktrackingSolver`: Implements backtracking search
- `PuzzleGenerator`: Generates valid Sudoku puzzles
- `SudokuGame`: Main game class with GUI

### Metrics Tracking
- `AlgorithmMetrics`: Tracks runtime, nodes visited, backtracks, and domain reductions

## Future Enhancements

Potential improvements:
- Additional difficulty levels
- More sophisticated heuristics
- Step-by-step algorithm visualization
- Puzzle import/export
- Statistics and leaderboards
- Multiplayer support

## Authors

- Berfin Duru ALKAN - 202228005
- Şahin ERŞAN - 202128002
- Özgün SOYKÖK - 202228043
- İsmail DOĞAN - 202128045

## Course

SENG 465 - Artificial Intelligence in Game Programming

## License

This project is created for educational purposes.

