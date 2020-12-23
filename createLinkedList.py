import time
import pdb

# define class LinkedList
# - representing the head of the linkedlist
class LinkedList:
    def __init__(self, head=None): # LinkedList instance object initializer
        self.head = head

    def insertNode(self, data): # data here means value we want to put at the head of the new linkedlist
        newNode = Node(data)
        newNode.setNext(self.head) # make the previous head to be the next node to this
        self.head = newNode # make this the new head

    def getNode(self, data): # data here means value of the node we want
        currentNode = self.head
        while not (currentNode is None):
            if currentNode.getData() == data:
                return currentNode
            else: 
                currentNode = currentNode.getNext()
        raise ValueError("Data not found")

    def countNodes(self, data): # data represents finding how many nodes have that data as their value
        currentNode = self.head
        i = 0 # counter for number of nodes
        while not (currentNode is None):
            if currentNode.getData() == data:
                i += 1
            currentNode = currentNode.getNext() # progress to the next node until the tail tied to None as being the next node
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
        return outputString
            
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
def createLinkedList(integerList: list):
    linkedList = LinkedList() # create shell of linkedlist
    # next line populates the linkedlist in reverse order i.e. least significant number is placed just after the head
    # because of FIFO meaning the last in is the one closer to the head i.e. the least significant bit (or the last element of the original list in this case)
    # so there is no need to `integerList.reverse()`
    for i in integerList:  
        linkedList.insertNode(i)
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
    secondLinkedList = createLinkedList(testListTwo)
    secondLinkedListString = secondLinkedList.printList()

    print("1st Linked List {} contains nodes {}".format(firstLinkedList, firstLinkedListString))
    print("2nd Linked List {} contains nodes {}".format(secondLinkedList, secondLinkedListString))
    print("\nTime: {} seconds".format((time.time() - start_time)))
    print("    ============    \n")

if __name__ == "__main__":
    main()
