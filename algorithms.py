"""
AI Algorithms for Sudoku Solving
Implements Constraint Propagation, AC-3, and Backtracking
"""

import time
import copy
from typing import List, Tuple, Optional, Dict, Set
from collections import deque
from sudoku_board import SudokuBoard


class AlgorithmMetrics:
    """Tracks performance metrics for algorithms"""
    
    def __init__(self):
        self.runtime = 0.0
        self.nodes_visited = 0
        self.backtrack_count = 0
        self.domain_reductions = 0
        self.start_time = None
    
    def start(self):
        """Start timing"""
        self.start_time = time.time()
    
    def stop(self):
        """Stop timing and record runtime"""
        if self.start_time:
            self.runtime = time.time() - self.start_time
    
    def reset(self):
        """Reset all metrics"""
        self.runtime = 0.0
        self.nodes_visited = 0
        self.backtrack_count = 0
        self.domain_reductions = 0
        self.start_time = None


class ConstraintPropagationSolver:
    """
    Constraint Propagation Algorithm
    Progressively reduces domains through logical elimination
    """
    
    def __init__(self):
        self.metrics = AlgorithmMetrics()
        self.domains: Dict[Tuple[int, int], Set[int]] = {}
    
    def solve(self, board: SudokuBoard) -> Tuple[Optional[SudokuBoard], AlgorithmMetrics]:
        """
        Solve Sudoku using constraint propagation
        
        Returns:
            Tuple of (solved_board, metrics)
        """
        self.metrics.reset()
        self.metrics.start()
        
        # Initialize domains
        self.domains = {}
        for row in range(board.size):
            for col in range(board.size):
                if board[row, col] == 0:
                    self.domains[(row, col)] = board.get_domain(row, col)
                else:
                    self.domains[(row, col)] = {board[row, col]}
        
        # Apply constraint propagation
        changed = True
        while changed:
            changed = False
            self.metrics.nodes_visited += 1
            
            # Find cells with single value and propagate
            for (row, col), domain in list(self.domains.items()):
                if len(domain) == 1 and board[row, col] == 0:
                    value = next(iter(domain))
                    board[row, col] = value
                    changed = True
                    self.metrics.domain_reductions += 1
                    
                    # Remove value from related cells
                    self._remove_from_neighbors(board, row, col, value)
        
        self.metrics.stop()
        
        # If not solved, return current state
        if board.is_solved():
            return board, self.metrics
        else:
            return board, self.metrics
    
    def _remove_from_neighbors(self, board: SudokuBoard, row: int, col: int, value: int):
        """Remove value from domains of related cells"""
        # Remove from row
        for c in range(board.size):
            if c != col and (row, c) in self.domains:
                if value in self.domains[(row, c)]:
                    self.domains[(row, c)].discard(value)
                    self.metrics.domain_reductions += 1
        
        # Remove from column
        for r in range(board.size):
            if r != row and (r, col) in self.domains:
                if value in self.domains[(r, col)]:
                    self.domains[(r, col)].discard(value)
                    self.metrics.domain_reductions += 1
        
        # Remove from box
        box_row = (row // board.box_size) * board.box_size
        box_col = (col // board.box_size) * board.box_size
        
        for r in range(box_row, box_row + board.box_size):
            for c in range(box_col, box_col + board.box_size):
                if (r, c) != (row, col) and (r, c) in self.domains:
                    if value in self.domains[(r, c)]:
                        self.domains[(r, c)].discard(value)
                        self.metrics.domain_reductions += 1
    
    def get_hint(self, board: SudokuBoard, row: int, col: int) -> Optional[int]:
        """Get a hint for a specific cell"""
        if board[row, col] != 0:
            return None
        
        domain = board.get_domain(row, col)
        if len(domain) > 0:
            return next(iter(domain))
        return None


class AC3Solver:
    """
    AC-3 (Arc Consistency Algorithm 3)
    Enforces binary consistency between related cells
    """
    
    def __init__(self):
        self.metrics = AlgorithmMetrics()
        self.domains: Dict[Tuple[int, int], Set[int]] = {}
    
    def solve(self, board: SudokuBoard) -> Tuple[Optional[SudokuBoard], AlgorithmMetrics]:
        """
        Solve Sudoku using AC-3 algorithm
        
        Returns:
            Tuple of (solved_board, metrics)
        """
        self.metrics.reset()
        self.metrics.start()
        
        # Initialize domains
        self.domains = {}
        for row in range(board.size):
            for col in range(board.size):
                if board[row, col] == 0:
                    self.domains[(row, col)] = board.get_domain(row, col)
                else:
                    self.domains[(row, col)] = {board[row, col]}
        
        # Build constraint graph (arcs)
        arcs = deque()
        for row in range(board.size):
            for col in range(board.size):
                # Add arcs for row constraints
                for c in range(board.size):
                    if c != col:
                        arcs.append(((row, col), (row, c)))
                
                # Add arcs for column constraints
                for r in range(board.size):
                    if r != row:
                        arcs.append(((row, col), (r, col)))
                
                # Add arcs for box constraints
                box_row = (row // board.box_size) * board.box_size
                box_col = (col // board.box_size) * board.box_size
                
                for r in range(box_row, box_row + board.box_size):
                    for c in range(box_col, box_col + board.box_size):
                        if (r, c) != (row, col):
                            arcs.append(((row, col), (r, c)))
        
        # Process arcs
        while arcs:
            self.metrics.nodes_visited += 1
            (xi, xj) = arcs.popleft()
            
            if self._revise(xi, xj):
                if len(self.domains[xi]) == 0:
                    self.metrics.stop()
                    return None, self.metrics  # Inconsistent
                
                # Add related arcs back to queue
                row_i, col_i = xi
                for row in range(board.size):
                    for col in range(board.size):
                        if (row, col) != xi and (row, col) != xj:
                            # Check if related
                            if (row == row_i or col == col_i or
                                (row // board.box_size == row_i // board.box_size and
                                 col // board.box_size == col_i // board.box_size)):
                                arcs.append(((row, col), xi))
        
        # Assign single-value domains
        for (row, col), domain in self.domains.items():
            if len(domain) == 1 and board[row, col] == 0:
                board[row, col] = next(iter(domain))
        
        self.metrics.stop()
        
        if board.is_solved():
            return board, self.metrics
        else:
            return board, self.metrics
    
    def _revise(self, xi: Tuple[int, int], xj: Tuple[int, int]) -> bool:
        """
        Revise domain of xi based on constraint with xj
        For Sudoku: xi and xj must have different values
        
        Returns:
            True if domain was revised
        """
        revised = False
        
        # If xj has only one possible value, remove it from xi
        if len(self.domains[xj]) == 1:
            value_to_remove = next(iter(self.domains[xj]))
            if value_to_remove in self.domains[xi] and len(self.domains[xi]) > 1:
                self.domains[xi].discard(value_to_remove)
                revised = True
                self.metrics.domain_reductions += 1
        
        return revised
    
    def get_hint(self, board: SudokuBoard, row: int, col: int) -> Optional[int]:
        """Get a hint for a specific cell"""
        if board[row, col] != 0:
            return None
        
        domain = board.get_domain(row, col)
        if len(domain) > 0:
            return next(iter(domain))
        return None


class BacktrackingSolver:
    """
    Brute-force Backtracking Search
    Depth-first search with backtracking
    """
    
    def __init__(self, use_mrv: bool = True):
        """
        Initialize backtracking solver
        
        Args:
            use_mrv: Use Minimum Remaining Values heuristic
        """
        self.metrics = AlgorithmMetrics()
        self.use_mrv = use_mrv
    
    def solve(self, board: SudokuBoard) -> Tuple[Optional[SudokuBoard], AlgorithmMetrics]:
        """
        Solve Sudoku using backtracking
        
        Returns:
            Tuple of (solved_board, metrics)
        """
        self.metrics.reset()
        self.metrics.start()
        
        result = self._backtrack(board.copy())
        self.metrics.stop()
        
        return result, self.metrics
    
    def _backtrack(self, board: SudokuBoard) -> Optional[SudokuBoard]:
        """Recursive backtracking function"""
        self.metrics.nodes_visited += 1
        
        if board.is_solved():
            return board
        
        # Select next cell
        cell = self._select_unassigned_variable(board)
        if cell is None:
            return None
        
        row, col = cell
        
        # Try values in domain
        domain = board.get_domain(row, col)
        for value in domain:
            if board.is_valid_move(row, col, value):
                board[row, col] = value
                
                result = self._backtrack(board)
                if result is not None:
                    return result
                
                # Backtrack
                board[row, col] = 0
                self.metrics.backtrack_count += 1
        
        return None
    
    def _select_unassigned_variable(self, board: SudokuBoard) -> Optional[Tuple[int, int]]:
        """Select next cell to assign (MRV heuristic if enabled)"""
        empty_cells = board.get_empty_cells()
        
        if not empty_cells:
            return None
        
        if self.use_mrv:
            # Minimum Remaining Values heuristic
            best_cell = None
            min_domain_size = float('inf')
            
            for row, col in empty_cells:
                domain_size = len(board.get_domain(row, col))
                if domain_size < min_domain_size:
                    min_domain_size = domain_size
                    best_cell = (row, col)
            
            return best_cell
        else:
            # Simple: return first empty cell
            return empty_cells[0]
    
    def get_hint(self, board: SudokuBoard, row: int, col: int) -> Optional[int]:
        """Get a hint for a specific cell"""
        if board[row, col] != 0:
            return None
        
        domain = board.get_domain(row, col)
        if len(domain) > 0:
            # Try to solve and see what value works
            test_board = board.copy()
            for value in domain:
                if test_board.is_valid_move(row, col, value):
                    test_board[row, col] = value
                    result, _ = self.solve(test_board)
                    if result and result.is_solved():
                        return value
        return None

