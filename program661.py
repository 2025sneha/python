#########################################################################################
#
#    File name :       program661.py
#    Description :     Used to accept string from user and count small characters
#    Author :          Sneha Mohane
#    Date :            03/08/2025
#
#########################################################################################

def CountSmall(
                data
              ):
    iCount = 0

    for ch in data:
        if(ch >= 'a' and ch <= 'z'):
            iCount += 1 

    return iCount    

def main():
    print("Enter string : ")
    str = input()

    iRet = CountSmall(str)

    print(f"frequency of a in {str} is {iRet}")
 


if __name__ == "__main__":
    main()     