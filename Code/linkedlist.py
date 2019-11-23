#!python


class Node(object):

    def __init__(self, data, next=None):
        """Initialize this node with the given data."""
        self.data = data # assign data
        self.next = next # initializes next as null

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item. Traverses linked list."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions? loop, indefinite"""
        # TODO: Loop through all nodes and count one for each
        count = 0

        for node in self.items():
            count += 1
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Why and under what conditions? one condition, no loop, constant time"""

        # TODO: Append node after tail, if it exists
        new_node = Node(item) # Create new node to hold given item

        if self.is_empty():
            self.head = new_node
        if self.tail is not None:
            self.tail.next = new_node #use self.tail's next pointer before we change tail reference
        self.tail = new_node


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Why and under what conditions? one condition, no loop, constant time"""

        # got help from https://www.geeksforgeeks.org/find-length-of-a-linked-list-iterative-and-recursive/

        new_node = Node(item) # create new node and put in item
        if self.is_empty():
            self.tail = new_node # new_node becomes head and tail if list in empty
        else:
            new_node.next = self.head # make new node's next reference point to "current" head

        self.head = new_node # make head reference point to the new Node was was prepended


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        # quality function returns True or False,check is this one the one I want, checking node's data
        TODO: Best case running time: O(1) Why and under what conditions? 1 item
        TODO: Worst case running time: O(n) Why and under what conditions? indefinite"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        node = self.head
        while node is not None:
            if quality(node.data) is True:
                return node.data
            else:
                node = node.next

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) Why and under what conditions? one item
        TODO: Worst case running time: O(n) Why and under what conditions? indefinite amt"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        node = self.head
        previous = None
        while node is not None: # loops over list as long as there are items
            if node.data == item: # if the node.data matches item
                if previous == None: # and it's the head
                    self.head = node.next # move head to next item
                    if node.next == None: # if head is also tail
                        self.tail = None # set tail to None
                elif node.next == None: # otherwise if item is just the tail
                    previous.next = None # set the previous item's next to NOne
                    self.tail = previous # make the previous item the tail
                elif node.data == item: # for all other cases
                    previous.next = node.next # set previous node's next reference to next
                return
            else:
                previous = node # keep searching
                node = node.next


        raise ValueError(f"Item not found: {item}")

    def replace(self, old_item, new_item):
        node = self.head

        while node is not None:
            if node.data == old_item:
                node.data = new_item
                return
            else:
                node = node.next


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
