import time


def golden(num1, num2, n=0):
    try:
        print(sum([num1, num2]))
        n += 1
        time.sleep(0.1)
        golden(num2, sum([num1, num2]), n)
    except KeyboardInterrupt:
        print(
            "\nRatio of last two numbers ("
            + str(num2)
            + ", "
            + str(sum([num1, num2]))
            + "): "
            + str(sum([num1, num2]) / num2)
        )
        i = 0
        while i <= n + 2:
            print(int(round((sum([num1, num2]) / num2) ** i)))
            i += 1


a, b = map(int, input("Type in two integers: ").split())
golden(a, b)
