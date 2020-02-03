'''
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements
'''

import argparse
import sys

# My solution:
# Time = O(n); Space = O(n) 
def my_solution(orig_arr, num_elements, rotate):
    new_arr = []
    for i in range(0, num_elements):
        if (num_elements > i+rotate):
            new_arr.append(orig_arr[i+rotate])
        else:
            new_arr.append(orig_arr[i+rotate-num_elements])
    print (new_arr)

# Other Solutions:
# Time = O(n); Space = O(d) - using temp_arr
# Time = O(n*d); Space = O(1) - using left_rotator
# Time = O(n); Space = O(1) - using left rotator with gcd
def gfg_solution(orig_arr, num_elements, rotate):
    rotate = rotate % num_elements
    gcd_value = gcd(rotate, num_elements)
    for i in range(gcd_value):
        temp = orig_arr[i]
        j = i
        while 1:
            k = j+rotate
            if k>=num_elements:
                k = k-num_elements
            if k == i:
                break
            orig_arr[j] = orig_arr[k]
            j = k
        orig_arr[j] = temp
    print (orig_arr)

def gcd(a, b):
    if b == 0:
        return a;
    else:
        return gcd(b, a%b)


# Main Program
parser = argparse.ArgumentParser(description="Rotate an array.")
parser.add_argument("--mine", action="store_true", help="Run my solution for the prolem")
parser.add_argument("--gfg", action="store_true", help="Run the gfg solution for the problem")
args = parser.parse_args()
if (len(sys.argv) > 1):
    num_elements = int(input("Enter the number of elements in the array: "))
    orig_arr = []
    for i in range(0, num_elements):
        orig_arr.append(input("Enter the value of element at index " + str(i) + " in the array: "))
        i +=1
    print (orig_arr)

    rotate = int(input("Enter the number by which you want to rotate the array: "))

    if (args.mine == True):
        my_solution(orig_arr, num_elements, rotate)
    elif (args.gfg == True):
        gfg_solution(orig_arr, num_elements, rotate)
    else:
        print ("Enter the right argument")
else:
    print ("Too short to run, enter arguments")
