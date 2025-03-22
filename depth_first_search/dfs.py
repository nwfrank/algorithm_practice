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
            stack.extend(reversed(graph[node]))  # Reverse to maintain order

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
    tester.test('Single node with no prerequisites', lambda: dfs(graph, 'A'), possible_results=[['A', 'B', 'D', 'E', 'F', 'C'], ['A', 'B', 'E', 'F', 'C', 'D'], ['A', 'C', 'F', 'E', 'B', 'D']])

    tester.print_pass_percentage()

test_dfs()
