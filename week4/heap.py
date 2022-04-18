import math
import sys

class Heap():
    def __init__(self, fptr):
        self.fptr = fptr
        self.h = []

    def insert(self, x):
        self.h.append(x)
        self.sift_up(0, len(self.h) - 1)
    
    def delete(self, x):
        i = self.h.index(x)
        self.h[i] = self.h[len(self.h)-1]
        self.h.pop()
        if i < len(self.h):
            self.sift_down(i)

    def print_min(self):
        self.fptr.write(str(self.h[0]) + '\n')

    def print_arr(self):
        self.fptr.write(str(self.h) + '\n')

    def sift_down(self, pos):
        end_pos = len(self.h)
        start_pos = pos
        new_item = self.h[pos]

        child_pos = 2*pos + 1 # left child position
        while child_pos < end_pos:
            # set child_pos to index of larger child
            right_pos = child_pos + 1
            if right_pos < end_pos and not self.h[child_pos] < self.h[right_pos]:
                child_pos = right_pos
            # move the larger child down
            self.h[pos] = self.h[child_pos]
            pos = child_pos
            child_pos = 2*pos + 1
        # The leaf at pos is empty now. Put new_item there, and bubble it up to its final resting
        # place.
        self.h[pos] = new_item
        self.sift_up(start_pos, pos)

    def sift_up(self, start_pos, pos):
        new_item = self.h[pos]
        while pos > start_pos:
            parent_pos = math.floor((pos-1)/2)
            parent = self.h[parent_pos]
            if new_item < parent:
                self.h[pos] = parent
                pos = parent_pos
                continue
            else:
                break
        self.h[pos] = new_item

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