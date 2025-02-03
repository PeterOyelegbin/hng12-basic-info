import math

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    abs_n = abs(n)  # Consider absolute value for Armstrong check
    digits = [int(digit) for digit in str(abs_n)]
    power = len(digits)
    return sum(d ** power for d in digits) == abs_n

def number_properties(n: int):
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    properties.append("even" if n % 2 == 0 else "odd")
    return properties
