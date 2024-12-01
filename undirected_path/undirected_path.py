def undirected_path(edges, node_A, node_B):
  # construct a dict from edges
  graph = {}
  for edge in edges:
    if edge[0] in graph:
      graph[edge[0]].append(edge[1])
    else:
      graph[edge[0]] = [edge[1]]
      
    if edge[1] in graph:
      graph[edge[1]].append(edge[0])
    else:
      graph[edge[1]] = [edge[0]]


  print(graph)
  # try to find if they are conencted
  stack = [node_A]
  visited = set()
  while stack!=[]:
    curr = stack.pop()
    
    if curr not in visited:
      visited.add(curr)
      if curr == node_B:
        return True
      else:
        stack+=graph[curr]
    
  return False
  '''
    graph = {}
    for edge in edges:
      if edge[0] in graph:
        graph[edge[0]].append(edge[1])
      else:
        graph[edge[0]] = [edge[1]]
      
      if edge[1] in graph:
        graph[edge[1]].append(edge[0])
      else:
        graph[edge[1]] = [edge[0]]
    
    stack = [node_A]
    visited = set()
    while(stack!=[]):
      curr = stack.pop()
      if curr not in visited:
        visited.add(curr)
      if curr==node_B:
        return True
      for el in graph:
        if el not in visited:
          stack.append(el)
          
    return False
  '''
  
    