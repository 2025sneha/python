####################################################################################################
#
#    File name :       program686.py
#    Description :     Used to accept numbers from user and print follwing matrix using nested loops
#    Author :          Sneha Mohane
#    Date :            03/08/2025
#
####################################################################################################

# Input Rows : 5    
'''
    
*  *  *  *  *     0
  *  *  *  *      1
   *  *  *        2
    *  *          3
     *            4
   
'''

def Display(
                iRow
           ):

    for i in range(iRow, 0, -1):
        print(" "* (iRow-i), end="")
        print("* "*i)
               

def main():
    print("Enter number of rows : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()     