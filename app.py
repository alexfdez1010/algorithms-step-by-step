from typing import List, Union

import streamlit as st
from graphviz import Graph

from config import *

IMAGE_SIDEBAR = "resources/sidebar.png"

MENU_ITEMS = {
    "About": "https://github.com/alexfdez1010/streamlit_algorithms",
    "Report a bug": "https://github.com/alexfdez1010/streamlit_algorithms/issues"
}


def parameter_input(parameter_name: str, parameter_information: List[Any]) -> Any:
    """
    Render a parameter input based on the information provided

    :param parameter_name: Name of the parameter
    :param parameter_information: Information about the parameter

    :return: The value of the parameter
    """
    parameter_type = parameter_information[0]

    if parameter_type in (ParameterType.INT, ParameterType.FLOAT):

        min_value = parameter_information[1]
        max_value = parameter_information[2]

        return st.number_input(parameter_name, min_value=min_value, max_value=max_value)

    elif parameter_type == ParameterType.STRING:
        return st.text_input(parameter_name)

    elif parameter_type == ParameterType.BOOLEAN:
        return st.checkbox(parameter_name)

    else:
        raise ValueError(f"Parameter type {parameter_type} is not supported")


def render_entry(entry: Union[str, Graph]):
    """
    Render an entry of the algorithm

    :param entry: Entry to render
    """
    if isinstance(entry, str):
        st.markdown(entry)
    else:
        st.graphviz_chart(entry, use_container_width=True)


def render_solution(algorithm_function, input_text: str):
    """
    Render the solution of the algorithm

    :param algorithm_function: Function to run the algorithm
    :param input_text: Input of the algorithm
    """
    for entry in algorithm_function(input_text):
        render_entry(entry)


def create_sidebar():
    """
    Create the sidebar of the application

    :return: The name and the information of the selected algorithm from the sidebar
    """

    with st.sidebar:
        st.image(IMAGE_SIDEBAR)
        st.title("Algorithms")
        category_names = ALGORITHMS.keys()
        category_selection = st.selectbox("Select a category", category_names)

        algorithm_names = ALGORITHMS[category_selection].keys()
        algorithm_selection = st.selectbox(
            "Select an algorithm",
            algorithm_names
        )

    return algorithm_selection, ALGORITHMS[category_selection][algorithm_selection]


def main():
    """
    Main function of the application
    """
    st.set_page_config(
        page_title="Algorithms step-by-step",
        page_icon=":hourglass_flowing_sand:",
        layout="wide",
        menu_items=MENU_ITEMS,
    )

    algorithm_selection, algorithm_information = create_sidebar()

    st.title(algorithm_selection)
    description = open(f"{DESCRIPTIONS_DIR}/{algorithm_information[DESCRIPTION_FILE]}", "r").read()
    st.markdown(description)

    if algorithm_information[RANDOM_GENERATE_FUNCTION] is not None:
        random_generated = st.checkbox("Generate random input")
    else:
        random_generated = False

    parameters = {}

    if random_generated:
        parameters_information: Dict[str, List] = algorithm_information[RANDOM_INPUT_PARAMETERS]
        parameters = {name: parameter_input(name, information) for name, information in parameters_information.items()}
        all_parameters = {**parameters, **algorithm_information[RANDOM_PARAMETERS]}

        input_text = algorithm_information[RANDOM_GENERATE_FUNCTION](**all_parameters)

    else:
        input_text = st.text_area("Input of the algorithm", height=300)

    if not st.button("Run algorithm"):
        return

    function = algorithm_information[FUNCTION]

    if random_generated:

        validation_function = algorithm_information.get(VALIDATION_RANDOM_PARAMETERS_FUNCTION, None)
        is_correct, message = (True, None) if validation_function is None else validation_function(**parameters)

    else:
        validation_function = algorithm_information.get(VALIDATION_INPUT_FUNCTION, None)
        validation_parameters = algorithm_information.get(VALIDATION_PARAMETERS, {})

        is_correct, message = (True, None) \
            if validation_function is None else validation_function(input_text, **validation_parameters)
    if is_correct:
        render_solution(function, input_text)
    else:
        st.error(message)


if __name__ == "__main__":
    main()
