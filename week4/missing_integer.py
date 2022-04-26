import sys

def missing_integer(arr):
    for i in range(len(arr)):
        if 0 <= arr[i]-1 and arr[i]-1 < len(arr):
            # swap arr[i] and arr[arr[i]]
            arr[arr[i]-1],arr[i] = arr[i],arr[arr[i]-1]
        else:
            arr[i] = 0

    for i in range(len(arr)):
       if 0 <= arr[i]-1 and arr[i]-1 < len(arr):
           # swap arr[i] and arr[arr[i]]
           arr[arr[i]-1],arr[i] = arr[i],arr[arr[i]-1]
       else:
           arr[i] = 0
    
    for i in range(len(arr)):
        if i != arr[i]-1:
            return i+1
    
    return 0

if __name__ == "__main__":
    fptr = open(sys.stdout.fileno(), 'w')

    n = int(input())

    arr = list(map(int, input().split(' ')))
    
    result = missing_integer(arr)
    fptr.write("missing integer: " + str(result) + '\n')