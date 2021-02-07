# Given a linked list of integers, remove any nodes from the linked list that have values that have previously occurred in the linked list. Your function should return a reference to the head of the updated linked list.

# Example:
# Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
# Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
# Explanation: The input list contains redundant nodes (3), (6), and (2), so those should be removed from the list.

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def condense_linked_list(node):
    # have a visite set to track the duplicates
    visited_set = set()
    # add the head of the node to the set(first value -> {3})
    visited_set.add(node.value)
    # have a current node var
    current_node = node
    # As long as current node next value exits --> keep looping through
    while current_node.next:
        # if current node next value not in the set >> then jump the nodes
        if current_node.next.value in visited_set:
            current_node.next = current_node.next.next
        else:
            # else >>> add it the visited set
            visited_set.add(current_node.next.value)  
            current_node = current_node.next 
    return node             