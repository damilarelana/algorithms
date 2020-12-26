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
            lastNode.setNext(newNode) # couple the newNode as the next node to the lastNode
        else:  # if newLinkedList is empty i.e. spanking new THEN insert the newNode to become the head
            data = newNode.getData() # get data from newNode
            newLinkedList.insertNode(data)
        lastNode = newNode # either-way irrespective of what happens in the if/else loop, make sure the newNode is now tagged as a the lastNode (in prep for the next iteration)

        # proceed to the nextNode for each nodeFirstInteger and nodeSecondInteger
        #   - first check if the node object exists or not i.e. is it None
        #   - if it is None then it would not have a nextNode so do nothing
        #   - if it is NOT Node then it would have a nextNode so call getNext()
        if not (nodeFirstInteger is None):
            nodeFirstInteger = nodeFirstInteger.getNext()

        if not (nodeSecondInteger is None):
            nodeSecondInteger = nodeSecondInteger.getNext()

    return newLinkedList # once the whole iteration is done and dusted
    