"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given n scores. 
Store them in a list and find the score of the runner-up.
The first line contains n. 
The second line contains an array A[] of n integers each separated by a space.

example:
input :
5
2 3 6 6 5
output:
5
explanation:
max score is 6 so second max is 5
"""

n = int(input())
arr = list(map(int, input().split()))

max_score = max(arr)

def bukan_max(x):
    if x == max_score:
        return False
    else:
        return True

arr_baru = list(filter(bukan_max, arr))

max_score = max(arr_baru)

print(max_score)