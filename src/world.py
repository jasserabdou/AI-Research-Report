from typing import List, Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value = value


class Edge:
    def __init__(self, node1: Node, node2: Node) -> None:
        self.node1 = node1
        self.node2 = node2


class Graph:
    """
    A class representing a graph.

    Attributes:
        nodes (List[Node]): A list of nodes in the graph.
        edges (List[Edge]): A list of edges in the graph.
    """

    def __init__(self) -> None:
        self.nodes: List[Node] = []
        self.edges: List[Edge] = []

    def add_node(self, value: int) -> None:
        """
        Adds a new node to the graph.

        Args:
            value (int): The value of the new node.
        """
        node = Node(value)
        self.nodes.append(node)

    def add_edge(self, value1: int, value2: int) -> None:
        """
        Adds a new edge to the graph.

        Args:
            value1 (int): The value of the first node.
            value2 (int): The value of the second node.
        """
        node1 = self.find_node(value1)
        node2 = self.find_node(value2)
        edge = Edge(node1, node2)
        self.edges.append(edge)

    def find_node(self, value: int) -> Optional[Node]:
        """
        Finds a node in the graph by its value.

        Args:
            value (int): The value of the node to find.

        Returns:
            Optional[Node]: The found node, or None if not found.
        """
        for node in self.nodes:
            if node.value == value:
                return node
        return None
