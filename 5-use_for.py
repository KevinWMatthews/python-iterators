class Iterable:
    def __init__(self, collection):
        self.collection = collection

    def __iter__(self):
        # Create the correct iterator
        return Iterator(self.collection)

class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0
        self.max_index = len(collection)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.max_index:
            raise StopIteration

        item = collection[self.index]
        self.index += 1
        return item

# user creates collection
collection = (4, 5, 6)
iterable = Iterable(collection)

# loop over collection
for item in iterable:
    # user adds code here
    print(item)
