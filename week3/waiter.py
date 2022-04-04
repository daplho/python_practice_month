import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def next_prime(list):
    if list == [2]:
        a = 3
    else:
        a = list[-1]+2
        found = 0
        while found == 0:
            for i in list:
                if a % i == 0:
                    a = a + 1
                    break
            else:
                found = 1
    return a

def first_primes(n):
    list = [2]
    while len(list) < n:
        new_entry = next_prime(list)
        list += [new_entry]
    return list

def waiter(number, q):
    A_cur = number
    Ai = []
    Bi = []
    answers = []
    primes_list = first_primes(q)

    for i in range(q):
        while len(A_cur) > 0:
            cur_num = A_cur.pop(0)
            if cur_num % primes_list[i] == 0:
                Bi.insert(0, cur_num)
            else:
                Ai.insert(0, cur_num)
        answers.extend(reversed(Bi))
        A_cur = Ai
        Ai = []
        Bi = []
    answers.extend(reversed(A_cur))
    return answers

if __name__ == '__main__':
    fptr = open(sys.stdout.fileno(), 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()