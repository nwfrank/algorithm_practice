import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_utils import Tester

def quick_sort(arr):
   return recursive_quicksort(arr, 0, len(arr) - 1)

def recursive_quicksort(arr, left, right):
    if left < right:
        pivot = arr[right]
        i = left
        for j in range(left, right):
            if arr[j] < pivot:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i += 1
        temp = arr[i]
        arr[i] = arr[right]
        arr[right] = temp
        
        recursive_quicksort(arr, left, i - 1)
        recursive_quicksort(arr, i + 1, right)
    return arr



# ============== TESTS ==============

def test_quick_sort():
    tester = Tester()
    
    tester.test('Unsorted array', lambda: quick_sort([14, 3, 2, 5, 7, 9, -1]), [-1, 2, 3, 5, 7, 9, 14])
    tester.test('Already sorted array', lambda: quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  
    tester.test('Reverse sorted array', lambda: quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])  
    tester.test('Array with duplicates', lambda: quick_sort([4, 2, 4, 3, 1, 2]), [1, 2, 2, 3, 4, 4])  
    tester.test('Single-element array', lambda: quick_sort([42]), [42])  
    tester.test('Empty array', lambda: quick_sort([]), [])  
    tester.test('Array with negative numbers', lambda: quick_sort([-3, -1, -7, -2]), [-7, -3, -2, -1])  
    tester.test('Array with mixed positive and negative numbers', lambda: quick_sort([3, -2, 7, -5, 0, 4]), [-5, -2, 0, 3, 4, 7]) 

    arr_random = random.sample(range(1, 100), 10)
    target = sorted(arr_random)
    tester.test('Array of random numbers', lambda: quick_sort(arr_random), target)

    tester.print_pass_percentage()

test_quick_sort()