##############################################################################################
#
#    File name :       program670.py
#    Description :     Used to accept numbers from user and display it in reverse and forward order
#    Author :          Sneha Mohane
#    Date :            03/08/2025
#
####################################################################################################

# Input : 4
#output : 4  3  2  1 2 3 4

def Display(
                iNo
           ):
        for i in range(iNo, 0, -1):
            print(i,end="\t")

        for i in range(2, iNo+1, 1):
            print(i,end="\t")

        print()    

def main():
    print("Enter string : ")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main()     