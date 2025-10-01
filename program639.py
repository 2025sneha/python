#########################################################################################
#
#    File name :       program639.py
#    Description :     Used to accept number from user and store in array and display it on screen
#    Author :          Sneha Mohane
#    Date :            03/08/2025
#
#########################################################################################

def main():
    print("Enter the number of elements : ")
    iLength = int(input())

    Arr = []

    print("Please enter the elements : ")

    for i in range(1,iLength+1):
        no = int(input())
        Arr.append(no)
    
    print(Arr)
    
if __name__ == "__main__":
    main()