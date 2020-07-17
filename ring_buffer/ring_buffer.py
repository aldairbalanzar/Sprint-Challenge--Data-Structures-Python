class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.index = 0

    def append(self, item):
        if len(self.data) == self.capacity:
            # print('if statement')
            self.data[self.index] = item
            self.index = self.index + 1
            if self.index == self.capacity:
                self.index = 0
        else:
            # print('else statement')
            self.data.append(item)

    def get(self):
        data = []
        for i in self.data:
            if i is not None:
                data.append(i)
        return data

ring = RingBuffer(5)

for i in range(10):
    ring.append(i)
    # print(ring.index)
# print('RING: ', ring.data)
# print(ring.get())