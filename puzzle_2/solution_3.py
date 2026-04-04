import numpy as np
import pandas as pd
from collections import defaultdict
from itertools import permutations

def partitions(n=10):
    """Generate valid partition for A + B = C
    A's length, B's length, and C's length are defined as a_len, b_len, and c_len respectively and they satisfy the following conditions.
        - a_len, b_len, c_len >0
        - a_len + b_len + c_len == n
        - |max(a_len,b_len) - c_len| <=1 (allowing for leading zeros)
    Args:
        n (int): total number of digits across A, B and C (a_len + b_len + c_len == n).
    Yields:
        tupe: (a_len,b_len,c_len)
    """
    for a_len in range(1,n-1):
        c_len = n - max(2,a_len)
        while c_len>0:
            b_len = n-(a_len+c_len)
            if (b_len>0) & (0<=abs(max(a_len,b_len)-c_len)<=1):
                yield (a_len,b_len,c_len)
            c_len-=1

def solution_3(pool=range(10), n=10):
    """Solve the equation A + B = C using digits from a pool.
    Args:
        pool (iterable): Digits to be used to solve the equation.
        n (int): Total number of digits to fill across A, B, and C
            (a_len + b_len + c_len = n )
    Returns:
        solution (dict):
            key (tuple): A valid partition (a_len, b_len, c_len)
            value (list): All valid solutions for that partition,
                            where each solution is [a_seq (tuple), b_seq (tuple), c_seq (tuple)] - digit sequences for A, B, and C respectively.
    """
    # Automatically initialises an empty list for each new partition key encountered.
    solutions = defaultdict(list)
    
    for a_len, b_len, c_len in partitions(n):
        print(f'working on {(a_len,b_len,c_len)}')
        if a_len<=b_len:
            a_place_values = 10**np.array(range(a_len-1,-1,-1))
            c_place_values = 10**np.array(range(c_len-1,-1,-1))

            # Once A and C are defined, B is automatically determined
            for perm in permutations(pool,a_len+c_len):
                a_seq = perm[:a_len]
                c_seq = perm[a_len:]
                a_val = sum(a_place_values*a_seq)
                c_val = sum(c_place_values*c_seq)

                if c_val >= a_val:
                    b_seq = tuple(int(i) for i in f'{c_val-a_val}')
                    b_seq = (0,)*(b_len-len(b_seq))+b_seq

                    if (len(b_seq)==b_len) & (sorted(a_seq+b_seq+c_seq)==sorted(pool)): # (len(b_seq)==b_len) is  a cheap check
                        solutions[(a_len,b_len,c_len)].append([a_seq,b_seq,c_seq])
                        # if a_len != b_len, swap A & B to get another valid solution without recomputing
                        if a_len != b_len:
                            solutions[(b_len,a_len,c_len)].append([b_seq,a_seq,c_seq])


    return solutions

if __name__=="__main__":
    import time

    start_time = time.perf_counter()
    answer = solution_3(pool=range(10),n=10)
    end_time = time.perf_counter()
    print(f'Runtime: {end_time-start_time} seconds')
    
    for key, value in answer.items():
        print(f'{key} has {len(value)} solutions.')