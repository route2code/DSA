'''
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements
'''

import argparse
import sys

# Solution
# Time = O(n); Space = O(1) 
def solution(orig_arr, num_elements, rotate):
    if (rotate == 0 or rotate == num_elements):
        return;
    i = rotate;
    j = num_elements - rotate
    while (i != j):
        if (i < j):
            swap(orig_arr, rotate-i, rotate+j-i, i)
            j -= i
        else:
            swap(orig_arr, rotate-i, rotate, j)
            i -= j
    swap(orig_arr, rotate-i, rotate, i)
    print (orig_arr)

def swap(arr, start, end, total):
    i = 0
    while (i < total):
        temp = arr[start+i]
        arr[start+i] = arr[end+i]
        arr[end+i] = temp
        i = i+1

# Main Program
parser = argparse.ArgumentParser(description="Rotate an array.")
parser.add_argument("--mine", action="store_true", help="Run my solution for the prolem")
parser.add_argument("--gfg", action="store_true", help="Run the gfg solution for the problem")
args = parser.parse_args()
num_elements = int(input("Enter the number of elements in the array: "))
orig_arr = []
for i in range(0, num_elements):
    orig_arr.append(input("Enter the value of element at index " + str(i) + " in the array: "))
    i +=1
print (orig_arr)

rotate = int(input("Enter the number by which you want to rotate the array: "))

solution(orig_arr, num_elements, rotate)
