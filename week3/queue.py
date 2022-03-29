import sys

class Queue():
    l = []

    def enqueue(self, x):
        self.l.append(x)
    
    def dequeue(self):
        return self.l.pop(0)

    def peek(self):
        return self.l[0]

if __name__ == "__main__":
    fptr = open(sys.stdout.fileno(), 'w')

    q = int(input())

    queue = Queue()
    for t_itr in range(q):
        query = list(map(int, input().split(' ')))

        if query[0] == 1:
            queue.enqueue(int(query[1]))
        if query[0] == 2:
            queue.dequeue()
        if query[0] == 3:
            fptr.write(str(queue.peek()))
            fptr.write('\n')

    fptr.close()