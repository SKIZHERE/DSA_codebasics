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
        d = {")":"(","}":"{","]":"["}
        for i in str:
            if i in d.values():
                self.push(i)
            elif i in d.keys():
                if self.is_empty():
                    return False
                elif self.peek() == d[i]:
                    self.pop()
        return self.is_empty()


if __name__ == '__main__':
    s = Stack()
    print(s.is_balanced("({a+b})"))
    print(s.is_balanced("))((a+b}{"))
    print(s.is_balanced("((a+b))"))
    print(s.is_balanced("))"))
    print(s.is_balanced("[a+b]*(x+2y)*{gg+kk}"))