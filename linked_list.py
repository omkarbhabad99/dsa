# Define a node class
class Node:
    def __init__(self,  input_data=None, input_next=None):
        self.data =  input_data
        self.next =  input_next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, input_data):
        node = Node(input_data)
        # head will store the address (reference) of the first node you just created.
        self.head = node

    def print(self):
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)



if __name__ == '__main__':
    root = LinkedList()
    root.insert_at_beginning(5)
    root.insert_at_beginning(10)
    root.print()