"""
PROJECT 3 - Quick/Insertion Sort
Name: Anna De Biasi
PID:
"""

from Project3.QuickSort import quick_sort


class DLLNode:
    """
    Class representing a node in the doubly linked list implemented below.
    """

    def __init__(self, value, next=None, prev=None):
        """
        DO NOT EDIT
        Constructor
        @attribute value: the value to give this node
        @attribute next: the next node for this node
        @attribute prev: the previous node for this node
        """
        self.__next = next
        self.__prev = prev
        self.__value = value

    def __str__(self):
        """
        DO NOT EDIT
        String representation of node
        :return: string of node's value
        """
        return str(self.__value)

    def __eq__(self, other):
        """
        DO NOT EDIT
        Determine if two nodes are equal (same value)
        :param other: node to compare to
        :return: True if nodes are equal, False otherwise
        """
        if other is None:
            return False
        if self.__value == other.__value:
            return True
        return False

    def get_value(self):
        """
        DO NOT EDIT
        Getter for value
        :return: the value of the node
        """
        return self.__value

    def set_value(self, value):
        """
        DO NOT EDIT
        Setter for value
        :param value: the value to set
        """
        self.__value = value

    def get_next(self):
        """
        DO NOT EDIT
        Getter for next node
        :return: the next node
        """
        return self.__next

    def set_next(self, node):
        """
        DO NOT EDIT
        Setter for next node
        :param node: the node to set
        """
        self.__next = node

    def get_previous(self):
        """
        DO NOT EDIT
        Getter for previous node
        :return: the previous node
        """
        return self.__prev

    def set_previous(self, node):
        """
        DO NOT EDIT
        Setter for previous node
        :param node: the node to set
        """
        self.__prev = node


class DLL:
    """
    Class representing a doubly linked list.
    """
    c = 0

    def __init__(self, data=None):
        """
        DO NOT EDIT
        Constructor
        :param: data to initialize list
        @attribute head: the head of the linked list
        @attribute tail: the tail of the linked list
        """
        self.head = None
        self.tail = None
        self.size = 0

        if data:
            [self.insert_back(i) for i in data]

    def __str__(self):
        """
        DO NOT EDIT
        String representation of a doubly linked list showing prev and next nodes
        :return: string of linked list
        """
        result = ""
        node = self.head

        while node:
            prev = "None"
            nxt = "None"

            if node.get_previous():
                prev = str(node.get_previous().get_value())

            if node.get_next():
                nxt = str(node.get_next().get_value())

            result += str(node.get_value()) + " (" + prev + ", " + nxt + ") " + "-> "
            node = node.get_next()

        return result + "None"

    def __eq__(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """
        if self.size != other.size or self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other and temp_self.get_previous() == temp_other.get_previous():
                temp_self = temp_self.get_next()
                temp_other = temp_other.get_next()
            else:
                return False

        # Make sure both are not longer than the other
        if temp_self is None and temp_other is None:
            return True

        return False

    def get_head(self):
        """
        DO NOT EDIT
        Getter for tail
        :return: tail node
        """
        return self.head

    def set_head(self, node):
        """
        DO NOT EDIT
        Setter for head
        :param node: node to assign to head
        """
        self.head = node

    def get_tail(self):
        """
        DO NOT EDIT
        Getter for tail
        :return: tail node
        """
        return self.tail

    def set_tail(self, node):
        """
        DO NOT EDIT
        Setter for tail
        :param node: node to assign to tail
        """
        self.tail = node

    def is_empty(self):
        """
        DO NOT EDIT
        Determines if the linked list is empty or not
        :return: [boolean] true if DLL is empty, false otherwise
        """
        return self.head is None and self.tail is None

    def get_size(self):
        """
        DO NOT EDIT
        Gives the user the size of their linked list
        :return: [int] the size of the linked list
        """
        return self.size

    def insert_back(self, value):
        """
        DO NOT EDIT
        Inserts a value into the back of the list
        :param value: the value to insert
        """
        node = DLLNode(value, prev=self.tail)
        if self.tail:
            self.tail.set_next(node)
        self.tail = node
        if not self.head:
            self.head = node
        self.size += 1

    # ------------------------Complete function below---------------------------

    def count_unique(self):
        """
        Takes a linked list and condenses (but we aren't gonna say condense bc then they can look up the solution
        very easily okay? okay.) it to represent the unique elements with the count of that element
        proceeding it. When an element occurs once, do not supply the value of its count.

        Let us say the threshold for this application problem is 8

        Examples:
            input:  a->a->a->b->b->c->c->d
            output: a->3->b->2->c->2->d->1

            input:  d->c->a->a->b->c->b->d
            output: a->2->b->2->c->2->d->2

            input: a->a->a->a->a->a->a->a->a->a->a->a->b
            output: a->1->2->b  # denotes 12 a's

        * note that there will be no character sorting in this problem because the quick sort algorithm only requires
            to be able to sort numbers, the examples are only for an easier visual

        Time Complexity: O(N), Space Complexity: O(1)
        """

        if self.is_empty():
            return

        # sorting the linked list in order to properly count elements
        quick_sort(self, self.get_head(), self.get_tail(), self.get_size(), 1)

        # assign variables read and write
        write, read = self.get_head(), self.get_head()
        count = 1

        for i in range(self.get_size()):

            # increment count when node's value and next value are the same
            if read.get_next() is not None and read.get_next().get_value() == read.get_value():
                count += 1
            else:  # write to linked list when nodes value doesn't equal the node's next value
                write.set_value(read.get_value())  # write is currently on where the value is represented not count
                write = write.get_next()  # get next node to start writing count in

                if count != 1:
                    for j in str(count):  # loop to account accounting for numbers greater than 9
                        write.set_value(int(j))
                        write = write.get_next()
                    count = 1  # set count back to one in for next value

            read = read.get_next()

        else:  # handling the last value being written

            if write is None:  # when all counts in linked list are 1
                return

            # assign the tail element
            if write.get_next() is not None or count == 1:
                temp = write
                while temp is not None:  # adjusting size for removing extra elements
                    self.size -= 1
                    temp = temp.get_next()

                write = write.get_previous()  # cutting off write and going to previous node
                write.set_next(None)

            self.set_tail(write)  # setting write node equal to the tail

