#########################################################################################
#
#    File name :       program621.py
#    Description :     Used to accept number from user print special character * using loop
#    Author :          Sneha Mohane
#    Date :            02/08/2025
#
#########################################################################################

def Display(
                No
           ):

    i = 1
   
    for i in range(1,No+1):
        print("*",end="\t")

    print("")

def main():

    print("Enter the number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()
