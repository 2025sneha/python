#########################################################################################
#
#    File name :       program659.py
#    Description :     Used to accept string from user and count  non vowels from string
#    Author :          Sneha Mohane
#    Date :            03/08/2025
#
#########################################################################################

def CountNonVowels(
                    data
                  ):
    iCount = 0

    pattern = "aeiouAEIOU"
    for ch in data:
        if(ch in pattern):
            iCount += 1

    return len(data) -iCount    

def main():
    print("Enter string : ")
    str = input()

    iRet = CountNonVowels(str)

    print(f"frequency of a in {str} is {iRet}")
 


if __name__ == "__main__":
    main()     