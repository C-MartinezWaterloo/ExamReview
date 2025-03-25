
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



if __name__ == '__main__':

    g = GraphAdjancencyList(0)

    g.add_node("YYZ")
    g.add_node("YYX")

    g.put_edge(0, 1)

    print(g.is_edge(0, 1))  # should print True
    print(g.is_edge(1, 0))  # should print False, unless you added a reverse edge

    g.nodes[0].print_list()



