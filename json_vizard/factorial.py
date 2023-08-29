def factorial(x: int) -> int:
    if not isinstance(x, int):
        raise TypeError("x must be an integer.")
    if x < 0:
        raise ValueError("x must be greater than or equal to 0.")
    if x == 0:
        return 1
    return x * factorial(x - 1)
