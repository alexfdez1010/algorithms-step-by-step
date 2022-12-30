# Algorithms step-by-step

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://algorithms-step-by-step.streamlit.app)

A web app that automatically solves algorithms with step-by-step explanations.

The algorithms are implemented in Python and the explanations are written in Markdown.
Additionally, for drawing the graphs, the [Graphviz](https://graphviz.org/) library is used.

The input for the algorithms is specified by the user in the web app. Also, the input can be generated randomly.

## Algorithms

- [Dijkstra's algorithm](descriptions/dijkstra.md)
- [Kruskal's algorithm](descriptions/kruskal.md)
- [Prim's algorithm](descriptions/prim.md)
- [Floyd-Warshall algorithm](descriptions/floyd_warshall.md)
- [Fibonacci with matrix exponentiation](descriptions/fibonacci.md)
- [Edit distance](descriptions/edit_distance.md)

## Setup

1. Clone the repository:

```bash
https://github.com/alexfdez1010/streamlit_algorithms.git
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

## Contributing

If you want to contribute to this project, you can do it in two ways:

- **Adding a new algorithm**: you can add a new algorithm by creating a new file in the `algorithms` folder
  and adding the algorithm's description in the `descriptions` folder. You will also to configure the algorithm in
  the `config.py` file.
  You may want to take a look at the existing algorithms to see how they are implemented.
- **Improving the explanations**: you can improve the explanations by editing the algorithms already implemented.

In either case, you can create a pull request and I will review it as soon as possible.

## Bugs

If you find any bug, please open an issue in this repository and I will try to fix it as soon as possible.
If you want to fix it yourself, you can also create a pull request. In any case, I will be very grateful for your help.

