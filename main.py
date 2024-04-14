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


if __name__ == "__main__":
    num_input = input('Please enter list of pinatas(enter integer numbers separeted by ,): \n')
    pinatas = [int(num) for num in num_input.split(",")]
    print(max_candies(pinatas))
