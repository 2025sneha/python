#########################################################################################
#
#    File name :       program609.py
#    Description :     Used to accept number from number and check even or odd numbers
#    Author :          Sneha Mohane
#    Date :            02/08/2025
#
#########################################################################################

def CheckEvenOdd(
                    No
                ):
    if(No % 2 == 0):
        return True
    else:
        return False    

def main():
    print("Enter number :")
    Value = int(input())

    bRet = CheckEvenOdd(Value)

    if(bRet == True):
        print(f"{Value} is even number")
    else:
        print(f"{Value} is odd number")    

if __name__ == "__main__":
    main()
