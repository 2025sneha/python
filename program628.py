#########################################################################################
#
#    File name :       program628.py
#    Description :     Used to accept number from user and count digits
#    Author :          Sneha Mohane
#    Date :            03/08/2025
#
#########################################################################################

def CountDigitsX(
                    iNo
                ):
    iCount = 0
    iDigit = 0

    while(iNo != 0):
        iDigit = iNo % 10
        if(iDigit == 5):
            iCount += 1
            iNo = iNo // 10

    return iCount     

def main():
    print("Enter number :")
    iValue = int(input())

    iRet = CountDigitsX(iValue)

    print(f"frequency of 5 in {iValue} is {iRet}")


if __name__ == "__main__":
    main()    