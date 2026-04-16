# x = 121
# num = x
# rev = 0
# while x > 0:
#     digit = x%10
#     rev = rev*10 + digit
#     x = x//10
# if rev == num:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")



# import math
# arr = [12,7,8,9,0]

# first_max = -math.inf
# second_max = -math.inf

# for curval in arr:
#     if curval > first_max:
#         second_max = first_max
#         first_max = curval 
#     elif curval > second_max:
#         second_max = curval
        

                                                             # @ MATRIX @ #

#Implementation of matrix

# rows = int(input("Enter no. of rows : "))
# columns = int(input("Enter no. of columns : "))

# matrix = []
# for i in range(rows):
#     rowArr = []
#     for j in range(columns):
#         values = int(input("Enter element"))
#         rowArr.append(values)
#     matrix.append(rowArr)

# print("Matrix is" , matrix)


#Traverser of matrix  -  Visiting all the element in the matrix


# @ ROW wise traverser:->

# for r in range(rows):
#     for c in range(columns):
#         print(matrix[r][c], end=" ")
#     print()


# # @ Column wise traverser:->

# for c in range(columns):
#     for r in range(rows):
#         print(matrix[r][c], end=" ")
#     print()


# @ Row wise sum :->
 
# for r in range(rows):
#     sum = 0
#     for c in range(columns):
#         sum = sum + matrix[r][c]
#     print("Sum of row",r,"is",sum)
# print() 


# # @ Diagonal transversal

# # Primary diagonal:->

# for r in range(rows):
#     print(matrix[r][r], end=" ")

# # Seconadry diagonal;->

# c = columns - 1
# for r in range(rows):
#     print(matrix[r][c], end=" ")
#     c = c-1

#     # Second way to do it is by using formula matrix[r][columns-1-r]

# for r in range(rows):
#     print(matrix[r][columns-1-r], end=" ")# We can use rows instead of columns as well because rows and columns are equal in square matrix                   


# # @ Sum of Primary diagonal:->

# sum = 0
# for r in range(rows): 
#     sum = sum + matrix[r][r]
# print("Sum of Primary diagonal is", sum)

# # @ Sum of Secondary diagonal:->

# sum = 0
# for r in range(rows):
#     sum = sum + matrix[r][columns-1-r]
# print("Sum of Secondary diagonal is", sum)


# @  Transpose of a matrix:->umns
# transpose = []
# for i in range(columns):
#     rowArr = []
#     for j in range (rows):
#         values = 0
#         rowArr.append(values)
#     transpose.append(rowArr)


# for i in range(rows):
#     for j in range(cols):
#         transpose[j][i] = matrix[i][j]
# print()

# print(transpose)


# @ Print UPPER Triangular Matrix :->

# for i in range(rows-1):
#     for j in range(i+1, cols):
#         print("UPPER Triangular Matrix is -- ",matrix[i][j])


# @ Print LOWER Triangular Matrix:->

# for i in range(1,rows):
#     for j in range(i):
#         print("LOWER Triangular Matrix is :-  ", matrix[i][j])


# @ Rotate of a matrix by 90 degree anticlockwise:->


# 1st way to do it is by making a new matrix using formula matrix[r][columns-1-r]:->

# ansMatrix = []
# for c in range(columns-1,-1,-1):
#     rowArr = []
#     for r in range(rows):
#         rowArr.append(matrix[r][c])
#     ansMatrix.append(rowArr)
# print(ansMatrix)


# 2nd way to do it is by using transpose of a matrix and then reversing the rows:->

# transpose = []
# for r in range(columns):
#     rowArr = []
#     for c in range(rows):
#         rowArr.append(matrix[c][r])
#     transpose.append(rowArr)
# print("Transpose of matrix is :-> ",transpose)

# One way to reverse the rows:->

# transpose.reverse()
# print("After Rotating the matrix", transpose)

# second way to reverse the rows:->

# transpose = transpose[: : -1]
# print("After Rotating the matrix", transpose)



#----------------------------------------------------------------------------------------------------------------------------
                                          #@ LINKED LIST @#
#linked list is the collection of nodes where each node contains data and Address to the next node in the list.
# It is a linear data structure that allows for efficient insertion and deletion of elements.

# Nodes - is a simple structure that contains data and a address to the next node in the list.
#It is the building block of a linked list.

#-----------------------------------------------------------------------------------------------------------------------------

# Implementation of node:
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


#------------------------------------------------------------------------------------------------------------------------------

# Operation on linked list:
# 1. Insertion:-> It is the process of adding a new node to the linked list. It can be done at the beginning, 
# end or at any position in the list.
# 2. Deletion:-> It is the process of removing a node from the linked list. It can be done at the beginning, end or at any position in the list.
# 3. Traversal:-> It is the process of visiting all the nodes in the linked list. It can be done using a loop or recursion.
# 4. Searching:-> It is the process of finding a specific node in the linked list.

#----------------------------------------------------------------------------------------------------------------------------

#@ Stack:-> It is a linear data structure that follows the Last In First Out (LIFO) principle. It allows for efficient
#           insertion and deletion of elements at the top of the stack.

# Implementation of stack using array:
# class stack:
#     def __init__(self,capacity):
#         self.top = -1
#         self.capacity = capacity
#         self.stackArray = []

#     def push(self,data):
#         if self.top == self.capacity -1:
#             print("Stack Overflow")
#             return
#         self.top = self.top + 1
#         return self.stackArray[self.top] = data

#     def pop(self):
#         if self.top == -1:
#             print("Stack Underflow")
#             return
#         self.top = self.top - 1
#         return self.stackArray[self.top + 1]
    
#     def peek(self):
#         if self.top == -1:
#             print("Stack is empty")
#             return
#         return self.stackArray[self.top]
    
#     def isEmpty(self):
#         if self.top == -1:
#             return True
#         return False
    
#     def isFull(self):
#         if self.top == self.capacity -1:
#             return True
#         return False
    
# stack1 = stack(5)
# stack1.push(1)
    

# arr = [5,3,9,2,7]
# n = len(arr)
# for i in range(n-1):
#     for j in range(0 , n-1-i):
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]
# print(arr)

                    ##@ Doubly Linked List:-> It is a linear data structure that consists of a sequence of 
                    # nodes where each node contains data and two pointers, one pointing to the next node 
                    # and the other pointing to the previous node in the list. It allows for efficient insertion 
                    # and deletion of elements at both ends of the list.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def insertAtFirstPos(self, data):
#         newNode = Node(data)
#         if self.head is None:
#             self.head = newNode
#         else:
#             newNode.next = self.head
#             self.head.prev = newNode
#         self.head = newNode

#     def traversal(self):
#         currNode = self.head
#         while currNode!= None:
#             print(currNode.data, end=" ")
#             currNode = currNode.next
#     def insertAtLast(self, data):
#         newNode = Node(data)
#         if self.head is None:
#             self.head = newNode
#         else:
#             currNode = self.head
#             while currNode.next != None:
#                 currNode = currNode.next
#             currNode.next = newNode
#             newNode.prev = currNode
# dll = DoublyLinkedList()
# dll.insertAtFirstPos("sansar")
# dll.insertAtFirstPos("sujal")
# dll.traversal()


# arr = [12,7,8,19,20,3,98]
# def selectionSort(arr):
#     n = len(arr)
#     for i in range(0, n):
#         smallInx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[smallInx]:
#                 smallInx = j
#         arr[i], arr[smallInx] = arr[smallInx], arr[i]
#     return arr
# print ("Before sorting", arr)
# print("After sorting", selectionSort(arr))

# def bubbleSorting(arr):
#     n = len(arr)
#     for i in range(0, n):
#         for j in range(0, n-1-i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# print("Before sorting", arr)
# print("After sorting", bubbleSorting(arr))

# arr = [12,7,8,19,20,3,98]
# def insertionSort(arr):
#     n = len(arr)
#     for i in range(1, n):
#         min = arr[i]
#         j = i-1
#         while j >= 0 and arr[j] > min:
#             arr[j+1] = arr[j]
#             j = j-1
#         arr[j+1] = min
#     return arr
# print("Before sorting", arr)
# print("After sorting", insertionSort(arr))    


# def mergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         L = arr[:mid]
#         R = arr[mid:]

#         mergeSort(L)
#         mergeSort(R)

#         i = j = k = 0

#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1

#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1

#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1

# ------------------------------------------------------------------------------------------

class Node:
    def __init__(self, nodeData):
        self.data = nodeData
        self.leftChildAddress = None
        self.rightChildAddress = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def buildTree(self):
        data = input("Enter the data for the node: ")
        if data == "Quit":
            return None
        node = Node(data)

        print("Enter the left child of", data)
        node.leftChildAddress = self.buildTree()

        print("Enter the right child of", data)
        node.rightChildAddress = self.buildTree()
        return node
    
bt = BinaryTree()
bt.buildTree()
