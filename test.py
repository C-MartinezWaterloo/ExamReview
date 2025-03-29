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
        cur = [0] * self.size

        index = self.startindex

        for i in range(5):
            print(self.cue[(index + i) % self.size])


    def printcueue(self):
        for i in range(5):
            print(self.cue[i])

    def __lt__(self, other):
        return self.cue_to_arr > other.cue_to_arr









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




   

    

    



