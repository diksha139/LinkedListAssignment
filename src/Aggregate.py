from src.LinkedList import LinkedList

"""
Aggregate class is responsible for implementating various operations on the linked list
    1. Get Minimum Timed Task Details
    2. Get Maximum Timed Task Details
    3. Get Average of all the execution times of the tasks pushed in the linked list
"""
class Aggregate:
    
    #Initializing linked list object for various operations 
    def __init__(self, linked_list:LinkedList):
        self.linked_list = linked_list
    
    #Function responsible for searching the task having maximum execution time among all the tasks
    def get_maximised_time_task(self):
        node = self.linked_list.get_list_head()
        if node is None:
            return
        max_task = node
        max_task_time = node.end_time - node.start_time
        node = node.next
        while node:
            task_completion_time = node.end_time - node.start_time
            if task_completion_time >= max_task_time:
                max_task_time = task_completion_time
                max_task = node
            node = node.next
        return max_task, max_task_time
    
    #Function responsible for searching the task having minimum execution time among all the tasks
    def get_minimised_timed_task(self):
        node = self.linked_list.get_list_head()
        if node is None:
            return
        min_task = node
        min_task_time = node.end_time - node.start_time
        node = node.next
        while node:
            task_completion_time = node.end_time - node.start_time
            if task_completion_time <= min_task_time:
                min_task_time = task_completion_time
                min_task = node
            node = node.next
        return min_task, min_task_time
    
    #Function responsible for calculating average of the all execution times of the tasks in the linked list
    def get_average_time_of_all_tasks(self):
        node = self.linked_list.get_list_head()
        if node is None:
            return
        sum_task_time = 0
        while node:
            task_time = node.end_time - node.start_time
            sum_task_time += task_time
            node = node.next
        average = sum_task_time/self.linked_list.length
        return average, sum_task_time, self.linked_list.length
