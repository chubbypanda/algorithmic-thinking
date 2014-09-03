# Project 1 for Algorithmic Thinking class, by k., 08/30/2014
# Degree distributions for graphs
# https://class.coursera.org/algorithmicthink-001/wiki/graph_degree

'''
three graph examples prescribed by the assingment; see project1.png
set of test case graphs at:
http://storage.googleapis.com/codeskulptor-alg/alg_module1_graphs.py
'''

EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 4, 5, 6, 7, 3])}


def make_complete_graph(num_nodes):
    '''
    takes the number of nodes num_nodes;
    returns a dictionary corresponding to a complete directed graph with the specified number of nodes

    nodes numbered 0 to num_nodes - 1, when num_nodes is positive,
    otherwise, the function returns a dictionary corresponding to the empty graph
    '''
    complete_graph = {}
    set_nodes = set(range(num_nodes))
    
    for node in range(num_nodes):
        # all nodes except for self-loops (not allowed)
        complete_graph[node] = set_nodes - set([node])

    return complete_graph


def compute_out_degrees(digraph):
    '''
    out of curiousity (not specified in the assignment);
    computes the out-degrees for the nodes in the digraph (directed graph);
    return a dictionary (with the same set of keys),
    '''
    out_degrees = {}
    
    for node in digraph:
        # simple check for length of each set
        out_degrees[node] = len(digraph[node])

    return out_degrees
        

def compute_in_degrees(digraph):
    '''
    computes the in-degrees for the nodes in the digraph (directed graph);
    return a dictionary (with the same set of keys) with corresponding values
    are the number of edges whose head matches a particular node
    '''
    in_degrees = {}
    list_nodes = []
    
    for node in digraph:
        # need to convert set to list
        list_nodes.extend(list(digraph[node]))

    for node in digraph:
        # count occurances of each degree
        in_degrees[node] = list_nodes.count(node)

    return in_degrees


def in_degree_distribution(digraph):
    '''
    computes the unnormalized distribution of the in-degrees of the graph;
    return a dictionary whose keys correspond to in-degrees of nodes in the graph,
    value associated with each key is the number of nodes with that in-degree
    '''
    distribution = {}
    list_indegrees = []
    in_degrees = compute_in_degrees(digraph)

    for degree in in_degrees:
        list_indegrees.append(in_degrees[degree])

    for degree in list_indegrees:
        if degree not in distribution.keys():
            # first occurance, initialize to 1
            distribution[degree] = 1
        else:
            # increment next occurance(s)
            distribution[degree] += 1

    return distribution
