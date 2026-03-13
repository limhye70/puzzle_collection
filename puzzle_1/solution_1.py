# solution 1
def solution_1():
    """Compute all ten-digit permutations that satisfy a specific equation.

    The function iterates through every permutation of the digits 0-9 using
    ten loops. Each loop ensures the current digit has not been used
    earlier in the sequence. When a full permutation is constructed, it tests
    whether the sum of the first three-digit number and the second three-digit
    number equals the four-digit number formed by the final four digits:

    (abc) + (def) == (ghij)

    Returns:
        list[list[int]]: A list of solutions, where each solution is a list of
            ten distinct digits ``[a, b, c, d, e, f, g, h, i, j]`` satisfying
            the above equation.
    """
    answer_list = []
    for e1 in range(10):
        for e2 in range(10):
            if e1==e2: continue
            for e3 in range(10):
                if e3 in {e1,e2}: continue
                for e4 in range(10):
                    if e4 in {e1,e2,e3}: continue
                    for e5 in range(10):
                        if e5 in {e1,e2,e3,e4}: continue
                        for e6 in range(10):
                            if e6 in {e1,e2,e3,e4,e5}: continue
                            for e7 in range(10):
                                if e7 in {e1,e2,e3,e4,e5,e6}: continue
                                for e8 in range(10):
                                    if e8 in {e1,e2,e3,e4,e5,e6,e7}: continue
                                    for e9 in range(10):
                                        if e9 in {e1,e2,e3,e4,e5,e6,e7,e8}: continue
                                        for e10 in range(10):
                                            if e10 in {e1,e2,e3,e4,e5,e6,e7,e8,e9}: continue
                                            if (100*e1+10*e2+e3) + (100*e4+10*e5+e6) == (1000*e7+100*e8+10*e9+e10):
                                                answer_list.append([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10])
                                                # if len(answer_list)%10==0: print(f'We have obtained {len(answer_list)} answers')
    return(answer_list)

if __name__=="__main__":
    import time

    start_time = time.perf_counter()
    answer = solution_1()
    end_time = time.perf_counter()

    print(f'Running Time: {end_time-start_time}')
    print(f'{len(answer)} possible answers are found.')