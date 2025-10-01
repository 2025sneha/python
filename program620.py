#########################################################################################
#
#    File name :       program620.py
#    Description :     Used to accept number from user print special character * using loop
#    Author :          Sneha Mohane
#    Date :            02/08/2025
#
#########################################################################################

def Display(No):

   i = 1

   while(i <= No):
    print("*",end="\t")
    i = i + 1
   
    print("")
def main():

    print("Enter the number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()
