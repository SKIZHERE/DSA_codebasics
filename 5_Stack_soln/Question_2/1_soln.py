from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)
    def reverse_string(self,str):
        new_str = ""
        for i in str:
            self.push(i)
        for j in range(self.size()):
            new_str += self.pop()
        return new_str
    def is_balanced(self,str):
        for i in str:
            if i in "([{":
                self.push(i)
            elif i == ")" and self.peek() != "(":
                return False
            elif i == "}" and self.peek() != "{":
                return False
            elif i == "]" and self.peek() != "[":
                return False
        if self.is_empty():
            return True
        return False


if __name__ == '__main__':
    s = Stack()
    print(s.is_balanced("))((a+b}{"))