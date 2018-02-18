#! python3
#collatz Sequence
info=   """
Hello there :)
You are about to begin a collatz sequence
It is a sequence where you will always end up at 1.
No matter what number you type in.
"""
print(info)
def collatz(num):
    if num%2==0:
        print(num//2)
        return num//2
    else:
        print(3*num+1)
        return 3*num+1

#Main Begginning
while True:
    print("Press CTRL+C to Exit")
    try:
        print("Enter a number: ")
        timescall=int(input())
        while timescall !=1:
            timescall=collatz(timescall)
    except ValueError:
        print("Please type an integer")

