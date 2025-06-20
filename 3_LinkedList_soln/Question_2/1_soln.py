from itertools import count


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class doubleLinkedList:
    def __init__(self):
        self.head = None
        self.foot = None

    def print(self):
        if self.head == None:
            print("list is empty")
            return
        obj = self.head
        dllstr = ""
        while obj:
            dllstr += str(obj.data) + " <--> " if obj.next else str(obj.data)
            obj = obj.next
        print(dllstr)

    def insert_at_beginning(self, data):
        node = Node( data, self.head, None)
        if self.head != None:
            self.head.prev = node
        else:
            self.foot = node
        self.head = node

    def insert_at_end(self, data):
        if self.head == None:
            self.insert_at_beginning(data)
            return

        node = Node(data, None, self.foot)
        self.foot.next = node
        self.foot = node

    def insert_values(self,data_list):
        self.head = None
        self.foot = None

        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        obj = self.head
        while obj:
            count+=1
            obj=obj.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            print("invalid index")
            return
        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.foot = None
            return
        count = 0
        obj = self.head
        while obj:
            if count == index:
                if obj.prev:
                    obj.prev.next = obj.next
                if obj.next:
                    obj.next.prev = obj.prev
                return
            obj = obj.next
            count += 1


if __name__ == "__main__":
    dll = doubleLinkedList()
    # dll.insert_at_beginning(5)
    # dll.print()
    # dll.insert_at_end(1)
    # dll.print()
    # dll.insert_at_end(99)
    # dll.print()
    # dll.insert_at_beginning(7)
    dll.insert_values([1,532,23,53,2,5])
    dll.print()
    print("length : ",dll.get_length())
    dll.remove_at(2)
    dll.print()