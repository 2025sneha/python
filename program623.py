#########################################################################################
#
#    File name :       program623.py
#    Description :     Used to accept number from user calculate factorial natural numbers
#    Author :          Sneha Mohane
#    Date :            02/08/2025
#
#########################################################################################

def Factorial(
                No
             ):
    iFact = 1

    for i in range(1, No+1):
        iFact = iFact * i

    return iFact    
   
def main():

    print("Enter the number : ")
    Value = int(input())

    iRet = Factorial(Value)

    print(f"Factorial is : {iRet}")

if __name__ == "__main__":
    main()
