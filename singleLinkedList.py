class ListNode:
    def __init__(self, data):
        # Store data.
        self.data = data
        
        # Store reference (next item).
        self.next = None
        return
    
    def has_value(self, value):
        # Method to compare the value with the node data.
        if self.data == value:
            return True
        else:
            return False

class SingleLinkedList:
    def __init__(self):
        # Constructor to initiate this object.
        
        self.head = None
        self.tail = None
        return

    def add_list_item(self, item):
        # Add an item at the end of the list.
        
        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item
            
        return

    def output_list(self):
        # Outputs the list (the value of the node, actually).

        theList = []
        
        current_node = self.head
        
        while current_node is not None:
            theList.append(current_node.data)
            
            # Jump to the linked node.
            current_node = current_node.next
            
        return theList

    def unordered_search (self, value):
        # Search the linked list for the node that has this value.
        
        # Define current_node.
        current_node = self.head
        
        # Define position.
        node_id = 1
        
        # Define list of results.
        results = []
        
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
                
            # Jump to the linked node.
            current_node = current_node.next
            node_id = node_id + 1
        
        return results

    def remove_list_item_by_value(self, value):
        
        # Define current_node.
        current_node = self.head
        previous_node = None
        
        # Define position.
        node_id = 1
        
        while current_node is not None:
            if current_node.has_value(value):
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    # we don't have to look any further
                    return
                
            # Jump to the linked node.
            previous_node = current_node
            current_node = current_node.next
            node_id = node_id + 1
        
        return

if __name__ == "__main__":
    
    lList = SingleLinkedList()

    # Add to list.
    node1 = ListNode(10)
    node2 = ListNode(5)
    node3 = ListNode(3)
    node4 = ListNode(59)
    lList.add_list_item(node1)
    lList.add_list_item(node2)
    lList.add_list_item(node3)
    lList.add_list_item(node4)

    # Print list.
    print("-----------------Old List")
    print(lList.output_list())

    # Find in list.
    print("-----------------")
    print("Position:", lList.unordered_search(59))

    # Remove from list.
    lList.remove_list_item_by_value(59)

    # Print list.
    print("-----------------Current List")
    print(lList.output_list())