#########################################################################################
#
#    File name :       program627.py
#    Description :     Used to accept number from user and display on reverse order 
#    Author :          Sneha Mohane
#    Date :            03/08/2025
#
#########################################################################################

def Reverse(
                iNo
           ):
    iRev = 0
    iDigit = 0

    while(iNo != 0):
        iDigit = iNo % 10
        iRev = iRev * 10 + iDigit
        iNo = iNo // 10

    return iRev     

def main():
    print("Enter number :")
    iValue = int(input())

    iRet = Reverse(iValue)

    print(f"Reverse number of {iValue} : {iRet}")


if __name__ == "__main__":
    main()    