# Algorithm Practice

This project implements a collection of essential functions that every programmer should be familiar with.
The goal is for me to practice these functions and share them!

## Features

- A wide range of functions that cover topics such as searches.
- Each function is thoroughly tested using a custom unit tester to ensure correctness.
- Simple, clear, and reusable code for easy integration into your own projects.

## Functions

The functions included in this project are designed to help improve your programming skills. Some examples include:

- **Search algorithms**: [Binary Search](./binary_search/binary_search.py)
- **Sorting algorithms**: [Bubble Sort](./sorting_algorithms/bubble_sort.py), [Topological Sort](./topological_sort/topological_sort.py), [Merge Sort](./sorting_algorithms/merge_sort.py)
- **Graph algorithms**: [Depth First Search](./graph_algorithms/depth_first_search/dfs.py), [Breath First Search](./graph_algorithms/breath_first_search/bfs.py), [Dijkstra's Shortest Path](./graph_algorithms/dijkstras_shortest_path/dijkstra.py)

## Testing

This project includes a custom unit tester class, `Tester`, which is designed to simplify testing and checking the correctness of functions. It tracks the total number of tests, the number of tests passed, and prints the results of each test, including any error messages.

## How to Use

1. **Import the Tester**:
   Import the [Tester](./test_utils.py) from the needed path
2. **Create a Function to Test**:
   This example creates a simple add function
3. **Initialize the Tester Class**:
   Create an instance of the `Tester` class.
4. **Test the Function With `.test`**:
   Pass in a message, lambda function, and expected result
5. **Print the Pass Rate**:
   Display the pass rate is desired

   ```python
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from test_utils import Tester

   def add(a, b):
        return a + b

    tester = Tester()

    tester.test("Testing addition function", lambda: add(2, 3), 5)
    tester.test("Testing subtraction function", lambda: add(5, 3), 2)

    tester.print_pass_percentage()
   ```

## Installation

To use this project locally, clone the repository:

```bash
git clone https://github.com/nwfrank/algorithm_practice.git
cd algorithm_practice
```
