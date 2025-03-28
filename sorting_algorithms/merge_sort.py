import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_utils import Tester

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    l, r = 0, 0
    merged = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    for i in range(l, len(left)):
        merged.append(left[i])
    for i in range(r, len(right)):
        merged.append(right[i])
    return merged




# ============== TESTS ==============

def test_merge_sort():
    tester = Tester()
    
    tester.test('Unsorted array', lambda: merge_sort([14, 3, 2, 5, 7, 9, -1]), [-1, 2, 3, 5, 7, 9, 14])
    tester.test('Already sorted array', lambda: merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  
    tester.test('Reverse sorted array', lambda: merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])  
    tester.test('Array with duplicates', lambda: merge_sort([4, 2, 4, 3, 1, 2]), [1, 2, 2, 3, 4, 4])  
    tester.test('Single-element array', lambda: merge_sort([42]), [42])  
    tester.test('Empty array', lambda: merge_sort([]), [])  
    tester.test('Array with negative numbers', lambda: merge_sort([-3, -1, -7, -2]), [-7, -3, -2, -1])  
    tester.test('Array with mixed positive and negative numbers', lambda: merge_sort([3, -2, 7, -5, 0, 4]), [-5, -2, 0, 3, 4, 7]) 

    arr_random = random.sample(range(1, 100), 10)
    target = sorted(arr_random)
    tester.test('Array of random numbers', lambda: merge_sort(arr_random), target)

    tester.print_pass_percentage()
   

test_merge_sort()