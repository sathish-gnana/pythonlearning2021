# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#https://www.hackerrank.com/challenges/py-if-else/problem

def sayweirdorno(num):
    # Use a breakpoint in the code line below to debug your script.
    mod = num % 2
    if (mod != 0):
        print("Weird")
    elif num in range(2,5):
        print("Not Weird")
    elif num in range(6,21):
        print("Weird")
    else:
        print("Not Weird")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sayweirdorno(3)
    sayweirdorno(24)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
