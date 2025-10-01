####################################################################################################
#
#    File name :       program690.py
#    Description :     Used to demonstrate the concept of life cycle
#    Author :          Sneha Mohane
#    Date :            03/08/2025
#
####################################################################################################

class Demo:
    def __init__(self):
        print("Inside constructor")

    def __del__(self):
        print("Inside Destructor")

def main():
    print("Inside main")
    obj1 = Demo()
    obj2 = Demo()

    print("End of main")


if __name__ == "__main__":
    main()     