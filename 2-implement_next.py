class Iterable:
    def __init__(self, collection):
        self.collection = collection

class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0
        self.max_index = len(collection)

    def __next__(self):
        if self.index >= self.max_index:
            raise StopIteration

        item = collection[self.index]
        self.index += 1
        return item

# user creates collection
collection = (4, 5, 6)
iterable = Iterable(collection)
iterator = Iterator(iterable.collection)

# loop over collection
while True:
    try:
        item = iterator.__next__()
        # user adds code here
        print(item)
    except StopIteration:
        break
