import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_utils import Tester

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr



# ============== TESTS ==============

def test_binary_search():
    tester = Tester()
    
    tester.test('Unsorted array', lambda: bubble_sort([14, 3, 2, 5, 7, 9, -1]), [-1, 2, 3, 5, 7, 9, 14])
    tester.test('Already sorted array', lambda: bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  
    tester.test('Reverse sorted array', lambda: bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])  
    tester.test('Array with duplicates', lambda: bubble_sort([4, 2, 4, 3, 1, 2]), [1, 2, 2, 3, 4, 4])  
    tester.test('Single-element array', lambda: bubble_sort([42]), [42])  
    tester.test('Empty array', lambda: bubble_sort([]), [])  
    tester.test('Array with negative numbers', lambda: bubble_sort([-3, -1, -7, -2]), [-7, -3, -2, -1])  
    tester.test('Array with mixed positive and negative numbers', lambda: bubble_sort([3, -2, 7, -5, 0, 4]), [-5, -2, 0, 3, 4, 7]) 

    arr_random = random.sample(range(1, 100), 10)
    target = sorted(arr_random)
    tester.test('Array of random numbers', lambda: bubble_sort(arr_random), target)

    tester.print_pass_percentage()

test_binary_search()