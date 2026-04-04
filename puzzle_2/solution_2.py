import numpy as np
from itertools import permutations
from collections import defaultdict

def partitions(n=10):
    """Generate valid partitions for A + B = C.
    A's length, B's length, and C's length are defined as a_len, b_len, and c_len respectively and they satisify following conditions.
        - a_len, b_len, c_len >0
        - a_len + b_len + c_len == n
        - |max(a_len,b_len) - c_len| <=1 (allowing for leading zeros)
    Args:
        n (int): Total number of digits across A, B, and C (a_len + b_len + c_len == n).
    Yields:
        tuple: (a_len,b_len,c_len)

    """
    
    for a_len in range(1,n-1):
        c_len = n-2
        while c_len>0:
            b_len = n-(a_len+c_len)
            if (b_len>0) & (0<=abs(max(a_len,b_len)-c_len)<=1):
                yield (a_len,b_len,c_len)
            c_len-=1

def solution_2(pool=range(10), n=10):
    """Solve the equation A + B = C using digits from a pool.
    Args:
        pool (iterable): Digits to be used to solve the equation.
        n (int): Total number of digits to fill across A, B, and C
            (a_len + b_len + c_len = n )
    Returns:
        solution (dict):
            key (tuple): A valid partition (a_len, b_len, c_len)
            value (list): All valid solutions for that partition,
                            where each solution is [a_seq, b_seq, c_seq] - digit sequences for A, B, and C respectively.
    """
    # Automatically initialises an empty list for each new partition key encountered
    solutions = defaultdict(list)
    
    for a_len, b_len, c_len in partitions(n):
        print(f'working on {(a_len,b_len,c_len)}')

        # Only compute when a_len <= b_len; swapping handles the rest
        if a_len <= b_len:
            a_place_values = 10**np.array(range(a_len-1,-1,-1))
            b_place_values = 10**np.array(range(b_len-1,-1,-1))
            c_place_values = 10**np.array(range(c_len-1,-1,-1))
          
            for perm in permutations(pool,n):
                a_seq = perm[:a_len]
                b_seq = perm[a_len:a_len+b_len]
                c_seq = perm[a_len+b_len:]

                if sum(a_place_values*a_seq)+sum(b_place_values*b_seq)==sum(c_place_values*c_seq):
                    solutions[(a_len,b_len,c_len)].append([a_seq,b_seq,c_seq])
                    # if a_len!=b_len, swap A and B to get another valid solution withough recomputing
                    if a_len != b_len:
                        solutions[(b_len,a_len,c_len)].append([b_seq,a_seq,c_seq])
              

    return solutions

if __name__=="__main__":
    import time

    start_time = time.perf_counter()
    answer = solution_2(pool=range(10),n=10)
    end_time = time.perf_counter()
    print(f'Runtime: {end_time-start_time} seconds')
    
    for key, value in answer.items():
        print(f'{key} has {len(value)} solutions.')