if __name__ == '__main__':
    while True:
        a = int(input("input a number: "))
        b = int(input("input a number: "))

        if (((a >= 1) and (a <= 10 ** 10)) and ((b <= 10 ** 10) and (b >= 1))):
            print("In the range:", a, b)
            print(a + b)
            print(a - b)
            print(a * b)