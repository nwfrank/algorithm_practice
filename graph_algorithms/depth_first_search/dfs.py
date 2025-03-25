import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
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
    
    undirected_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    tester.test_multiple_possibilities('Graph with multiple possibilities starting at node A', lambda: dfs(undirected_graph, 'A'), [['A', 'B', 'D', 'E', 'F', 'C'], ['A', 'B', 'E', 'F', 'C', 'D'], ['A', 'C', 'F', 'E', 'B', 'D']])
    tester.test_multiple_possibilities('Graph with multiple possibilities starting at node D', lambda: dfs(undirected_graph, 'D'), [['D', 'B', 'A', 'C', 'F', 'E'], ['D', 'B', 'E', 'F', 'C', 'A']])
    tester.test('Single node', lambda: dfs({'S': []}, 'S'), ['S'])
    linear_directed_graph = {
        'S': ['M'],
        'M': ['A'],
        'A': ['R'],
        'R': ['T'],
        'T': ['!'],
        '!': []
    }
    tester.test('Directed graph with only one possible path', lambda: dfs(linear_directed_graph, 'S'), ['S', 'M', 'A', 'R', 'T', '!'])
    tester.test('Directed graph with only one possible path and unreachable verticies', lambda: dfs(linear_directed_graph, 'R'), ['R', 'T', '!'])
    directed_graph = {
        'S': ['B', 'D'],
        'A': ['S'],
        'B': ['C'],
        'C': ['S'],
        'D': ['A']
    }
    tester.test_multiple_possibilities('Directed graph with multiple possibilities starting from node S', lambda: dfs(directed_graph, 'S'), [['S', 'B', 'C', 'D', 'A'], ['S', 'D', 'A', 'B', 'C']])
    tester.test('Directed graph with multiple possibilities starting from node D', lambda: dfs(directed_graph, 'D'), ['D', 'A', 'S', 'B', 'C'])

    tester.print_pass_percentage()

test_dfs()
