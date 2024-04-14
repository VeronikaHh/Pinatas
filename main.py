def max_candies(pinatas: list[int]) -> int:
    n = len(pinatas)
    if n == 0:
        return 0
    if n == 1:
        return pinatas[0]

    drop_list = [0] * n
    drop_list[0] = pinatas[0]
    drop_list[1] = max(pinatas[0], pinatas[1])

    for i in range(2, n):
        drop_list[i] = max(drop_list[i - 1], pinatas[i - 1] * pinatas[i] + (drop_list[i - 2] if i > 1 else 0))

    return drop_list[n - 1]


if name == "__main__":
    pinatas = [3, 14, 5, 9, 2, 6, 5, 3, 5]
    print(max_candies(pinatas))