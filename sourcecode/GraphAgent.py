import random
import networkx as nx
from typing import Any, Dict, List


class GraphAgent:
    """
    A class representing an agent that performs actions on a graph.

    Attributes:
        start (Any): The starting node of the agent.
        target (Any): The target node that the agent wants to reach.
        graph (nx.Graph): The graph on which the agent performs actions.
        shortest_paths (Dict[Any, Dict[Any, List[Any]]]): A dictionary containing the shortest paths between nodes.

    Methods:
        random_walk: Performs a random walk on the graph until the target node is reached.
        shortest_path: Moves along the shortest path from the start node to the target node.
        sense_and_store: Stores the current node in the agent's memory.
        get_episode_memory: Returns the memory of the agent, which contains the visited nodes.
        calculate_shortest_paths: Calculates the shortest paths between all pairs of nodes in the graph.
    """

    def __init__(
        self,
        start: Any,
        target: Any,
        graph: nx.Graph,
        shortest_paths: Dict[Any, Dict[Any, List[Any]]],
    ):
        self.start = start
        self.target = target
        self.graph = graph
        self.shortest_paths = shortest_paths
        self.current_node = start
        self.memory = []

    def random_walk(self):
        while self.current_node != self.target:
            neighbors = list(self.graph.neighbors(self.current_node))
            self.current_node = random.choice(neighbors)
            self.sense_and_store()

    def shortest_path(self):
        path = self.shortest_paths[self.start][self.target]
        for node in path:
            self.current_node = node
            self.sense_and_store()

    def sense_and_store(self):
        self.memory.append(self.current_node)

    def get_episode_memory(self) -> List[Any]:
        return self.memory

    def calculate_shortest_paths(self):
        shortest_paths = dict(nx.all_pairs_shortest_path(self.graph))
        return shortest_paths
