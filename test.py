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







class CircularCueue:
    def __init__(self, spots):
        self.cue = [0] * spots
        self.startindex = 0
        self.endindex = 0
        self.spots = spots
        self.size = 0

    def enqueue(self,data):

        if self.size >= self.spots:
            print("CUE IS FULL")

        else:
            self.cue[self.endindex] = data

            self.endindex += 1

            self.endindex = self.endindex % self.spots

            self.size += 1

    
    def dequeue(self):

        val = self.cue[self.startindex]


        self.cue[self.startindex] = 0

        self.startindex += 1

        self.startindex = self.startindex % self.spots

        self.size -= 1

        return val


    def cue_to_arr(self):
        cur = [0] * self.spots 

        index = self.startindex

        for i in range(5):
            cur[i] = self.cue[(index + i) % self.spots]

        return cur


    def printcueue(self):
        for i in range(5):
            print(self.cue[i])

    def __gt__(self, other):
        return self.cue_to_arr() > other.cue_to_arr()








if __name__ == "__main__":

    C = CircularCueue(5)
    
    C.enqueue(1)
    C.enqueue(2)
    C.enqueue(3)
    C.enqueue(4)
    C.enqueue(5)
    C.dequeue()
    C.enqueue(6)

    D = CircularCueue(5)
    D.enqueue(9)
    D.enqueue(1)
    D.enqueue(4)
    D.printcueue()
    print(D.cue_to_arr())


    print(D > C)




   

    

    



