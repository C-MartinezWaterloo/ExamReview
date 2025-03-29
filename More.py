class PriorityQueue():
    def __init__(self):
        self.queue = {}

    def enqueue(self, elem, priority):
        self.queue[elem] = priority

    def find_min(self):
        smallest = float('inf')
        minkey = None
        for key, value in self.queue.items():
            if value < smallest:
                smallest = value
                minkey = key
        return minkey

    def extract_min(self):
        val = self.find_min()
        if val is not None:
            del self.queue[val]
        return val


class CircularQueue():
    def __init__(self, spots):
        self.arr = [0] * spots
        self.start = 0
        self.end = 0
        self.spots = spots
        self.size = 0  # Track current number of elements

    def enqueue(self, elem):
        if self.size == self.spots:
            print(f"Queue full, overriding value at index {self.end}: {self.arr[self.end]}")
            self.start = (self.start + 1) % self.spots  # Move start forward if overwriting
        else:
            self.size += 1

        self.arr[self.end] = elem
        print(f"Enqueued {elem} at index {self.end}")
        self.end = (self.end + 1) % self.spots

    def dequeue(self):
        if self.size == 0:
            print("Queue is empty!")
            return None

        val = self.arr[self.start]
        print(f"Dequeued {val} from index {self.start}")
        self.arr[self.start] = 0  # Optional: clear the slot
        self.start = (self.start + 1) % self.spots
        self.size -= 1
        return val

    
    def __lt__(self, other):
        init = self.start

        
        







    def printQueue(self):
        print("Queue is: [", end="")
        for i in range(self.size):
            idx = (self.start + i) % self.spots
            print(self.arr[idx], end=", " if i < self.size - 1 else "")
        print("]")





if __name__ == "__main__":
    q = PriorityQueue()

    q.enqueue("Bob", 5)
    q.enqueue("Charlie", 2)
    q.enqueue("Sarah", 1)

    c = CircularQueue(5)
    

    c.enqueue(10)
    c.enqueue(12)
    c.enqueue(7)
    c.enqueue(7)
    c.enqueue(1)

    c.printQueue()

    c.dequeue()





    # print(q.extract_min())  # Sarah
    # print(q.extract_min())  # Charlie
    # print(q.extract_min())  # Bob
