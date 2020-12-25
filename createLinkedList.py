import time
import pdb

# define class LinkedList
# - representing the head of the linkedlist
class LinkedList:
    def __init__(self, head=None): # LinkedList instance object initializer
        self.head = head

    def insertNode(self, data): # data here means value we want to put at the head of the new linkedlist (assumes the data is NOT None)
        newNode = Node(data)
        if not (data is None): # helps avoid resetting the head when the data is None
            newNode.setNext(self.head) # make the previous head to be the next node to this i.e. assuming the data is NOT None
        self.head = newNode # make this the new head. if data == None, then this behaves as if you just reinitialized the LinkedList

    def getNode(self, data=None): # data here means value of the node we want, returns None [when the only node is None]
        currentNode = self.head
        while not (currentNode is None):
            if currentNode.getData() == data:  # works even when 'data == None' AND 'currentNode.getData()' becomes None after calling `currentNode = currentNode.getNext()'
                return currentNode
            else: 
                currentNode = currentNode.getNext()
        return None # when no data is found e.g. at the tail or empty LinkedList

    def countNodes(self, data): # counts nodes with specific data in them that is not None
        i = 0 # counter for number of nodes
        currentNode = self.head # this would not be None for a populated LinkedList.
        while not (currentNode is None):
            if currentNode.getData() == data: # only increments for cases when the node value matches the specific data we are trying to count (the occurrence)
                i += 1
            currentNode = currentNode.getNext() # progress to the next node until the tail tied to None as being the next node
        return i
    
    def countAllNodes(self):
        i = 0 # counter for number of nodes
        currentNode = self.head  # this would not be None for a populated LinkedList. But would be None for a shell LinkedList (i.e. not yet populated)
        while not (currentNode is None): # loop is true for populated data LinkedList BUT skipped for empty LinkedList
            i += 1
            currentNode = currentNode.getNext() # progress to the next node until the tail which == None, becomes the next node
        return i

    def deleteNode(self, data): # deletes all nodes that has data as their value:
        currentNode = self.head
        validatedNode = None
        validationFlag = False
        while  not (currentNode is None) and (validationFlag is False):
            if currentNode.getData() == data:
                validationFlag = True
            else: 
                validatedNode = currentNode
                currentNode = currentNode.getNext()
        
        if (currentNode is None): # handles when you get to end of linkedlist or when list is empty
            raise ValueError("data not found in the LinkedList")

        if (validatedNode is None):
            self.head = currentNode.getNext()
        else:
            validatedNode.setNext(currentNode.getNext())
        return currentNode

    def listLength(self): # calculates the length of the linkedlist i.e. without comparing any sort of data
        currentNode = self.head
        i = 0 # counter to store interations of available nodes
        while not (currentNode is None):
            i += 1
            currentNode = currentNode.getNext()
        return i

    def printList(self):
        currentNode = self.head
        outputString = ""
        while not (currentNode is None): # iterates through all the notes and prints the data they contain
            outputString += str(currentNode.getData()) + " "
            currentNode = currentNode.getNext()
        if outputString == "": # when it is the same as original initialization
            return "... " # returns this to capture when there is nothing to return
        else:
            return outputString # this returns the stored concatenated value

# define class Node
# - representing the nodes of the linkedlist
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setNext(self, newNext):
        self.next = newNext


# define CreateLinkedList()
#   - takes in a a list with elements being integer values
def createLinkedList(data=None): 
    linkedList = LinkedList() # create shell of linkedlist
    # next line populates the linkedlist in reverse order i.e. least significant number is placed just after the head
    # because of FIFO meaning the last in is the one closer to the head i.e. the least significant bit (or the last element of the original list in this case)
    # so there is no need to `integerList.reverse()`
    if isinstance(data, list): # checks if data is a list of integers
        for i in data:  
            linkedList.insertNode(i)
        return linkedList
    else: # return the empty linkedlist, when no data is passed means data == None
        return linkedList

# getInteger()
# - used to obtain the required test data
def getIntegers():
    try:
        print("using the format 1234 ...")
        inputIntegerString = input("Enter an integer: ")
        while (inputIntegerString is None):
            print("Input cannot be empty")
            getIntegers() # recursive call
        try: # check if the input are digits 
            inputIntegers = int(inputIntegerString)
            return inputIntegers
        except ValueError:
            print("Invalid user define input as integer literal") # handling the exception by calling getIntegers() again
            getIntegers() # recursive call
        finally:
            print("User defined integers, successfully entered")
    except ValueError:
        raise Exception("Unable to initialize the user defined integers")

def parseInputIntegers(inputIntegers: int):  # inputString is of type string
    inputIntegersString = str(inputIntegers)
    listOfStrings = list(inputIntegersString)
    listOfInt = [int(s) for s in listOfStrings]  # using list comprehension
    return listOfInt  # return a list with each integer digit as element of the list


# getTestData()
def getTestData():
    # obtain 1st test integers
    print("========================    \n")
    testIntegerOne = getIntegers()
    testListOne = parseInputIntegers(testIntegerOne)
    print("\n1st test Integer: ", testIntegerOne)
    print("1st test List: ", testListOne)
    print("========================    \n")

    # obtain 2nd test integer
    print("Enter the second test integer,", end= " ")
    testIntegerTwo = getIntegers()
    testListTwo = parseInputIntegers(testIntegerTwo)
    print("\n2nd test Integer: ", testIntegerTwo)
    print("2nd test List: ", testListTwo)
    print("========================    \n")

    return testListOne, testListTwo

def main():
    testListOne, testListTwo = getTestData()

    start_time = time.time()
    firstLinkedList = createLinkedList(testListOne)
    firstLinkedListString = firstLinkedList.printList()
    firstLinkedListNumOfNodes = firstLinkedList.countAllNodes() # want to start the counting from head

    firstLinkedListHeadGetData = firstLinkedList.head.getData()
    firstLinkedListGetNode = firstLinkedList.getNode()


    secondLinkedList = createLinkedList(testListTwo)
    secondLinkedListString = secondLinkedList.printList()
    secondLinkedListNumOfNodes = secondLinkedList.countAllNodes()
    
    randomLinkedList = createLinkedList() # empty LinkedList
    randomLinkedListString = randomLinkedList.printList() # print content of empty LinkedList
    randomLinkedListNumOfNodes = randomLinkedList.countAllNodes() # print number of nodes in empty LinkedList
    randomLinkedListEmptyValue = randomLinkedList.head.getData() # prints the first returned value (as data=None due to not being supplied) 

    print("1st Linked List {} contains {} nodes, and corresponding node values: {}".format(firstLinkedList, firstLinkedListNumOfNodes, firstLinkedListString))
    print("2nd Linked List {} contains {} nodes, and corresponding node values: {}".format(secondLinkedList, secondLinkedListNumOfNodes, secondLinkedListString))
    print("random Linked List {} contains {} nodes, corresponding node values: {}, and empty value: {}".format(randomLinkedList, randomLinkedListNumOfNodes, randomLinkedListString, randomLinkedListEmptyValue))

    print("1st Linked List's head is {} and getNode() gives {}".format(firstLinkedListHeadGetData, firstLinkedListGetNode))

    print("\nTime: {} seconds".format((time.time() - start_time)))
    print("    ============    \n")

if __name__ == "__main__":
    main()
