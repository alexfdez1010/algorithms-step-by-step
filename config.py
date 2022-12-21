from enum import Enum
from typing import Dict, Any


from algorithms.prim import prim_algorithm
from random_generators.generator_graph import random_adjacency_list_only_one_component
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
    INT = "int"
    FLOAT = "float"
    STRING = "string"
    BOOLEAN = "boolean"


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
        RANDOM_GENERATE_FUNCTION: random_adjacency_list_only_one_component,
        VALIDATION_PARAMETERS: {
            "directed": False,
            "weighted": True
        },
        VALIDATION_INPUT_FUNCTION: validate_only_one_component
    }
}
