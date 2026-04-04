from itertools import permutations
 
 
def solution_ai() -> dict:
    """
    Solve the puzzle: arrange digits 0-9 exactly once into three numbers A, B, C
    such that A + B = C. Each number occupies one 'box' (can be multi-digit).
    Leading zeros are allowed.
 
    Returns:
        solution (dict):
            key (tuple): A valid partition (a_len, b_len, c_len)
            value (list): All valid solutions for that partition,
                            where each solution is [a_seq (tuple), b_seq (tuple), c_seq (tuple)]
                            - digit sequences for A, B, and C respectively.
    """
    digits = tuple(range(10))  # 0-9
    total_digits = len(digits)  # 10
    solutions = {}
 
    # Generate all valid (a_len, b_len, c_len) partitions where lengths sum to 10
    # and each length is at least 1
    partitions = [
        (a_len, b_len, c_len)
        for a_len in range(1, total_digits - 1)
        for b_len in range(1, total_digits - a_len)
        for c_len in [total_digits - a_len - b_len]
        if c_len >= 1
    ]
 
    def seq_to_int(seq: tuple) -> int:
        """Convert a digit sequence (tuple) to an integer."""
        result = 0
        for d in seq:
            result = result * 10 + d
        return result
 
    # Iterate over all permutations of 10 digits
    for perm in permutations(digits):
        for a_len, b_len, c_len in partitions:
            a_seq = perm[:a_len]
            b_seq = perm[a_len:a_len + b_len]
            c_seq = perm[a_len + b_len:]
 
            a_val = seq_to_int(a_seq)
            b_val = seq_to_int(b_seq)
            c_val = seq_to_int(c_seq)
 
            if a_val + b_val == c_val:
                key = (a_len, b_len, c_len)
                if key not in solutions:
                    solutions[key] = []
                solutions[key].append([a_seq, b_seq, c_seq])
 
    return solutions


if __name__=="__main__":
    import time

    start_time = time.perf_counter()
    answer = solution_ai()
    end_time = time.perf_counter()
    print(f'Runtime: {end_time-start_time} seconds')
    
    for key, value in answer.items():
        print(f'{key} has {len(value)} solutions.')