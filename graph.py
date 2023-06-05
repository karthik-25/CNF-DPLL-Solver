import sys

class GraphNode:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        
class Graph:
    def __init__(self):
        self.nodes = {}
        self.output_str = ""
        self.clause_list = []
        self.tree_build_fail_str = "Error: Graph build failed."
    
    def build_graph(self, input_file):
        with open(input_file, "r") as f:
            for line in f:
                if line == "\n" or "#" in line:
                    continue

                if ":" in line:
                    self.process_line(line)                                         
                
                else:
                    print(self.tree_build_fail_str, "Input line does not follow expected format: {0}".format(line))
                    sys.exit()
                            
    def process_line(self, line):
        node_name = line.split(":")[0].strip()
        if node_name not in self.nodes:
            self.nodes[node_name] = GraphNode(node_name)

        neighbor_names = line.split(":")[1].strip()[1:-1]
        if neighbor_names:
            for neighbor_name in neighbor_names.split(","):
                neighbor_name = neighbor_name.strip()
                if neighbor_name not in self.nodes:
                    self.nodes[neighbor_name] = GraphNode(neighbor_name)

                if self.nodes[neighbor_name] not in self.nodes[node_name].neighbors:
                    self.nodes[node_name].neighbors.append(self.nodes[neighbor_name])
                
                if self.nodes[node_name] not in self.nodes[neighbor_name].neighbors:
                    self.nodes[neighbor_name].neighbors.append(self.nodes[node_name])
                    
    def graph_constraints(self, colors):
        for node_name, node in self.nodes.items():
            self.clause_list.append(" ".join([node_name + "_" + c for c in colors]))

            for c in colors:
                for neighbor_node in node.neighbors:
                    self.clause_list.append("!" + node_name + "_" + c + " !" + neighbor_node.name + "_" + c)

        return self.clause_list
        
    def print_graph(self):
        for name, node in self.nodes.items():
            print("{0} - {1}".format(name, [n.name for n in node.neighbors]))


