class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range (self.MAX)]

    def get_hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.MAX

    def get_range_prob(self,index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key, index):
        range_prob = self.get_range_prob(index)
        for i in range_prob:
            if self.arr[i] is None:
                return i
            if self.arr[i][0] == key:
                return i
        raise Exception("Hashmap Full")

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, value)
        else:
            new_h =self.find_slot(key,h)
            self.arr[new_h] = (key, value)
        print(self.arr)

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        range_prob = self.get_range_prob(h)
        for i in range_prob:
            x = self.arr[i]
            if x is None:
                return
            if x[0] == key:
                return x[1]


    def __delitem__(self, key):
        h = self.get_hash(key)
        range_prob = self.get_range_prob(h)
        for i in range_prob:
            if self.arr[i] is None:
                return
            if self.arr[i][0] == key:
                self.arr[i] = None
        print(self.arr)

if __name__ == "__main__":
    t = HashTable()
    t["march 6"] = 130
    t["march 17"] = 20
    t["nov 1"] = 1
    t["march 33"] = 234
    print(t["dec 1"])
    t["march 33"] = 999
    print(t["march 33"])
    t["april 1"] = 87
    t["april 2"] = 123
    t["april 3"] = 234234
    t["april 4"] = 91
    t["May 22"] = 4
    t["May 7"] = 47
    # t["Jan 1"] = 0
    del t["april 2"]
    t["Jan 1"] = 0
    print(t["march 33"])
    print(t["march 1"])
    print(t["march 17"])