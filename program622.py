#########################################################################################
#
#    File name :       program622.py
#    Description :     Used to accept number from user calculate addition natural numbers
#    Author :          Sneha Mohane
#    Date :            02/08/2025
#
#########################################################################################

def Addition(
                No
            ):
    iSum = 0

    for i in range(1, No+1):
        iSum = iSum + i

    return iSum    
   
def main():

    print("Enter the number : ")
    Value = int(input())

    iRet = Addition(Value)

    print(f"Addition is : {iRet}")

if __name__ == "__main__":
    main()
