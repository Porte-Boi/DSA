class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:             # This type of for loops are used for breaking tuples
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("All routes: ",self.graph_dict)
    
    # Finding the all paths

    def get_paths(self, start, end, path =[]):
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths



if __name__ == "__main__":
    routes = [
        ("chittagong", "dhaka"),
        ("chittagong", "cox's bazar"),
        ("dhaka", 'dubai'),
        ("dubai", "bologna"),
        ("dhaka", "sylet"),
    ]

    route_graph = Graph(routes)

    start = "chittagong"
    end = "sylet"

    print(f"\nPaths between {start} and {end}: ", route_graph.get_paths(start, end))



