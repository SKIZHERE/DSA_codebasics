import time
from collections import deque
from threading import Thread


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if self.size() == 0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

q = Queue()

def Place_Order(Orders):
    for item in Orders:
        print("Placing Order: ", item)
        q.enqueue(item)
        time.sleep(0.5)

def Serve_Order():
    time.sleep(1)
    while not q.is_empty():
        order = q.dequeue()
        print("Serving Order: ", order)
        time.sleep(2)
    return
if __name__ == '__main__':
    Orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    t1 = Thread(target=Place_Order, args=(Orders,))
    t2 = Thread(target=Serve_Order)

    t1.start()
    t2.start()





