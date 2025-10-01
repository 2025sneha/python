#########################################################################################
#
#    File name :       program619.py
#    Description :     Used to accept number from user print special character * using loop
#    Author :          Sneha Mohane
#    Date :            02/08/2025
#
#########################################################################################

def Display(
                No
           ):

   i = 1

   while(i <= No):
    print("*")
    i = i + 1
   

def main():

    print("Enter the number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()
