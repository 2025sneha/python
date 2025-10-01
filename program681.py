##############################################################################################
#
#    File name :       program681.py
#    Description :     Used to accept numbers from user and print follwing matrix using nested loops 
#    Author :          Sneha Mohane
#    Date :            03/08/2025
#
####################################################################################################

# Input Rows : 5   Col : 5 
'''
  *  *  *  *  *
  *           *
  *           *
  *           *
  *  *  *  *  *
   
'''

def Display(
                iRow, 
                iCol
           ):

    for i in range(1,iRow+1, 1):
        for j in range(1,iCol+1, 1):
            if(i == 1 or i == iRow or j == 1 or j == iCol ):
                print("*",end="\t")
            else:
                print(" ",end="\t")    
                
        print()    

   

def main():
    print("Enter number of rows : ")
    Value1 = int(input())

    print("Enter number of columns : ")
    Value2 = int(input())

    Display(Value1, Value2)

if __name__ == "__main__":
    main()     