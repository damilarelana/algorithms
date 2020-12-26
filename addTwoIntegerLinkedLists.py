import time
import createLinkedList as c
from IPython.display import display

def addIntegerNodes(nodeFirstInteger: c.Node, nodeSecondInteger: c.Node):

    newLinkedList = c.LinkedList() # default head value is None
    lastNode = c.Node() # default data argument is None (ensures there is a coupling of )
    carryValue = 0 # high multiple value carried over when adding two other numbers e.g. 9 + 8 = 17 - meaning we carry over 1 (i.e. 10 multiples while having remainder 7

    while ( (nodeFirstInteger != None) or (nodeSecondInteger != None) or (carryValue > 0) ): # these are checking the node object themselves being none and not their value
        
        # extract data from each nodes via the getData() attributes [e.g. notice that head is also a node]
        if not (nodeFirstInteger is None): # if the node object is not None, then it means it has a data within a LinkedList THEN we can extract the value via getData()
            nodeFirstIntegerValue = nodeFirstInteger.getData()
        else:
            nodeFirstIntegerValue = 0

        if not (nodeSecondInteger is None):  # if the node object is not None, then it means it has a data within a LinkedList THEN we can extract the value via getData()
            nodeSecondIntegerValue = nodeSecondInteger.getData()
        else:
            nodeSecondIntegerValue = 0

        # carryValue propagates high multiple value after addition e.g. 9 + 8 = 17 -> carries 1 (i.e. 10 multiples)
        #   - carried is towards the right in this case since we started the addition from left to right i.e. less significant bit first [from first node to last node]
        nodeValueSum =  nodeFirstIntegerValue + nodeSecondIntegerValue + carryValue
        newNode = c.Node(nodeValueSum % 10) # 'nodeValueSum' gives the remainder (of 9 + 8 = 17 i.e. 7 in this case) to be stored as the node value - assuming base 10. 
        carryValue = nodeValueSum // 10 # gives the 'multiple of 10' that is carried over to the right i.e. 

        # populate the newLinkedList shell
        if not (newLinkedList.head is None): # if newLinkedList is not empty
            lastNode.setNext(newNode) # couple the newNode as the next node to the lastNode (obtained via the head assignment)
            lastNode = newNode # assign the address of the newNode as the new lastNode
        else:  # if newLinkedList is empty i.e. spanking new THEN insert the newNode to become the head
            data = newNode.getData() # get data from newNode
            newLinkedList.insertNode(data)
            lastNode = newLinkedList.head # set the first state of the lastNode i.e. the head, after the first insertion

        # proceed to the nextNode for each nodeFirstInteger and nodeSecondInteger
        #   - first check if the node object exists or not i.e. is it None
        #   - if it is None then it would not have a nextNode so do nothing
        #   - if it is NOT Node then it would have a nextNode so call getNext()
        if not (nodeFirstInteger is None):
            nodeFirstInteger = nodeFirstInteger.getNext()

        if not (nodeSecondInteger is None):
            nodeSecondInteger = nodeSecondInteger.getNext()

    return newLinkedList # once the whole iteration is done and dusted
    
# getLinkedListData()
def getLinkedListData():

    # acquire test LinkedList data
    testListOne, testListTwo = c.getInputData()
    
    firstLinkedList = c.createLinkedList(testListOne) # create firstLinkedList
    firstLinkedListString = firstLinkedList.printList()
    firstLinkedListNumOfNodes = firstLinkedList.countAllNodes() # want to start the counting from head
    print("1st Linked List {} contains {} nodes, and corresponding node values: {}".format(firstLinkedList, firstLinkedListNumOfNodes, firstLinkedListString))
    if not (firstLinkedList.head is None): # extract first node within the firstLinkedList
        firstNodeFirstLinkedList = firstLinkedList.getNode(firstLinkedList.head.getData()) # prints the first returned value (as data=None due to not being supplied) 
    else:
        firstNodeFirstLinkedList = None

    secondLinkedList = c.createLinkedList(testListTwo) # create secondLinkedList
    secondLinkedListString = secondLinkedList.printList()
    secondLinkedListNumOfNodes = secondLinkedList.countAllNodes()
    print("2nd Linked List {} contains {} nodes, and corresponding node values: {}".format(secondLinkedList, secondLinkedListNumOfNodes, secondLinkedListString))
    if not (secondLinkedList.head is None): # extract first node within the secondLinkedList
        firstNodeSecondLinkedList = secondLinkedList.getNode(secondLinkedList.head.getData()) # prints the first returned value (as data=None due to not being supplied) 
    else:
        firstNodeSecondLinkedList = None

    return firstNodeFirstLinkedList, firstNodeSecondLinkedList

# main()

def main():

    # get LinkedList data
    firstNodeFirstLinkedList, firstNodeSecondLinkedList = getLinkedListData()

    start_time = time.time()

    # start processing
    newLinkedList = addIntegerNodes(firstNodeFirstLinkedList, firstNodeSecondLinkedList) # passing the first nodes of each linkedlist
    newLinkedListString = newLinkedList.printList()
    newLinkedListNumOfNodes = newLinkedList.countAllNodes()
    print("Adding two integer linked lists gives {} that contains {} nodes, and corresponding node values: {}".format(newLinkedList, newLinkedListNumOfNodes, newLinkedListString))
    print("\nTime: {} seconds".format((time.time() - start_time)))


if __name__ == "__main__":
    main()
