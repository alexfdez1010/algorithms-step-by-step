from enum import Enum
from typing import Dict, Any

from algorithms.kruskal import kruskal_algorithm
from algorithms.prim import prim_algorithm
from random_generators.generator_graph import random_graph_only_one_component
from validations.validate_graph import validate_only_one_component, validate_number_of_edges

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
ALGORITHMS: Dict[str, Dict[str, Any]] = {
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
    }
}
