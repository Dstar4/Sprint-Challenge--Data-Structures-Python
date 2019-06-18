# buffer does not grow
# last element is replaced by new element


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    # adds a new element and deletes the last element if length == capacity
    def append(self, item):
        print(self.current)
        print(self.storage)

        # replaces the item for the "current" index
        self.storage[self.current] = item
        # check that our current position is not beyond the lists length
        if self.current < self.capacity - 1:
            # increment our position
            self.current += 1
        # if we are past the length of the array set to index[0]
        else:
            self.current = 0

    # returns all of the elements in the buffer
    # does not return None values

    def get(self):
        returnArr = []
        for i in self.storage:
            if i is not None:
                returnArr.append(i)
        print(returnArr)
        return returnArr
