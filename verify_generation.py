
import sys
from puzzle_generator import PuzzleGenerator
from sudoku_board import SudokuBoard
import time

# Increase recursion limit slightly to see if it's just on the edge, 
# but for 36x36 it implies depth > 1000 usually.
sys.setrecursionlimit(2000)

def test_generation(size):
    print(f"Testing generation for size {size}x{size}...")
    start_time = time.time()
    try:
        generator = PuzzleGenerator()
        # Reset solver metrics if needed, but we are just testing generation
        board = generator.generate(size=size, difficulty="hard")
        elapsed = time.time() - start_time
        print(f"Success! Generated {size}x{size} in {elapsed:.2f} seconds.")
        return True
    except RecursionError:
        print(f"Failed: RecursionError for {size}x{size}")
        return False
    except Exception as e:
        print(f"Failed with error: {e}")
        return False

if __name__ == "__main__":
    # Test 16x16 first
    # if not test_generation(16):
    #     print("Skipping larger sizes due to failure.")
    #     sys.exit(1)
        
    # Test 25x25
    # test_generation(25)
    
    # Test 36x36
    test_generation(36)
