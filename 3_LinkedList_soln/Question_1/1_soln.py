from itertools import count


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        obj = self.head
        llstr = ''
        while obj:
            llstr += str(obj.data) + ' --> ' if obj.next else str(obj.data)
            obj = obj.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data, None)
            return
        obj = self.head
        while obj.next:
            obj = obj.next

        obj.next = Node(data,None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        obj = self.head
        while obj:
            count += 1
            obj = obj.next
        return count

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        obj = self.head
        while obj:
            if count == index-1:
                obj.next = obj.next.next
                break

            obj = obj.next
            count+=1

    def insert_at(self,index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        obj = self.head
        while obj:
            if count == index -1:
                node = Node(data, obj.next)
                obj.next = node
                break
            count+=1
            obj = obj.next

    def insert_after_value(self, data_match, data):
        obj = self.head
        while obj:
            if data_match == obj.data:
                node = Node(data, obj.next)
                obj.next = node
                return
            obj = obj.next
        print("No such Value Exists")
        # raise Exception("No such Value Exists")

    def remove_by_value(self, data_match):
        obj = self.head
        while obj.next:
            if data_match == obj.next.data:
                obj.next = obj.next.next
                return
            obj = obj.next
        print("No such Value Exists")
        # raise Exception("No such Value Exists")




if __name__ == "__main__":

    # ll = LinkedList()
    # ll.insert_values([1,4,121,357,34,7])
    # ll.print()
    # ll.insert_after_value(4,5555)
    # ll.print()
    # ll.remove_by_value(121)
    # ll.print()

    # ll.insert_at_begining(5)
    # ll.insert_at_begining(90)
    # ll.insert_at_end(70)
    # ll.insert_at(2,55)
    # ll.remove_at(3)
    # ll.print()
    # print("length of linked list is:",ll.get_length())

    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()