def rec_sum(a: int, b: int) -> int:
    """ Return recurrent sum of integer A and B."""
    # make sum of 0 and B+A, increase B by A number of units while A is not equal to 0
    if a == 0:
        return b
    return rec_sum(a-1, b+1)


a = int(input("Enter an integer number A >= 0: "))
b = int(input("Enter an integer number B >= 0: "))
print(f"{a} + {b} = {rec_sum(a, b)}.")
