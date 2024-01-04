def ackermann(a: int, b: int) -> int:
    if a == 0:
        return b + 1
    elif b == 0:
        return ackermann(a - 1, 1)
    else:
        return ackermann(a - 1, ackermann(a, b - 1))


if __name__ == "__main__":
    ackermann(0, 0)
