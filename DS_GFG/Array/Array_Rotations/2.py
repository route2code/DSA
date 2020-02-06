'''
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements
'''

import argparse
import sys

# Solution
# Time = O(n); Space = O(1) 
def solution(orig_arr, num_elements, rotate):
    if rotate == 0:
        return
    reverse_arr(orig_arr, 0, rotate-1)
    reverse_arr(orig_arr, rotate, num_elements-1)
    reverse_arr(orig_arr, 0, num_elements-1)
    print (orig_arr)

def reverse_arr(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start = start+1
        end = end-1

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
