import heapq
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from test_utils import Tester

def dijkstra(graph, start):
    priority_queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
    'E': [],
}



# ============== TESTS ==============

def test_dijkstra():
    tester = Tester()
    
    directed_graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)],
        'E': [],
    }
    tester.test('Directed graph starting at A', lambda: dijkstra(directed_graph, 'A'), {'A': 0, 'B': 1, 'C': 3, 'D': 4, 'E': float('inf')})
    tester.test('Directed graph starting at B', lambda: dijkstra(directed_graph, 'B'), {'A': 1, 'B': 0, 'C': 2, 'D': 3, 'E': float('inf')})
    tester.test('Directed graph starting at isolated node E', lambda: dijkstra(directed_graph, 'E'), {'A': float('inf'), 'B': float('inf'), 'C': float('inf'), 'D': float('inf'), 'E': 0})
    
    directed_graph2 = {
        'X': [('Y', 3), ('Z', 7)],
        'Y': [('Z', 1), ('W', 5)],
        'Z': [('W', 2)],
        'W': [],
        'V': [('X', 4)]
    }

    tester.test('Directed graph starting at X', lambda: dijkstra(directed_graph2, 'X'), {'X': 0, 'Y': 3, 'Z': 4, 'W': 6, 'V': float('inf')})
    tester.test('Directed graph starting at Y', lambda: dijkstra(directed_graph2, 'Y'), {'X': float('inf'), 'Y': 0, 'Z': 1, 'W': 3, 'V': float('inf')})
    tester.test('Directed graph starting at isolated node V', lambda: dijkstra(directed_graph2, 'V'), {'X': 4, 'Y': 7, 'Z': 8, 'W': 10, 'V': 0})

    undirected_graph = {
        'A': [('B', 2), ('C', 5)],
        'B': [('A', 2), ('C', 1), ('D', 3)],
        'C': [('A', 5), ('B', 1), ('D', 2)],
        'D': [('B', 3), ('C', 2), ('E', 4)],
        'E': [('D', 4)]
    }
    tester.test('Undirected graph starting at A', lambda: dijkstra(undirected_graph, 'A'), {'A': 0, 'B': 2, 'C': 3, 'D': 5, 'E': 9})
    tester.test('Undirected graph starting at C', lambda: dijkstra(undirected_graph, 'C'), {'A': 3, 'B': 1, 'C': 0, 'D': 2, 'E': 6})
    tester.test('Undirected graph starting at E', lambda: dijkstra(undirected_graph, 'E'), {'A': 9, 'B': 7, 'C': 6, 'D': 4, 'E': 0})
    

    tester.print_pass_percentage()

test_dijkstra()

