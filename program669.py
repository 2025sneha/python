##############################################################################################
#
#    File name :       program669.py
#    Description :     Used to accept numbers from user and display it in reverse order
#    Author :          Sneha Mohane
#    Date :            03/08/2025
#
####################################################################################################

# input 4
# 4  3   2   1

def Display(
                iNo
           ):
    for i in range(iNo, 0, -1):
        print(i,end="\t")

    print()
    
def main():
    print("Enter the value : ")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main()     