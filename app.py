from typing import Any, List, Dict, Union

import streamlit as st
from graphviz import Graph

from config import ALGORITHMS, RANDOM_INPUT_PARAMETERS, ParameterType, FUNCTION, RANDOM_GENERATE_FUNCTION, \
    DESCRIPTION_FILE, DESCRIPTIONS_DIR, VALIDATION_INPUT_FUNCTION, RANDOM_PARAMETERS, VALIDATION_PARAMETERS, \
    VALIDATION_RANDOM_PARAMETERS_FUNCTION

IMAGE_SIDEBAR = "resources/sidebar.png"

MENU_ITEMS = {

}

st.set_page_config(
    page_title="Algorithms",
    page_icon=":book:",
    menu_items=MENU_ITEMS,
)


def parameter_input(parameter_name: str, parameter_information: List[Any]) -> Any:
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
    if isinstance(entry, str):
        st.markdown(entry)
    else:
        st.graphviz_chart(entry, use_container_width=True)

def render_solution(algorithm_function, input_text: str):
    for entry in algorithm_function(input_text):
        render_entry(entry)


def main():
    with st.sidebar:
        st.image(IMAGE_SIDEBAR)
        st.title("Algorithms")
        algorithm_names = ALGORITHMS.keys()
        algorithm_selection = st.selectbox(
            "Select an algorithm",
            algorithm_names,
            index=0
        )

    algorithm_information = ALGORITHMS[algorithm_selection]
    st.title(algorithm_selection)
    description = open(f"{DESCRIPTIONS_DIR}/{algorithm_information[DESCRIPTION_FILE]}", "r").read()
    st.markdown(description)
    random_generated = st.checkbox("Generate random input")

    parameters = {}

    if random_generated:

        parameters_information: Dict[str, List] = algorithm_information[RANDOM_INPUT_PARAMETERS]
        parameters = {name: parameter_input(name, information) for name, information in parameters_information.items()}
        all_parameters = {**parameters, **algorithm_information[RANDOM_PARAMETERS]}

        input_text = algorithm_information[RANDOM_GENERATE_FUNCTION](**all_parameters)

    else:
        input_text = st.text_area("Input of the algorithm", height=500)

    if st.button("Run algorithm"):

        function = algorithm_information[FUNCTION]

        if random_generated:

            validation_function = algorithm_information.get(VALIDATION_RANDOM_PARAMETERS_FUNCTION, None)
            is_correct, message = (True, None) if validation_function is None else validation_function(**parameters)

            if is_correct:
                render_solution(function, input_text)
            else:
                st.error(message)

        else:

            validation_function = algorithm_information.get(VALIDATION_INPUT_FUNCTION, None)
            validation_parameters = algorithm_information.get(VALIDATION_PARAMETERS, {})

            is_correct, message = (True, None) if validation_function is None else validation_function(input_text, **validation_parameters)

            if is_correct:
                render_solution(function, input_text)

            else:
                st.error(message)



if __name__ == "__main__":
    main()
