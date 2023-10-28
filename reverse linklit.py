class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def print_reverse(self, node):
        if node is None:
            return
        self.print_reverse(node.next)
        print(node.data)

    def print_reverse_list(self):
        self.print_reverse(self.head)

# Example usage
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    print("Original Linked List:")
    temp = linked_list.head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

    print("\nLinked List in Reverse Order:")
    linked_list.print_reverse_list()
