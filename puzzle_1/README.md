## Puzzle (Quiz)

Find all assignments of the digits **0-9** to the letters below such that each digit is used exactly once and the equation holds:

```
   ABC
 + DEF
 -----
  GHJI
```

The goal is to compute all 10-digit solutions where the three-digit numbers `ABC` and `DEF` sum to the four-digit number `GHJI`.


## Solutions

This folder contains two solution implementations:

- `solution_1.py` - A brute-force search using ten loops, checking at each step whether the digit was already used.
- `solution_2.py` – A faster search using `itertools.permutations` to generate permutations by **swapping digit positions**, avoiding the repeated duplicate checks of solution 1.

Both scripts contain a function that returns a list of all valid 10‑digit permutations that satisfy the equation.

## Running the code

From this folder you can run either solution directly:

```sh
python puzzle_1/solution_1.py
python puzzle_1/solution_2.py
```

Each script prints the runtime and the count of valid solutions found.

