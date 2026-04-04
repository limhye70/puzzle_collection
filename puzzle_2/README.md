## Puzzle (Quiz)

Find all solutions to the equation below using each digit (0 to 9) only once.
Leading zeros are allowed (e.g., `07 + 13 = 20`).

```
A + B = C
```

## Solutions

This folder contains four solution implementations:

- `solution_1.py` - Tests all 10-digit permutations for every possible partition.
- `solution_2.py` – Optimized version of soultion_1; only computes cases where len(A) <= len(B) and uses symmetry for the rest.
- `solution_3.py` - Further optimized by iterating only over A and C partitions; B is automatically derived.
- `solution_ai.py` - A generated solution from Claude.

All scripts contain a function that returns a dictionary where keys are valid (len(A), len(B), len(C)) partitions and values are the corresponding sequences A, B, and C.

## Running the code

From this folder you can run any solution directly:

```sh
python puzzle_2/solution_1.py
python puzzle_2/solution_2.py
python puzzle_2/solution_3.py
python puzzle_2/solution_ai.py
```

Each script prints the runtime and the count of valid solutions found.

