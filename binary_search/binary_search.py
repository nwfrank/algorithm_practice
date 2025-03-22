import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_utils import Tester

def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False


# ============== TESTS ==============

def test_binary_search():
    tester = Tester()
    
    arr = [1, 3, 5, 7, 9]
    tester.test('Target is in the array', lambda: binary_search(arr, 5), True)
    tester.test('Target is not in the array', lambda: binary_search(arr, 4), False)
    tester.test('Empty array', lambda: binary_search([], 5), False)
    tester.test('Single-element array, target is present', lambda: binary_search([5], 5), True)
    tester.test('Single-element array, target is not present', lambda: binary_search([5], 3), False)
    tester.test('Large array', lambda: binary_search(list(range(1, 10001)), 5000), True)
    tester.test('Array with duplicates, target is a duplicate', lambda: binary_search([1, 2, 2, 2, 3], 2), True)
    tester.test('Array with duplicates, target is not a duplicate', lambda: binary_search([1, 2, 2, 2, 3], 4), False)
    
    arr = random.sample(range(1, 100), 10)
    arr.sort()
    target = random.choice(arr)
    tester.test('Random numbers test', lambda: binary_search(arr, target), True)

    tester.print_pass_percentage()

test_binary_search()