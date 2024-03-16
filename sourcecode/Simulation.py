from GraphAgent import GraphAgent
from world import Graph
from GraphMetrics import GraphMetrics
import random
import networkx as nx

# Constants
NUM_NODES = 5
NUM_SIMULATIONS = 1000

# Create a Graph object
graph = Graph()

# Add nodes
for i in range(1, NUM_NODES + 1):
    graph.add_node(i)

# Add edges
for i in range(1, NUM_NODES):
    graph.add_edge(i, i + 1)

# Convert graph to a networkx.Graph object
nx_graph = nx.Graph()
for node in graph.nodes:
    nx_graph.add_node(node.value)
for edge in graph.edges:
    nx_graph.add_edge(edge.node1.value, edge.node2.value)

# Calculate shortest paths
shortest_paths = dict(nx.all_pairs_shortest_path(nx_graph))


def run_simulation(start, target, graph, paths, is_random_walk):
    """
    Runs a simulation with the given parameters.

    Args:
        start: The starting node of the simulation.
        target: The target node of the simulation.
        graph: The graph representing the environment.
        paths: The available paths in the graph.
        is_random_walk: A boolean indicating whether to perform a random walk or find the shortest path.

    Returns:
        The episode memory of the agent after running the simulation.
    """
    agent = GraphAgent(start, target, graph, paths)
    if is_random_walk:
        agent.random_walk()
    else:
        agent.shortest_path()
    return agent.get_episode_memory()


# Run simulations
random_walk_results = [
    run_simulation(
        *random.sample(range(1, NUM_NODES + 1), 2), nx_graph, shortest_paths, True
    )
    for _ in range(NUM_SIMULATIONS)
]
shortest_path_results = [
    run_simulation(
        *random.sample(range(1, NUM_NODES + 1), 2), nx_graph, shortest_paths, False
    )
    for _ in range(NUM_SIMULATIONS)
]

# Print results
print("Random walk results:", random_walk_results)
print("Shortest path results:", shortest_path_results)


# Calculate metrics
metrics = GraphMetrics(nx_graph)


degree = metrics.degree_centrality()
closeness = metrics.closeness_centrality()
betweenness = metrics.betweenness_centrality()

print("Degree centrality:", degree)
print("Closeness centrality:", closeness)
print("Betweenness centrality:", betweenness)
