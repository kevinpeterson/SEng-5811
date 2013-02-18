#                
#                0
#               /|
#              1 |
#               \|
#                2 
#               / \          
#              3   4
#               \ / \\
#                6    5
#
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
    

print "\n"           
for path in find_paths('0',graph,{'4':1}): 
    print "->".join(str(p) for p in path)
    
print "\n"            
for path in find_paths('0',graph,{'4':2,'5':1}): 
    print " -> ".join(str(p) for p in path)