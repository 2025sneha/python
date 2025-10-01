#########################################################################################
#
#    File name :       program624.py
#    Description :     Used to accept number from user and display it in reverse order
#    Author :          Sneha Mohane
#    Date :            02/08/2025
#
#########################################################################################

# Input : 721
# 1  2  7

def DisplayDigits(
                    No
                 ):
    iDigit = 0

    while(No != 0):
        iDigit = No % 10
        No = No // 10
        print(iDigit)

def main():

    print("Enter the number : ")
    Value = int(input())

    DisplayDigits(Value)

  

if __name__ == "__main__":
    main()
