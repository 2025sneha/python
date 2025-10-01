####################################################################################################
#
#    File name :       program697.py
#    Description :     Used to insert nodes into singly linear linked list
#    Author :          Sneha Mohane
#    Date :            03/08/2025
#
####################################################################################################

class Node:
    def __init__(self,No):
       self.Data = No
       self.next = None

class SinglyLL:
    def __init__(self):
        self.First = None
        self.iCount = 0

##########################################################################

    def InsertFirst(self,No):                              
        newn = Node(No)

        if(self.First == None):         #LL is empty
            self.First = newn
        else:                           #LL contains atleast 1 node
            newn.next = self.First
            self.First = newn

        self.iCount = self.iCount + 1    

#################################################################

    def Display(self):
        pass

#################################################################

    def Count(self):
        return self.iCount

##############################################################

def main():
    print("Demonstration of singly Linear List")

    sobj = SinglyLL()

    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)

    iRet = sobj.Count()

    print(f"Number of nodes in linked list are {iRet}")
    
if __name__ == "__main__":
    main()