import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    length = len(arr)
    count = 0
    mini = min(arr)
    mini_ind = arr.index(mini)
    if mini_ind == 0:
        mini_ind = 0
    else:
        arr[0],arr[mini_ind] = arr[mini_ind], arr[0]
        count = count+1
    for i in range (length-1):
        if arr[i+1]==i+2:
            continue
        new_mini = min(arr[i+1:])
        if arr[i+1] >new_mini:
            new_ind = arr.index(new_mini)
            arr[i+1], arr[new_ind] = arr[new_ind],arr[i+1] 
            count = count+1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
