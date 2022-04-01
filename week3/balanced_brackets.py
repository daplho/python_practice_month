import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    brackets = []

    for c in s:
        try:
            if c in '({[':
                brackets.append(c)
            elif c == ')' and brackets.pop() != '(':
                return "NO"
            elif c == '}' and brackets.pop() != '{':
                return "NO"
            elif c == ']' and brackets.pop() != '[':
                return "NO"
        except IndexError:
            return "NO"
    
    if len(brackets) != 0:
        return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(sys.stdout.fileno(), 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()