class Iterable:
    def __init__(self, collection):
        self.collection = collection

# user creates collection
collection = (4, 5, 6)
iterable = Iterable(collection)

# loop over collection
index = 0
max_index = len(iterable.collection)

while index < max_index:
    item = iterable.collection[index]
    index += 1
    # user adds code here
    print(item)
