# Program to count islands in boolean 2D matrix 
class Graph: 

	def __init__(self, row, col, g): 
		self.ROW = row 
		self.COL = col 
		self.graph = g 

	# A function to check if a given cell 
	# (row, col) can be included in DFS 
	def isSafe(self, i, j, visited): 
		# row number is in range, column number 
		# is in range and value is 1 
		# and not yet visited 
		return (i >= 0 and i < self.ROW and
				j >= 0 and j < self.COL and
				not visited[i][j] and self.graph[i][j]) 
			

	# A utility function to do DFS for a 2D 
	# boolean matrix. It only considers 
	# the 8 neighbours as adjacent vertices 
	def DFS(self, i, j, visited): 

		#these arrays are used to find the neighbors 
		#in 8 directions
		rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]; 
		colNbr = [-1, 0, 1, -1, 1, -1, 0, 1];
		
		#create counter to count the island sizes
		count = 1
		# Mark this cell as visited
		visited[i][j] = True

		# recursively iterates through each neighbor (8 directions) 
		for k in range(8): 
			if self.isSafe(i + rowNbr[k], j + colNbr[k], visited): 
				#count the recursive calls for when there is a 1 neighbor
				count += self.DFS(i + rowNbr[k], j + colNbr[k], visited)
		#return the island size
		return count

	def islandsize(self): 

		# Initially all cells are unvisited 
		visited = [[False for j in range(self.COL)]for i in range(self.ROW)]
		#create empty array that stores the island sizes in the graph
		d = []
		#travese through the all cells of the graph
		for i in range(self.ROW): 
			for j in range(self.COL): 
				# if cell with value 1 is not visited yet 
				if visited[i][j] == False and self.graph[i][j] == 1: 
					# call dfs to count the island size around the new
					#found island
					count = self.DFS(i, j, visited)
					#add the value to the array
					d.append(count)

		return d 


graph = [[1, 0, 0, 1], 
		[0, 1, 0, 1], 
		[0, 1, 0, 0], 
		[0, 1, 0, 1]]


row = len(graph) 
col = len(graph[0]) 

g = Graph(row, col, graph) 

print "Island Sizes are:"
print g.islandsize() 
