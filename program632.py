#########################################################################################
#
#    File name :       program632.py
#    Description :     Used to accept number from user and perform summation of factors
#    Author :          Sneha Mohane
#    Date :            03/08/2025
#
#########################################################################################

def Sumfactors(
                iNo
              ):
    iSum = 0

    for i in range(1, (iNo//2)+1):
        if(iNo % i == 0):
           iSum += 1

    return iSum       

def main():
    print("Enter number :")
    iValue = int(input())

    iRet = Sumfactors(iValue)

    print(f"Summation of factors of {iValue} is : {iRet}")

if __name__ == "__main__":
    main()    