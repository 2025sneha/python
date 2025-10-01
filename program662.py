#########################################################################################
#
#    File name :       program662.py
#    Description :     Used to accept string from user and replace a with _
#    Author :          Sneha Mohane
#    Date :            03/08/2025
#
#########################################################################################

def Replace(
                data
           ):
    output = ""

    for ch in data:
        if(ch == 'a'):
            output.append('_')  # Error
        else:
            output.append(ch)

    return output

def main():
    print("Enter string : ")
    str = input()

    strX = Replace(str)

    print(f"Updated string is {strX}")

if __name__ == "__main__":
    main()  