from collections import deque
from itertools import permutations
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_utils import Tester

def topological_sort(arr):
    graph = {}
    in_degree = {}
    
    for vertex in arr:
        vertex_val = vertex['val']
        graph[vertex_val] = []
        in_degree[vertex_val] = 0

    for vertex in arr:
        for prereq in vertex['prerequisites']:
            graph[prereq].append(vertex['val'])
            in_degree[vertex['val']] += 1
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for dependent in graph[vertex]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

    return result if len(result) == len(arr) else []


# ============== TESTS ==============

def test_topological_sort():
    tester = Tester()
    
    arr = [
        {"val": "Math", "prerequisites": []},
    ]
    tester.test('Single node with no prerequisites', lambda: topological_sort(arr), ['Math'])

    arr = [
        {"val": "Math", "prerequisites": ["Physics"]},
        {"val": "Physics", "prerequisites": []},
    ]
    tester.test('Two nodes, one with a prerequisite', lambda: topological_sort(arr), ['Physics', 'Math'])

    arr = [
        {"val": "Math", "prerequisites": ["Physics"]},
        {"val": "Physics", "prerequisites": ["Math"]},
    ]
    tester.test('Circular dependency (return empty array)', lambda: topological_sort(arr), [])
    
    arr = [
        {"val": "A", "prerequisites": []},
        {"val": "B", "prerequisites": []},
        {"val": "C", "prerequisites": ["A", "B"]},
    ]
    tester.test('Multiple valid sorts with independent letters', lambda: topological_sort(arr), possible_results=[['A', 'B', 'C'], ['B', 'A', 'C']])

    arr = [
        {"val": "Cake", "prerequisites": ["Eggs"]},
        {"val": "Eggs", "prerequisites": []},
        {"val": "Omelet", "prerequisites": ["Eggs"]},
    ]
    tester.test('All ingredients depend on one base', lambda: topological_sort(arr), possible_results=[['Eggs', 'Cake', 'Omelet'], ['Eggs', 'Omelet', 'Cake']])

    arr = [
        {"val": "X", "prerequisites": []},
        {"val": "Y", "prerequisites": []},
        {"val": "Z", "prerequisites": []},
    ]
    tester.test('No prerequisites, all letters independent', lambda: topological_sort(arr), possible_results=[list(p) for p in permutations(['X', 'Y', 'Z'])])

    arr = [
        {"val": "Sauce", "prerequisites": ["Tomatoes"]},
        {"val": "Tomatoes", "prerequisites": ["Water"]},
        {"val": "Water", "prerequisites": []},
        {"val": "Salt", "prerequisites": ["Tomatoes"]},
    ]
    tester.test('Complex ingredient dependency structure', lambda: topological_sort(arr), possible_results=[['Water', 'Tomatoes', 'Sauce', 'Salt'], ['Water', 'Tomatoes', 'Salt', 'Sauce']])

    arr = [
        {"val": "Apple", "prerequisites": []},
        {"val": "Banana", "prerequisites": []},
        {"val": "Carrot", "prerequisites": []},
        {"val": "Dates", "prerequisites": []},
        {"val": "Eggplant", "prerequisites": []},
        {"val": "Fig", "prerequisites": []},
    ]
    tester.test('Large graph with independent ingredients', lambda: topological_sort(arr), possible_results=[list(p) for p in permutations(['Apple', 'Banana', 'Carrot', 'Dates', 'Eggplant', 'Fig'])])

    arr = [
        {"val": "Sugar", "prerequisites": ["Sugar"]},
    ]
    tester.test('Single ingredient with self-prerequisite (return empty array)', lambda: topological_sort(arr), [])

    tester.print_pass_percentage()

test_topological_sort()
