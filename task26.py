def rec_pow(a: float, b: int) -> float:
    """ A^B """
    if b == 0:
        return 1
    return rec_pow(a, b-1)*a


a = float(input("Enter a number A: "))
b = int(input("Enter an integer number B >= 0: "))
print(f"{a}^{b} = {rec_pow(a, b)}.")
