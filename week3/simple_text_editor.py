import sys

class Editor:

    def __init__(self, fptr):
        self.fptr = fptr
        self.S = ""
        self.S_log = [""]

    def append(self, w):
        self.S += w
        self.S_log.append(self.S)

    def delete(self, k):
        self.S = self.S[:len(self.S)-k]
        self.S_log.append(self.S)
    
    def print(self, k):
        self.fptr.write(self.S[k-1:k])
        self.fptr.write('\n')
    
    def undo(self):
        self.S_log.pop()
        self.S = self.S_log[len(self.S_log)-1]

if __name__ == "__main__":
    fptr = open(sys.stdout.fileno(), 'w')

    q = int(input())

    editor = Editor(fptr)
    for t_itr in range(q):
        operation = list(input().split(' '))

        if operation[0] == '1':
            editor.append(operation[1])
        if operation[0] == '2':
            editor.delete(int(operation[1]))
        if operation[0] == '3':
            editor.print(int(operation[1]))
        if operation[0] == '4':
            editor.undo()