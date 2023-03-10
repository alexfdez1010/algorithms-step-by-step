from enum import Enum
from typing import Dict, Any

from algorithms.dijkstra import dijkstra
from algorithms.edit_distance import edit_distance
from algorithms.fibonacci import fibonacci
from algorithms.floyd_warshall import floyd_warshall
from algorithms.kruskal import kruskal_algorithm
from algorithms.prim import prim_algorithm
from random_generators.generator_graph import random_graph_only_one_component, random_graph, \
    random_graph_with_source_vertex
from random_generators.generator_string import generate_two_words
from validations.generic_algorithms import only_one_parameter_positive_number, two_strings
from validations.validate_graph import validate_only_one_component, validate_number_of_edges, validate_graph, \
    validate_graph_with_source_vertex

DESCRIPTIONS_DIR = "descriptions"
DESCRIPTION_FILE = "description_file"
FUNCTION = "function"
RANDOM_GENERATE_FUNCTION = "random_function"
RANDOM_INPUT_PARAMETERS = "random_input_parameters"
RANDOM_PARAMETERS = "random_parameters"
VALIDATION_INPUT_FUNCTION = "validation_input"
VALIDATION_PARAMETERS = "validation_parameters"
VALIDATION_RANDOM_PARAMETERS_FUNCTION = "validation_random_parameters"


class ParameterType(Enum):
    """
    Enum for the type of the parameter
    """
    INT = "int"
    FLOAT = "float"
    STRING = "string"
    BOOLEAN = "boolean"


"""
This is the dictionary that contains all the information about the algorithms
The key is the name of the algorithm
The value is a dictionary that contains the following keys:
    - DESCRIPTION_FILE: the name of the file that contains the description of the algorithm
    - FUNCTION: the function that implements the algorithm
    - RANDOM_INPUT_PARAMETERS: the parameters of the random input function
    - VALIDATION_RANDOM_PARAMETERS_FUNCTION: the function that validates the random parameters
    - RANDOM_PARAMETERS: the parameters of the random input
    - RANDOM_GENERATE_FUNCTION: the function that generates a random input for the algorithm
    - VALIDATION_PARAMETERS: the parameters of the validation function
    - VALIDATION_INPUT_FUNCTION: the function that validates the input
"""
ALGORITHMS: Dict[str, Dict[str, Dict[str, Any]]] = {
    "Graphs": {
        "Prim's Algorithm": {
            DESCRIPTION_FILE: "prim.md",
            FUNCTION: prim_algorithm,
            RANDOM_INPUT_PARAMETERS: {
                "n": [ParameterType.INT, 3, 20],
                "m": [ParameterType.INT, 2, 40]
            },
            VALIDATION_RANDOM_PARAMETERS_FUNCTION: validate_number_of_edges,
            RANDOM_PARAMETERS: {
                "weighted": True,
                "directed": False
            },
            RANDOM_GENERATE_FUNCTION: random_graph_only_one_component,
            VALIDATION_PARAMETERS: {
                "directed": False,
                "weighted": True
            },
            VALIDATION_INPUT_FUNCTION: validate_only_one_component
        },
        "Kruskal's Algorithm": {
            DESCRIPTION_FILE: "kruskal.md",
            FUNCTION: kruskal_algorithm,
            RANDOM_INPUT_PARAMETERS: {
                "n": [ParameterType.INT, 3, 20],
                "m": [ParameterType.INT, 2, 40]
            },
            VALIDATION_RANDOM_PARAMETERS_FUNCTION: validate_number_of_edges,
            RANDOM_PARAMETERS: {
                "weighted": True,
                "directed": False
            },
            RANDOM_GENERATE_FUNCTION: random_graph_only_one_component,
            VALIDATION_PARAMETERS: {
                "directed": False,
                "weighted": True
            },
            VALIDATION_INPUT_FUNCTION: validate_only_one_component
        },
        "Floyd-Warshall Algorithm": {
            DESCRIPTION_FILE: "floyd_warshall.md",
            FUNCTION: floyd_warshall,
            RANDOM_INPUT_PARAMETERS: {
                "n": [ParameterType.INT, 5, 30],
                "m": [ParameterType.INT, 6, 50]
            },
            VALIDATION_RANDOM_PARAMETERS_FUNCTION: validate_number_of_edges,
            RANDOM_PARAMETERS: {
                "weighted": True,
                "directed": True
            },
            RANDOM_GENERATE_FUNCTION: random_graph,
            VALIDATION_PARAMETERS: {
                "directed": True,
                "weighted": True
            },
            VALIDATION_INPUT_FUNCTION: validate_graph
        },
        "Dijkstra's Algorithm": {
            DESCRIPTION_FILE: "dijkstra.md",
            FUNCTION: dijkstra,
            RANDOM_INPUT_PARAMETERS: {
                "n": [ParameterType.INT, 5, 30],
                "m": [ParameterType.INT, 6, 50]
            },
            VALIDATION_RANDOM_PARAMETERS_FUNCTION: validate_number_of_edges,
            RANDOM_PARAMETERS: {
                "weighted": True,
                "directed": False
            },
            RANDOM_GENERATE_FUNCTION: random_graph_with_source_vertex,
            VALIDATION_PARAMETERS: {
                "weighted": True
            },
            VALIDATION_INPUT_FUNCTION: validate_graph_with_source_vertex
        }
    },
    "Dynamic Programming": {
        "Edit Distance": {
            DESCRIPTION_FILE: "edit_distance.md",
            FUNCTION: edit_distance,
            RANDOM_INPUT_PARAMETERS: {
                "n": [ParameterType.INT, 5, 30],
                "m": [ParameterType.INT, 5, 30]
            },
            VALIDATION_RANDOM_PARAMETERS_FUNCTION: None,
            RANDOM_PARAMETERS: {},
            RANDOM_GENERATE_FUNCTION: generate_two_words,
            VALIDATION_PARAMETERS: {},
            VALIDATION_INPUT_FUNCTION: two_strings
        }
    },
    "Miscellaneous": {
        "Fibonacci using matrix exponentiation": {
            DESCRIPTION_FILE: "fibonacci.md",
            FUNCTION: fibonacci,
            RANDOM_INPUT_PARAMETERS: {},
            VALIDATION_RANDOM_PARAMETERS_FUNCTION: None,
            RANDOM_PARAMETERS: {},
            RANDOM_GENERATE_FUNCTION: None,
            VALIDATION_PARAMETERS: {},
            VALIDATION_INPUT_FUNCTION: only_one_parameter_positive_number
        }
    }
}
