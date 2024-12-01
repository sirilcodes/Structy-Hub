def island_count(grid):
  count  = 0
  visited = set()
  steps = [[1,0],[-1,0],[0,1],[0,-1]]
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      
      
        
      if grid[r][c] == 'L':
        if (r,c) not in visited:
          count+=1
        stack = [[r,c]]
        print(visited)
        while stack!=[]:
          r,c = stack.pop()
          if (r,c) not in visited:
            #count+=1
            visited.add((r,c))
            for step in steps:
              if r+step[0] >= 0 and r+step[0] < len(grid):
                if c+step[1] >= 0 and c+step[1] < len(grid[0]):
                  #print("r: c: ",r+step[0], c+step[1])
                  if grid[r+step[0]][c+step[1]] == 'L':
                    stack.append([r+step[0],c+step[1]])
                    #if (r+step[0],r+step[1]) not in visited:
                    #  visited.add((r+step[0],c+step[1]))
                      
  print("Count is :-------   ",count)    
            
  return count


          
      
'''
  visited = set()
  count = 0
  directions = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == "L":
        if (r,c) not in visited:
          count+=1
        stack = [[r,c]]
        
        while stack != []:
          
          curr = stack.pop()
          if (curr[0],curr[1]) not in visited:
            # move in all directions, and add to visited if its land
            
            visited.add((curr[0],curr[1]))
            for dir in directions:
              curr[0]+=dir[0]
              curr[1]+=dir[1]
              
              #cap row
              if curr[0]<=0:
                curr[0]=0
              if curr[0]>len(grid)-1:
                curr[0]=len(grid)-1
              
              #cap column
              if curr[1]<=0:
                curr[1] = 0
              if curr[1]>=len(grid[0])-1:
                curr[1] = len(grid[0])-1


              if grid[curr[0]][curr[1]]=="L":
                if (curr[0],curr[1]) not in visited:
                  #print(curr[0],curr[1])
                  stack.append([curr[0],curr[1]])
        
  return count
'''     


'''
grid = [
  ['W', '-', 'W', 'W', 'W'],
  ['W', '-', 'W', 'W', 'W'],
  ['W', 'W', 'W', '-', 'W'],
  ['W', 'W', '-', '-', 'W'],
  ['-', 'W', 'W', 'L', 'L'],
  ['-', '1', 'W', 'W', 'W'],
]
'''
        
            