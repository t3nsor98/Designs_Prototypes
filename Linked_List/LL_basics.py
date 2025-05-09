# A Node class to represent each element in the Linked List
class Node:
    def __init__(self, data):
        self.data = data  # The data stored in the node
        self.next = None  # Pointer to the next node (initially None)

# A LinkedList class to manage the list
class LinkedList:
    def __init__(self):
        self.head = None  # Head of the Linked List (initially None)

    # Method to add a new node at the end of the Linked List
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
            return
        # Traverse to the end of the list and add the new node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Method to display the Linked List
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Method to delete a node by value
    def delete(self, key):
        current = self.head

        # If the head node itself holds the key to be deleted
        if current and current.data == key:
            self.head = current.next  # Change head
            current = None  # Free the old head
            return

        # Search for the key to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not present in the Linked List
        if not current:
            print("Key not found in the list.")
            return

        # Unlink the node from the Linked List
        prev.next = current.next
        current = None

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("Linked List after appending elements:")
    ll.display()

    ll.delete(20)
    print("Linked List after deleting 20:")
    ll.display()

    ll.delete(40)  # Trying to delete a non-existent element