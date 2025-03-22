import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_utils import Tester

def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(graph[node])

    return result



# ============== TESTS ==============

def test_dfs():
    tester = Tester()
    
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    tester.test_multiple_possibilities('Graph with multiple possibilities starting at node A', lambda: dfs(graph, 'A'), [['A', 'B', 'D', 'E', 'F', 'C'], ['A', 'B', 'E', 'F', 'C', 'D'], ['A', 'C', 'F', 'E', 'B', 'D']])
    tester.test_multiple_possibilities('Graph with multiple possibilities starting at node D', lambda: dfs(graph, 'D'), [['D', 'B', 'A', 'C', 'F', 'E'], ['D', 'B', 'E', 'F', 'C', 'A']])
    tester.test('Single node', lambda: dfs({'S': []}, 'S'), ['S'])

    tester.print_pass_percentage()

test_dfs()
