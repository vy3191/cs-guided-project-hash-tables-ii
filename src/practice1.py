class HashTableNode:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None

class HashTable:
  def __init__(self, capacity):
    self.capacity = capacity
    self.storage = [None] * capacity
    
  def my_hash(self,key):
    bytes_str = key.encode()
    bytes_sum = 0
    for byte in bytes_str:
      bytes_sum += byte
    return bytes_sum % self.capacity
  
  def insert(self, key, value):
    # convert the key to an index for our storage
    index = self.my_hash(key)
    print(f'{key} hashed to {index}')
    # store the value in the storage
    
    # UPDATING THE NODE AT THE GIVEN INDEX
    current_node = self.storage[index]
    while current_node is not None:
      # compare the current node key to the key we are inserting
      if current_node.key == key:
        current_node.value = value
        return
      else:
        current_node = current_node.next        
    
    # get the new node
    new_node = HashTableNode(key, value)
    # grab the value at the current index(which should None to begin with)
    current_head = self.storage[index]
    # if there are no values stored at the index
    if current_head is None:
      self.storage[index] = new_node
    # if there are already node is stored
    else:
      # move the value stored at the index down
      # Make new node - the head of the list
      new_node.next = current_head
      self.storage[index] = new_node
    
  def get(self, key):
    # convert the key to an index for our storage
    index = self.my_hash(key)    
    # get the head of the linked list using our index
    current_node = self.storage[index]
    # search through the linked list
    while current_node:
      if current_node.key == key:
        return current_node.value
      current_node = current_node.next

  def delete(self, key):
    # get the index
    index = self.my_hash(key)      
    # get the current node
    current_node = self.storage[index]
    # if there is nothing to delete
    if current_node is None:
      print("Nothing to Delete")
      return 
    # check if the node to delete is the head
    if current_node.key == key:
      print(f"Deleted value>>>{current_node.value}")
      self.storage[index] == current_node.next
      return
    
    #otherwise, delete the node from inside the list
    prev_node = None
    while current_node:
      # look for the node that matches our key
      if current_node.key == key:
        # delete that node
        # make previous node, point to whatever current node points to..
        print(f"Deleted node>>>>{current_node.value}")
        prev_node.next = current_node.next
        return
      else:
        prev_node = current_node
        current_node = current_node.next
        
    print(f"Error: could not find {key}")  
    return    
      
  
my_dict = HashTable(8)  
my_dict.insert('banana', 'banana is a fruit')
my_dict.insert('apple', 'apple is a fruit')
my_dict.insert('cucumber', 'cucumber is a veg')
my_dict.insert('tomato', 'tomato is a fruit/veg')


my_dict.insert('peach', 'peach definitely not a banana')

print(my_dict.get('apple'))
print(my_dict.get('cucumber'))
print(my_dict.get('tomato'))
print(my_dict.get('banana'))
print(my_dict.get('peach'))
print(my_dict.delete("banana"))
print(my_dict.get('banana'))