from collections import defaultdict

class GraphNode:
    def __init__(self, name, incoming, outgoing):
        self._name = name
        self._incoming = incoming
        self._outgoing = outgoing

    def name(self):
        return self._name


class UndirectedGraph:
    def __init__(self, v):
        self._v = v

    def vertices(self):
        pass


class GraphBuilder:
    def __init__(self):
        self._pending = defaultdict(lambda: set())
        self._undirectedEdges = []
        
    def addEdge(self, source, destination):
        self._adjacencies[source].add(destination)

    def undirectedGraph(self):
        pass

        
