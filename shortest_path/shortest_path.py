edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]


def shortest_path(edges, node_A, node_B):




  graph = {}
  # build a graph
  for edge in edges:
    if edge[0] in graph:
      graph[edge[0]].append(edge[1])
    else:
      graph[edge[0]] = [edge[1]]


    if edge[1] in graph:
      graph[edge[1]].append(edge[0])
    else:
      graph[edge[1]] = [edge[0]]


  visited = set()
  queue = [[node_A,0]]
  while queue!=[]:
    curr_node,curr_dist = queue[0][0],queue[0][1]
    queue = queue[1:]
    print(queue)
    if curr_node == node_B:
      
      return curr_dist


    for node in graph[curr_node]:
      if node not in visited:
        queue.append([node,curr_dist+1])
        visited.add(node)
  return -1


shortest_path(edges, 'b', 'g')