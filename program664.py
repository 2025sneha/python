#########################################################################################
#
#    File name :       program664.py
#    Description :     Used to accept string from user and replace a with _
#    Author :          Sneha Mohane
#    Date :            03/08/2025
#
#########################################################################################

def Replace(
                data
           ):

    i = 0
     
    for i in range(len(data)):
        if(data[i] == 'a'):
            data[i] = '_'       # Error

def main():
    print("Enter string : ")
    str = input()

    Replace(str)

    print(f"Updated string is {str}")

if __name__ == "__main__":
    main()