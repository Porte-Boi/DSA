# from collections import defaultdict

# capitals = defaultdict(lambda: "The key doesn't exists")
# capitals['Dhaka'] = 'Bangladesh'

# print(capitals['Dhaka'])
# print(capitals['Delli'])



# from collections import Counter
# # A counter from an iterable
# c1 = Counter(['aaa', 'bbb', 'aaa', 'ccc', 'bbb', 'aaa'])
# # A counter from a mapping
# c2 = Counter({'red' : 4, 'blue' : 5}) 
# # A counter from keyword args
# c3 = Counter(cats=4, dogs=8)

# print(c1)
# print(c2)
# print(c3)

# print(list(c1.elements()))
# print(c1.total())


# from sklearn.feature_extraction.text import CountVectorizer

# documents = ["Hello, my name is Shawon"]

# cv = CountVectorizer()

# X = cv.fit_transform(documents)

# print('Unique words: ', cv.get_feature_names_out())

# # print sparse matrix with word frequencY
# pd.DataFrame(X.toarray(), columns = cv.get_feature_names_out())



def get_hash(key):
    h = 0
    for i in key:
        h += ord(i)
    return h % 100

class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [[] for j in range(self.Max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.Max
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)

        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h] [idx]= (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))
        

    def __getitem__(self,index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
    

t = HashTable()
print(t.get_hash('march 6'))
print(t.get_hash('march 17'))
