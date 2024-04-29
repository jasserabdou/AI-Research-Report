import networkx as nx
from typing import Dict


class GraphMetrics:
    """
    A class that calculates various centrality metrics for a given graph.

    Parameters:
    graph (networkx.Graph): The graph for which centrality metrics will be calculated.

    Methods:
    degree_centrality(): Calculates the degree centrality for each node in the graph.
    closeness_centrality(): Calculates the closeness centrality for each node in the graph.
    betweenness_centrality(): Calculates the betweenness centrality for each node in the graph.
    """

    def __init__(self, graph: nx.Graph):
        self.graph = graph

    def degree_centrality(self) -> Dict:
        """
        Calculates the degree centrality for each node in the graph.

        Returns:
        dict: A dictionary where the keys are the nodes and the values are their degree centrality scores.
        """
        return nx.degree_centrality(self.graph)

    def closeness_centrality(self) -> Dict:
        """
        Calculates the closeness centrality for each node in the graph.

        Returns:
        dict: A dictionary where the keys are the nodes and the values are their closeness centrality scores.
        """
        return nx.closeness_centrality(self.graph)

    def betweenness_centrality(self) -> Dict:
        """
        Calculates the betweenness centrality for each node in the graph.

        Returns:
        dict: A dictionary where the keys are the nodes and the values are their betweenness centrality scores.
        """
        return nx.betweenness_centrality(self.graph)
