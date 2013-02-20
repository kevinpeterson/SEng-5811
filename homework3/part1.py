print '''
##############
Kevin Peterson
SEng 5811 
Homework #3
Part 1
https://github.com/kevinpeterson/SEng-5811/blob/master/homework3/part1.py
##############
'''

graph = '''                 
                0
               /|
              1 |
               \|
                2 
               / \          
              3   4
               \ / \\\\
                6    5
'''

print "Graph:"
print graph

graph = {'0': ['1', '2'],
           '1': ['2'],
           '2': ['3', '4'],
           '3': ['6'],
           '4': ['5', '6'],
           '5': ['4']}

def _is_visited(node,path,visits):
    if node in path:
        if node in visits:
            visits_left = visits[node]
            if visits_left == 1:
                del visits[node]
            else:
                visits[node] -= 1  
            return False
        else:
            return True
    else:
        return False

def find_paths(start,graph,visits,path=[]):
    '''Recursively look for paths through the graph.
       The 'visits' param will allow for more than one
       visit of a node during path scan. This is used
       to simulate looping. If a node is not mentioned
       in 'visits,' it is assumed it can be visited
       only once.
    '''
    if start not in graph:
        return [[start]]
    else:
        children = graph[start]
        paths = []
        for child in children:
            if not _is_visited(child,path,visits):
                visits_copy = visits.copy()
                for sub_path in find_paths(child,graph,visits_copy,path + [child]):
                    paths.append([start] + sub_path)
                
        return paths
    
print "(a) Paths:"           
for path in find_paths('0',graph,{'4':1}): 
    print "->".join(str(p) for p in path)
    
print "\n(b) Paths:"          
for path in find_paths('0',graph,{'4':2,'5':1}): 
    print " -> ".join(str(p) for p in path)
    
    
def _get_cover_sets(main_set,cover_sets):
    '''Cover Set Algorithm'''
    cover_set = []
    
    while len(main_set) > 0:
        most_matches = 0
        best_subset = None
            
        for candidate_set in cover_sets:
            matches = len(main_set.intersection(candidate_set))
            if matches > most_matches:
                most_matches = matches
                best_subset = candidate_set;
    
        main_set = main_set.difference(best_subset)
        cover_sets.remove(best_subset)
        cover_set.append(best_subset)
    
    return cover_set;
    
 
graph_nodes = set()

paths = find_paths('0',graph,{'4':1});
for path in paths: 
    for node in path:
        graph_nodes.add(node)
                
cover_paths = _get_cover_sets(graph_nodes,paths)
      
print "\n(c) Test Coverage:"
print "There are %i path(s) that will cover all nodes in the graph: " % len(cover_paths)
for cover_path in cover_paths:
    print " -> ".join(str(p) for p in cover_path)

 
    