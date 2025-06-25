
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range (self.MAX)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h%10

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] is not None:
            self.arr[h].append((key,value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

if __name__ == "__main__":
    t = HashTable()
    t["march 6"] = 130
    t["march 1"] = 20
    t["march 17"] = 20
    print(t["march 1"])
    del t["march 1"]
    print(t["march 1"])
    print(t["march 6"])

