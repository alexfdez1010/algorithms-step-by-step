# AGENTS.md - Guide for AI Agents

This document provides comprehensive guidance for AI agents working with the **Algorithms Step-by-Step** repository. It explains the project structure, conventions, and best practices for adding new algorithms or modifying existing ones.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Repository Structure](#repository-structure)
3. [Key Files and Their Purposes](#key-files-and-their-purposes)
4. [Adding a New Algorithm](#adding-a-new-algorithm)
5. [Algorithm Implementation Patterns](#algorithm-implementation-patterns)
6. [Input/Output Conventions](#inputoutput-conventions)
7. [Validation and Random Generation](#validation-and-random-generation)
8. [Best Practices](#best-practices)
9. [Common Pitfalls](#common-pitfalls)

---

## Project Overview

**Algorithms Step-by-Step** is a Streamlit web application that visualizes algorithm execution with step-by-step explanations. The app:

- Accepts user input or generates random inputs
- Validates inputs before execution
- Yields step-by-step results using Python generators
- Renders results in Markdown with visualizations (graphs, tables, LaTeX)

**Tech Stack:**
- **Frontend:** Streamlit
- **Visualization:** Graphviz (for graphs), Markdown tables, LaTeX
- **Language:** Python 3

---

## Repository Structure

```
algorithms-step-by-step/
├── algorithms/              # Algorithm implementations (generators)
│   ├── __init__.py
│   ├── dijkstra.py
│   ├── edit_distance.py
│   ├── fibonacci.py
│   ├── floyd_warshall.py
│   ├── kruskal.py
│   └── prim.py
├── data_structures/         # Custom data structures (e.g., DisjointSetUnion)
│   ├── __init__.py
│   └── disjoint_set_union.py
├── descriptions/            # Markdown descriptions for each algorithm
│   ├── dijkstra.md
│   ├── edit_distance.md
│   ├── fibonacci.md
│   ├── floyd_warshall.md
│   ├── kruskal.md
│   └── prim.md
├── random_generators/       # Functions to generate random inputs
│   ├── __init__.py
│   ├── generator_graph.py
│   └── generator_string.py
├── utils/                   # Utility functions
│   ├── __init__.py
│   ├── draw_utils.py        # Graph visualization
│   ├── graph_utils.py       # Graph parsing and conversion
│   └── markdown_utils.py    # Markdown/LaTeX formatting
├── validations/             # Input validation functions
│   ├── __init__.py
│   ├── generic_algorithms.py
│   └── validate_graph.py
├── resources/               # Static resources (images, etc.)
├── app.py                   # Main Streamlit application
├── config.py                # Algorithm registry and configuration
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## Key Files and Their Purposes

### `config.py`
**Purpose:** Central registry for all algorithms. Each algorithm is configured with:
- `DESCRIPTION_FILE`: Markdown file describing the algorithm
- `FUNCTION`: The algorithm implementation (generator function)
- `RANDOM_GENERATE_FUNCTION`: Function to generate random inputs (optional)
- `RANDOM_INPUT_PARAMETERS`: Parameters for random generation UI
- `RANDOM_PARAMETERS`: Fixed parameters passed to random generator
- `VALIDATION_INPUT_FUNCTION`: Function to validate user input
- `VALIDATION_PARAMETERS`: Parameters for validation
- `VALIDATION_RANDOM_PARAMETERS_FUNCTION`: Validates random parameters

**Structure:**
```python
ALGORITHMS: Dict[str, Dict[str, Dict[str, Any]]] = {
    "Category Name": {
        "Algorithm Name": {
            DESCRIPTION_FILE: "filename.md",
            FUNCTION: algorithm_function,
            RANDOM_INPUT_PARAMETERS: {...},
            VALIDATION_RANDOM_PARAMETERS_FUNCTION: validation_func,
            RANDOM_PARAMETERS: {...},
            RANDOM_GENERATE_FUNCTION: random_func,
            VALIDATION_PARAMETERS: {...},
            VALIDATION_INPUT_FUNCTION: validation_func
        }
    }
}
```

### `app.py`
**Purpose:** Main Streamlit application. Handles:
- Sidebar navigation (category and algorithm selection)
- Input collection (manual or random)
- Validation
- Rendering algorithm results

**Key Function:** `render_solution(function, input_text)` - Executes the algorithm generator and renders each yielded item.

### Algorithm Files (`algorithms/*.py`)
**Purpose:** Implement algorithms as **generator functions** that yield step-by-step results.

**Pattern:**
```python
def algorithm_name(input_string: str) -> Union[str, Graph, Digraph]:
    """
    Algorithm description
    :param input_string: Input format description
    :return: Generator yielding strings, graphs, or other renderable objects
    """
    # Parse input
    # Initialize data structures
    # Yield initial state
    # Iterate and yield steps
    # Yield final result
```

### Description Files (`descriptions/*.md`)
**Purpose:** Explain the algorithm in Markdown format. Should include:
- Algorithm overview
- How it works
- Time/space complexity
- Input format specification

### Validation Files (`validations/*.py`)
**Purpose:** Validate user inputs and random parameters.

**Return Type:** `Tuple[bool, Optional[str]]`
- `(True, None)` if valid
- `(False, "Error message")` if invalid

### Random Generator Files (`random_generators/*.py`)
**Purpose:** Generate random inputs for testing.

**Return Type:** `str` - Formatted input string

---

## Adding a New Algorithm

Follow these steps to add a new algorithm:

### 1. Create the Algorithm Implementation

**File:** `algorithms/your_algorithm.py`

```python
from typing import Union
from utils.markdown_utils import markdown_table  # If needed

def your_algorithm(input_string: str) -> Union[str, ...]:
    """
    Brief description
    :param input_string: Input format
    :return: Generator yielding steps
    """
    # Parse input
    lines = input_string.splitlines()
    
    # Initialize
    yield "## Algorithm Name Resolution"
    yield "Initial state description"
    
    # Main algorithm loop
    for step in range(...):
        yield f"### Step {step + 1}"
        yield "Step description"
        # Yield visualizations (tables, graphs, etc.)
    
    # Final result
    yield "### Final Result"
    yield f"Result: {result}"
```

### 2. Create the Description File

**File:** `descriptions/your_algorithm.md`

```markdown
Brief description of the algorithm.

Explain how it works, its applications, and complexity.

## Input Format

Specify the exact input format expected.

Example:
```
line 1: parameters
line 2: data
...
```
```

### 3. Create Validation Function (if needed)

**File:** `validations/validate_your_input.py` or add to existing file

```python
from typing import Tuple, Optional

def validate_your_input(input_string: str, **kwargs) -> Tuple[bool, Optional[str]]:
    """
    Validates the input
    :param input_string: The input to validate
    :return: (True, None) if valid, (False, error_message) if invalid
    """
    lines = input_string.splitlines()
    
    # Validation logic
    if not valid:
        return False, "Error message"
    
    return True, None
```

### 4. Create Random Generator (optional)

**File:** `random_generators/generator_your_type.py` or add to existing file

```python
def random_your_input(param1: int, param2: int, **kwargs) -> str:
    """
    Generates random input
    :param param1: Description
    :param param2: Description
    :return: Formatted input string
    """
    # Generate random data
    output = f"{param1} {param2}\n"
    # ... more lines
    return output
```

### 5. Register in `config.py`

Add to the appropriate category in the `ALGORITHMS` dictionary:

```python
from algorithms.your_algorithm import your_algorithm
from validations.validate_your_input import validate_your_input
from random_generators.generator_your_type import random_your_input

ALGORITHMS = {
    "Category Name": {
        "Your Algorithm Name": {
            DESCRIPTION_FILE: "your_algorithm.md",
            FUNCTION: your_algorithm,
            RANDOM_INPUT_PARAMETERS: {
                "param1": [ParameterType.INT, min_val, max_val],
                "param2": [ParameterType.INT, min_val, max_val]
            },
            VALIDATION_RANDOM_PARAMETERS_FUNCTION: None,  # or validation function
            RANDOM_PARAMETERS: {},  # Fixed parameters
            RANDOM_GENERATE_FUNCTION: random_your_input,  # or None
            VALIDATION_PARAMETERS: {},  # Parameters for validation
            VALIDATION_INPUT_FUNCTION: validate_your_input
        }
    }
}
```

### 6. Update `README.md`

Add your algorithm to the list:

```markdown
## Algorithms

- [Your Algorithm](descriptions/your_algorithm.md)
```

---

## Algorithm Implementation Patterns

### Pattern 1: Dynamic Programming (e.g., Edit Distance)

```python
def dp_algorithm(input_string: str) -> str:
    # Parse input
    lines = input_string.splitlines()
    
    # Initialize DP table
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    # Base cases
    yield "Base cases initialized"
    yield markdown_table(dp, headers_rows, headers_columns)
    
    # Fill DP table
    for i in range(1, n + 1):
        yield f"### Step {i}"
        for j in range(1, m + 1):
            # DP recurrence
            dp[i][j] = ...
        yield markdown_table(dp, headers_rows, headers_columns)
    
    # Final result
    yield f"Result: {dp[n][m]}"
```

### Pattern 2: Graph Algorithms (e.g., Dijkstra, Kruskal)

```python
from utils.graph_utils import input_to_adjacency_list, adjacency_list_to_list_of_edges
from utils.draw_utils import draw_graph

def graph_algorithm(input_string: str) -> Union[str, Graph]:
    # Parse graph
    graph = input_to_adjacency_list(input_string, directed=False, weighted=True)
    edge_list = adjacency_list_to_list_of_edges(graph)
    
    # Show initial graph
    yield "## Algorithm Resolution"
    yield "Initial graph:"
    yield draw_graph(len(graph), edge_list, weighted=True, directed=False)
    
    # Algorithm steps
    for step in ...:
        yield f"### Step {step}"
        yield "Description"
        yield draw_graph(len(graph), edge_list, edges_selected=selected_edges)
    
    # Final result
    yield "### Final Result"
    yield draw_graph(len(graph), edge_list, edges_selected=final_edges)
```

### Pattern 3: Iterative Algorithms (e.g., Fibonacci)

```python
def iterative_algorithm(input_string: str) -> str:
    n = int(input_string.strip())
    
    yield "## Algorithm Resolution"
    
    for i in range(n):
        yield f"### Iteration {i + 1}"
        # Computation
        yield f"Result: {result}"
    
    yield f"### Final Result: {final_result}"
```

---

## Input/Output Conventions

### Input Formats

#### Graph Input (Weighted, Directed/Undirected)
```
n m
u1 v1 w1
u2 v2 w2
...
um vm wm
```
- `n`: number of nodes (0-indexed)
- `m`: number of edges
- `ui vi wi`: edge from node `ui` to `vi` with weight `wi`

#### Graph with Source Vertex
```
n m
u1 v1 w1
...
um vm wm
source
```

#### Two Strings
```
string1
string2
```

#### Single Integer
```
n
```

### Output (Yielded Items)

Algorithms yield items that are rendered by Streamlit:

1. **Strings:** Rendered as Markdown
   - Use `#`, `##`, `###` for headings
   - Use `**bold**`, `*italic*`
   - Use code blocks with triple backticks

2. **Graphviz Objects:** Rendered as graph visualizations
   - `Graph` (undirected)
   - `Digraph` (directed)

3. **Tables:** Use `markdown_table()` from `utils.markdown_utils`

4. **LaTeX:** Use `latex_to_markdown()` for math expressions

---

## Validation and Random Generation

### Validation Best Practices

1. **Check input structure first** (number of lines, format)
2. **Validate data types** (integers, floats)
3. **Check constraints** (ranges, relationships)
4. **Return descriptive error messages**

Example:
```python
def validate_input(input_string: str) -> Tuple[bool, Optional[str]]:
    lines = input_string.splitlines()
    
    if len(lines) == 0:
        return False, "Input cannot be empty"
    
    if len(lines[0].split()) != 2:
        return False, "First line must contain two integers"
    
    try:
        n, m = map(int, lines[0].split())
    except ValueError:
        return False, "First line must contain integers"
    
    if n < 1:
        return False, "n must be at least 1"
    
    return True, None
```

### Random Generation Best Practices

1. **Use appropriate ranges** for parameters
2. **Ensure generated inputs are valid**
3. **For graphs:** Ensure connectivity if required
4. **Return formatted string** matching expected input format

Example:
```python
def random_input(n: int, m: int) -> str:
    output = f"{n} {m}\n"
    for i in range(m):
        # Generate random data
        output += f"{data}\n"
    return output
```

---

## Best Practices

### Code Style

1. **Use type hints** for function parameters and return types
2. **Write docstrings** for all functions (Google/NumPy style)
3. **Follow PEP 8** naming conventions
4. **Use meaningful variable names**

### Algorithm Implementation

1. **Always use generators** (`yield` instead of `return`)
2. **Yield descriptive text** at each step
3. **Use Markdown formatting** for structure (headings, lists)
4. **Visualize state** whenever possible (tables, graphs)
5. **Explain what's happening** in each step
6. **Show final result** clearly

### Testing

1. **Test with manual inputs** first
2. **Test with random inputs** to catch edge cases
3. **Verify visualizations** render correctly
4. **Check error messages** are helpful

### Documentation

1. **Describe input format** precisely in the description file
2. **Include examples** in descriptions
3. **Explain algorithm complexity** (time/space)
4. **Document any special requirements**

---

## Common Pitfalls

### 1. Not Using Generators
❌ **Wrong:**
```python
def algorithm(input_string: str) -> List[str]:
    results = []
    results.append("Step 1")
    return results
```

✅ **Correct:**
```python
def algorithm(input_string: str) -> str:
    yield "Step 1"
```

### 2. Incorrect Input Parsing
❌ **Wrong:**
```python
n, m = input_string.split()  # Doesn't handle multiline input
```

✅ **Correct:**
```python
lines = input_string.splitlines()
n, m = map(int, lines[0].split())
```

### 3. Missing Type Hints
❌ **Wrong:**
```python
def algorithm(input_string):
    ...
```

✅ **Correct:**
```python
def algorithm(input_string: str) -> Union[str, Graph]:
    ...
```

### 4. Not Validating Inputs
❌ **Wrong:**
```python
n = int(input_string)  # May crash on invalid input
```

✅ **Correct:**
```python
# In validation function
try:
    n = int(input_string)
except ValueError:
    return False, "Input must be an integer"
```

### 5. Forgetting to Register in config.py
Always add your algorithm to `ALGORITHMS` dictionary in `config.py`, otherwise it won't appear in the UI.

### 6. Inconsistent Input Format
Ensure your algorithm, validation, and description all agree on the exact input format.

### 7. Not Yielding Enough Information
Yield intermediate steps, not just the final result. The goal is to show the algorithm's execution step-by-step.

---

## Quick Reference

### Adding a New Algorithm Checklist

- [ ] Create `algorithms/your_algorithm.py` with generator function
- [ ] Create `descriptions/your_algorithm.md` with explanation
- [ ] Create validation function (if needed)
- [ ] Create random generator (if needed)
- [ ] Add imports to `config.py`
- [ ] Register algorithm in `ALGORITHMS` dictionary in `config.py`
- [ ] Update `README.md` with algorithm link
- [ ] Test with manual input
- [ ] Test with random input (if applicable)
- [ ] Verify visualizations render correctly

### Useful Utility Functions

```python
# Graph utilities
from utils.graph_utils import (
    input_to_adjacency_list,
    input_to_adjacency_matrix,
    adjacency_list_to_list_of_edges
)

# Drawing utilities
from utils.draw_utils import (
    draw_graph,
    draw_disjoint_sets
)

# Markdown utilities
from utils.markdown_utils import (
    markdown_table,
    latex_to_markdown,
    matrix_to_markdown
)
```

### Parameter Types in config.py

```python
from config import ParameterType

ParameterType.INT      # Integer input
ParameterType.FLOAT    # Float input
ParameterType.STRING   # String input
ParameterType.BOOLEAN  # Boolean input
```

---

## Example: Complete Algorithm Addition

See `algorithms/edit_distance.py` for a simple example, or `algorithms/kruskal.py` for a more complex graph algorithm example.

---

## Support

For questions or issues:
1. Check existing algorithm implementations for patterns
2. Review this guide
3. Open an issue on GitHub

---

**Last Updated:** 2024
**Maintained by:** Repository contributors
