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


if __name__ == "__main__":
    q = PriorityQueue()

    q.enqueue("Bob", 5)
    q.enqueue("Charlie", 2)
    q.enqueue("Sarah", 1)

    print(q.extract_min())  # Sarah
    print(q.extract_min())  # Charlie
    print(q.extract_min())  # Bob
