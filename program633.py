#########################################################################################
#
#    File name :       program633.py
#    Description :     Used to accept number from user and check perfect number
#    Author :          Sneha Mohane
#    Date :            03/08/2025
#
#########################################################################################

def CheckPerfect(
                    iNo
                ):
    iSum = 0

    for i in range(1, (iNo//2)+1):
        if(iNo % i == 0):
           iSum += 1

    if(iSum == iNo):
        return True   
    else:
        return False
   

def main():
    print("Enter number :")
    iValue = int(input())

    bRet = CheckPerfect(iValue)

    if(bRet == True):
        print(f"{iValue} is perfect number")
    else:
         print(f"{iValue} is  not perfect number")


if __name__ == "__main__":
    main()    