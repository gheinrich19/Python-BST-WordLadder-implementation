class Node:  # just making another node class here
    def __init__(self, numData):
        self.numData = numData
        self.leftChild = None
        self.rightChild = None
        
    def insert(self, numData):  # the insert method checks for size of value and inserts left or right accordingly
        if self.numData == numData:
            return False
        elif self.numData > numData:
            if self.leftChild:
                return self.leftChild.insert(numData)
            else:
                self.leftChild = Node(numData)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(numData)
            else:
                self.rightChild = Node(numData)
                return True
    def printPre(self):    # thsi would be the preorder traversal where it prints the currnet node first!
        if self:
            print(str(self.numData))
            if self.leftChild:
                self.leftChild.printPre()
            if self.rightChild:
                self.rightChild.printPre()
                
    def printInorder(self):  # here we have the inorder traversal going left first then printing value, then going down to the right 
        # f = open('output.txt', 'w')
        if self:
            if self.leftChild:
                self.leftChild.printInorder()
                print(str(self.numData))

                # f.write(str(self.numData))
            if self.rightChild:
                self.rightChild.printInorder()
        
                
        
class Mytree:   
    def __init__ (self): #tree class has insert and print methods. 
        self.root = None
        
        
    def insert(self, numData):
        if self.root:
            return self.root.insert(numData)
        else:
            self.root = Node(numData)
            return True
            
            
    def printPre(self):
        print("PreOrder")
        self.root.printPre()
        
    def printInorder(self):
        print('In Order')
        self.root.printInorder()
        
        
        
        
        
def main():
    # open the file with the insert value data
    with open('nums.txt', 'r') as wordlist:
        myDictionary = wordlist.read().split()
    
    f = open('output.txt', 'w')
    
    Tree = Mytree() # instantiating a tree 
    
    
    
    
    for value in myDictionary:
        Tree.insert(value)
        Tree.printInorder()
        
        #f.write(str(insertVal))
        
    f.close()
  
        # f.write(mynum)
        # print(Tree.printInorder())
        # f.write('now adding another')
    
   
    
    
    
    
if __name__=="__main__":main()