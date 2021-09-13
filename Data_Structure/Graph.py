def GraphArray():
    class Graph:
        def __init__(self):
            self.adj = dict()
            self.edges = 0
            self.nodes = 0

        def insertEdge(self, node1, node2):
            if node1 in self.adj.keys():
                self.adj[node1].append(node2)
            if node2 in self.adj.keys():
                self.adj[node2].append(node1)
            if node1 not in self.adj.keys():
                self.adj.update({node1: [node2]})
            if node2 not in self.adj.keys():
                self.adj.update({node2: [node1]})
            self.edges += 1
            self.nodes = len(self.adj.keys())

        def insertNode(self, node):
            nodes = [int(n) for n in input("Enter Connected Nodes: ").split(",")]
            for n in nodes:
                self.insertEdge(node, n)

        def removeEdge(self, node1, node2):
            if self.edges == 0:
                print("Empty Graph")
            else:
                self.adj[node1].remove(node2)
                self.adj[node2].remove(node1)
                self.edges -= 1

        def removeNode(self, node):
            if self.nodes == 0:
                print("Empty Graph")
            else:
                for n in self.adj[node]:
                    self.adj[n].remove(node)
                    self.edges -= 1
                self.adj.pop(node)
                self.nodes -= 1

        def DFS(self, v, visited):
            stack = [v]
            visited.add(v)
            while stack:
                v = stack.pop()
                print(v, end=' ')
                for visit in self.adj[v]:
                    if visit not in visited:
                        stack.append(visit)
                        visited.add(visit)

        def BFS(self, v, visited):
            queue = [v]
            visited.add(v)
            while queue:
                v = queue.pop(0)
                print(v, end=" ")
                for visit in self.adj[v]:
                    if visit not in visited:
                        queue.append(visit)
                        visited.add(visit)

        def Traversal(self, ch, v):
            if v not in self.adj.keys():
                print("Not Present")
                return

            visited = set()
            if ch == "DFS":
                print("DFS Traversal:")
                self.DFS(v, visited)
            elif ch == "BFS":
                print("BFS Traversal:")
                self.BFS(v, visited)
            print()



    g = Graph()
    g.insertEdge(1, 2)
    g.insertEdge(1, 3)
    g.insertEdge(2, 3)
    g.insertEdge(2, 4)
    g.insertEdge(2, 5)
    g.insertEdge(3, 5)
    g.insertEdge(4, 5)
    g.Traversal("DFS", 1)
    g.removeNode(5)
    g.Traversal("BFS", 1)
    g.insertNode(5)
    # print(g.adj, g.edges, g.nodes)
    # g.removeEdge(2, 5)
    # print(g.adj, g.edges, g.nodes)


GraphArray()

def GraphLL():
    class Node:
        def __init__(self, vertex):
            self.vertex = vertex
            self.next = None

    class Graph:
        def __init__(self):
            self.adj = list()
            self.edges = 0
            self.nodes = 0

        def insertEdge(self, v1, v2):
            node = Node(v2)
            node.next = self.adj[v1]
            self.adj[v1] = node

            node = Node(v1)
            node.next = self.adj[v2]
            self.adj[v2] = node
            self.edges += 1
            self.nodes = len(self.adj)

        def printLL(self):
            for node in self.adj:
                while node.next:
                    print(node.vertex, "->", end="")
                    node = node.next
                print()


    g = Graph()
    g.insertEdge(1, 2)
    g.insertEdge(1, 3)
    g.insertEdge(2, 3)
    g.insertEdge(2, 4)
    g.insertEdge(2, 5)
    g.insertEdge(3, 5)
    g.insertEdge(4, 5)
    g.printLL()

# GraphLL()

