#########################################################################################
#
#    File name :       program655.py
#    Description :     Used to accept string from user and count frequency of string 
#    Author :          Sneha Mohane
#    Date :            03/08/2025
#
#########################################################################################

def CountFrequency(
                    data
                  ):
    iCount = 0

    for ch in data:
        if(ch == 'a'):
            iCount += 1

    return iCount

def main():
    print("Enter string : ")
    str = input()

    iRet = CountFrequency(str)

    print(f"Frequency of a in {str} is {iRet}")

if __name__ == "__main__":
    main()