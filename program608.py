#########################################################################################
#
#    File name :       program608.py
#    Description :     Used to perform addition of two numbers
#    Author :          Sneha Mohane
#    Date :            02/08/2025
#
#########################################################################################

def Addition(
                No1, No2
            ):
    sum = 0
    sum = No1 + No2
    return sum


def main():
    print("Enter first number")
    Value1 = int(input())

    print("Enter second number")
    Value2 = int(input())

    Ans = 0
    Ans = Addition(Value1,Value2)

    print(f"Addition of {Value1} & {Value2} is : {Ans}")

if __name__ == "__main__":
    main()
