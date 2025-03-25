
import linked_list


class Graph:
    
    def __init__(self, num_nodes: int):
        self.adj_matrix = np.zeros((num_nodes, num_nodes))

    def is_edge(self, i: int, j: int):
        return self.adj_matrix[i][j] == 1

    def put_edge(self, i: int, j: int):
        self.adj_matrix[i][j] = 1

    def remove_edge(self, i: int, j: int):
        self.adj_matrix[i][j] = 0




class GraphAdjancencyList:

    def __init__(self, num_nodes):
        self.nodes = []
        self.node_names = {}
        self.node_names_rev = {}
        self.num_nodes = num_nodes
        for i in range(num_nodes):
            self.nodes.append(linked_list.LinkedList())
    
    def add_node(self, name):
        self.node_names[name] = len(self.nodes)
        self.node_names_rev[len(self.nodes)] = name
        self.nodes.append(linked_list.LinkedList())
        self.num_nodes += 1
    
    def is_edge_name(self, name1, name2):
        return self.is_edge(self.node_names[name1], self.node_names[name2])
    
    def is_edge(self, i, j):
        # self.nodes[i] list of the neighbours of node i
        return self.nodes[i].contains(j)

    def put_edge(self, i, j): # O(1)
        self.nodes[i].insert(0, j)

    def put_edge_name(self, name1, name2):
        self.put_edge(self.node_names[name1], self.node_names[name2])

    def remove_edge(self, i, j): # O(d)
        self.nodes[i].remove(j)
        # if user is allowed to call put_edge(1, 2) twice, need to either 
        # take care of it inside put_edge or inside remove_edge


    
def breadth_first_traversal(g, start_name):

    start_index = g.node_names[start_name]
    visited = [False] * g.num_nodes

    DS = linked_list.Queue()
    DS.add(start_index)

    while not DS.is_empty():
        cur = DS.get()
        if not visited[cur]:
            print(g.node_names_rev[cur])
            visited[cur] = True

            cur = g.nodes[cur].head

            while cur:
                if not visited[cur.data]:
                    DS.add(cur.data)
                cur = cur.next






if __name__ == '__main__':
    # g = Graph(4) # Graph.__init__(g, 4)
    # g.put_edge(1, 2) # Graph.put_edge(g, 1, 2)
    # print(g.is_edge(1, 2))



    # setting up a matrix
    # import numpy as np
    # M = np.array((10, 10)) # a 10x10 matrix
    # M = np.zeros((10, 10)) # an all-zero 10x10 matrix
    # M[0][1] # row 0, column 1

    airports = GraphAdjancencyList(0)
    airports.add_node("YYZ")
    airports.add_node("YVR")
    airports.add_node("JFK")
    
    airports.put_edge_name("YVR", "YYZ")
    airports.put_edge_name("YYZ", "YVR")
    airports.put_edge_name("YYZ", "JFK")
    

    breadth_first_traversal(airports, "YVR")
    #    YYZ
    #  / ^  \
    # v  /    v
    # YVR     JFK




