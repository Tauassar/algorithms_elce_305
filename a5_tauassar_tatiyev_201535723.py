class Topological:
    # vertices in the graph
    vertices = []
    # dictionary of edges
    edges = {}

    def __init__(self, vertices, edges=None):
        self.vertices = [i for i in range(vertices+1)]
        # use set to store multiple connected unique values
        for i in self.vertices:
            self.edges[i] = set()
        if edges is not None:
            for i in edges:
                self.edges[i[0]].add(i[1])

    # add edge to the graph
    def add_edge(self, source, destination):
        self.edges[source].add(destination)

    # remove edge from the graph
    def remove_edge(self, source, destination):
        try:
            self.edges[source].remove(destination)
        except ValueError:
            print('Existing graph has no such nodes: ({0} {1})'.format(
                source, destination
            ))

    # Simple implementation of dfs
    def dfs(self, vertex, visited, stack):
        # Mark the current node as visited.
        visited.append(vertex)
        # Recursively call dfs to traverse graph
        for i in self.edges[vertex]:
            if i not in visited:
                self.dfs(i, visited, stack)
        # add current vertex to stack
        stack.append(vertex)

    # Actual topological sort algorithm
    def sort(self):
        # Mark all the vertices as not visited
        visited = []
        stack = []
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in self.vertices:
            if i not in visited:
                self.dfs(i, visited, stack)
        stack.reverse()
        print("Sorted graph: {0}".format(stack))
        return stack


# driver
def main():
    # initial setup of the graph
    edges = [
        [0, 1],
        [2, 3],
        [3, 4],
        [5, 3],
        [4, 1],
        [0, 2],
    ]
    # include 5 vertices and
    graph = Topological(5, edges)
    print('Initial DAG')
    graph.sort()
    print('(5, 2) added')
    graph.add_edge(5, 2)
    graph.sort()
    print('(5, 3) and (4, 1) removed')
    graph.remove_edge(5, 3)
    graph.remove_edge(4, 1)
    graph.sort()


if __name__ == "__main__":
    main()
