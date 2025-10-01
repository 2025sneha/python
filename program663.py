#########################################################################################
#
#    File name :       program663.py
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
            output = output + '_'
        else:
            output = output + ch

    return output

def main():
    print("Enter string : ")
    str = input()

    strX = Replace(str)

    print(f"Updated string is {strX}")

if __name__ == "__main__":
    main()