import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test_utils import Tester

def bfs(graph, start):
    visited = set()
    queue = [start]
    result = []
    while len(queue):
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            result.append(node)
            for nei in graph[node]:
                queue.append(nei)
    return result
    

# ============== TESTS ==============

def test_bfs():
    tester = Tester()
    
    undirected_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    tester.test_multiple_possibilities('Graph with multiple possibilities starting at node A', lambda: bfs(undirected_graph, 'A'), [
        ['A', 'B', 'C', 'D', 'E', 'F'], 
        ['A', 'B', 'C', 'D', 'F', 'E'],
        ['A', 'B', 'C', 'E', 'D', 'F'],
        ['A', 'B', 'C', 'E', 'F', 'D'],
        ['A', 'B', 'C', 'F', 'D', 'E'],
        ['A', 'B', 'C', 'F', 'E', 'D'],
        ['A', 'C', 'B', 'D', 'E', 'F'],
        ['A', 'C', 'B', 'D', 'F', 'E'],
        ['A', 'C', 'B', 'E', 'D', 'F'],
        ['A', 'C', 'B', 'E', 'F', 'D'],
        ['A', 'C', 'B', 'F', 'D', 'E'],
        ['A', 'C', 'B', 'F', 'E', 'D']
    ])
    tester.test_multiple_possibilities('Graph with multiple possibilities starting at node D', lambda: bfs(undirected_graph, 'D'), [
        ['D', 'B', 'A', 'E', 'C', 'F'],
        ['D', 'B', 'A', 'E', 'C', 'F'],
        ['D', 'B', 'E', 'A', 'F', 'C'],
        ['D', 'B', 'E', 'A', 'F', 'C']
    ])
    tester.test('Single node', lambda: bfs({'S': []}, 'S'), ['S'])
    linear_directed_graph = {
        'S': ['M'],
        'M': ['A'],
        'A': ['R'],
        'R': ['T'],
        'T': ['!'],
        '!': []
    }
    tester.test('Directed graph with only one possible path', lambda: bfs(linear_directed_graph, 'S'), ['S', 'M', 'A', 'R', 'T', '!'])
    tester.test('Directed graph with only one possible path and unreachable verticies', lambda: bfs(linear_directed_graph, 'R'), ['R', 'T', '!'])
    directed_graph = {
        'S': ['B', 'D'],
        'A': ['S'],
        'B': ['C'],
        'C': ['S'],
        'D': ['A']
    }
    tester.test_multiple_possibilities('Directed graph with multiple possibilities starting from node S', lambda: bfs(directed_graph, 'S'), [
        ['S', 'B', 'D', 'A', 'C'],
        ['S', 'B', 'D', 'C', 'A'],
        ['S', 'D', 'B', 'A', 'C'],
        ['S', 'D', 'B', 'C', 'A']
    ])
    tester.test('Directed graph with multiple possibilities starting from node D', lambda: bfs(directed_graph, 'D'), ['D', 'A', 'S', 'B', 'C'])

    tester.print_pass_percentage()

test_bfs()
