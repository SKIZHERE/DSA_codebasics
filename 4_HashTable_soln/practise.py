
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range (self.MAX)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h%10

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for i, j in enumerate(self.arr[h]):
            if len(j) == 2 and j[0]== key:
                self.arr[h][i] = (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for i in self.arr[h]:
            if i[0] == key:
                return i[1]


    def __delitem__(self, key):
        h = self.get_hash(key)
        for i, val in enumerate(self.arr[h]):
            if val[0] == key:
                del self.arr[h][i]

if __name__ == "__main__":
    t = HashTable()
    t["march 6"] = 130
    t["march 6"] = 90
    t["march 1"] = 30
    t["march 17"] = 20
    print(t["march 6"])
    print(t["march 1"])
    del t["march 1"]
    print(t["march 1"])
    print(t["march 17"])

