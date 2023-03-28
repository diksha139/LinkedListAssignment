"""
Node Class:
    This is responsible for storing task details in the class and can be added to linked list
"""
class Node:
    #Constructor Implementation
    def __init__(self, task_id, start_time, end_time):
        self.task_id = task_id
        self.start_time = start_time
        self.end_time = end_time
        self.next = None

    def __repr__(self) -> str:
        return str({'task_id': self.task_id, 'start_time': self.start_time, 'end_time': self.end_time})
    
"""
LinkedList Class:
    This is responsible for implementing Linked List for the tasks and is used for implementing
    various aggregate operations.

"""
class LinkedList:
    #Constructor Implementation
    def __init__(self):
        self.head = None
        self.length = 0
        
    #This method will return the head of the linked list
    def get_list_head(self):
        return self.head
    
    #This method is responsible for printing the linked list nodes
    def print_linked_list(self):
       node = self.get_list_head()
       while node:
           print(node.task_id) 
           node = node.next
            
    #This method is responsible for inserting node in the linked list 
    #in the beginning or at end based on the flag as insert_at_starting
    def insert_node(self, node:Node, insert_at_starting=0):
        if node is None:
            return
        if self.head is None:
            self.head = node
        elif insert_at_starting:
            node.next = self.get_list_head()
            self.head = node
        else:
            temp = self.get_list_head()
            while temp.next:
                temp = temp.next
            temp.next = node
        self.length += 1
    
    #This method is responsible for printing the linked list nodes in reverse order
    def print_in_reverse(self, node):
        if node is None:
            return
        self.print_in_reverse(node.next)
        print(node.task_id) 
