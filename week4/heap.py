import math
import sys

class Heap():
    def __init__(self, fptr):
        self.fptr = fptr
        self.h = []

    def insert(self, x):
        self.h.append(x)
        self.sift_up(len(self.h) - 1)
    
    def delete(self, x):
        for i in range(len(self.h)):
            if x == self.h[i]:
                if i == len(self.h)-1:
                    self.h.pop()
                    return
                else:
                    self.h[i], self.h[len(self.h)-1] = self.h[len(self.h)-1], self.h[i]
                    self.h.pop()
                    self.sift_down(i)
                    return

    def print_min(self):
        self.fptr.write(str(self.h[0]) + '\n')

    def print_arr(self):
        self.fptr.write(str(self.h) + '\n')

    def sift_down(self, i):
        while i < len(self.h):
            child_i1 = 2*i+1
            child_i2 = 2*i+2

            if child_i1 < len(self.h) and child_i2 < len(self.h):
                if self.h[child_i1] < self.h[child_i2] and self.h[child_i1] < self.h[i]:
                    self.h[child_i1], self.h[i] = self.h[i], self.h[child_i1]
                    i = child_i1
                else:
                    self.h[child_i2], self.h[i] = self.h[i], self.h[child_i2]
                    i = child_i2
            elif child_i1 < len(self.h) and self.h[child_i1] < self.h[i]:
                self.h[child_i1], self.h[i] = self.h[i], self.h[child_i1]
                i = child_i1
            elif child_i2 < len(self.h) and self.h[child_i2] < self.h[i]:
                self.h[child_i2], self.h[i] = self.h[i], self.h[child_i2]
                i = child_i2
            else:
                return

    def sift_up(self, i):
        while i > 0:
            parent_i = math.floor((i-1)/2)
            if self.h[i] < self.h[parent_i]:
                self.h[i], self.h[parent_i] = self.h[parent_i], self.h[i]
                i = parent_i
            else:
                return

if __name__ == "__main__":
    fptr = open(sys.stdout.fileno(), 'w')

    q = int(input())

    heap = Heap(fptr)
    for q_itr in range(q):
        query = list(map(int, input().split(' ')))

        if query[0] == 1:
            heap.insert(query[1])
        if query[0] == 2:
            heap.delete(query[1])
        if query[0] == 3:
            heap.print_min()
        if query[0] == 4:
            heap.print_arr()