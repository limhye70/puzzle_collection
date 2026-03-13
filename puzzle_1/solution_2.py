from itertools import permutations

def solution_2():
    """Compute all ten-digit permutations that satisfy the puzzle equation.

    This version is more efficient than :func:`solution_1` because it uses
    ``itertools.permutations`` to produce each full permutation of the digits
    0–9 switching postions without duplicate checks. For every permutation
    it tests the same equality:

        (abc) + (def) == (ghij)

    Returns:
        list[list[int]]: A list of solutions, where each solution is a list of
            ten distinct digits ``[a, b, c, d, e, f, g, h, i, j]`` satisfying
            the above equation.
    """
    answer_list = []
    for perm in permutations(range(10),10):
        if (100*perm[0]+10*perm[1]+perm[2])+(100*perm[3]+10*perm[4]+perm[5])==(1000*perm[6]+100*perm[7]+10*perm[8]+perm[9]):
            answer_list.append(list(perm))
    return answer_list


if __name__=="__main__":
    import time
    
    start_time = time.perf_counter()
    answer = solution_2()
    end_time = time.perf_counter()

    print(f'Running Time: {end_time-start_time}')
    print(f'{len(answer)} possible answers are found.')