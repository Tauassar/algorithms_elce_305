

class BST:
	# first node of the tree
	root =None
	# actual value stored in node
	key = None
	# childrens of the node
	left = None
	right = None
	# parent node
	p = None

	def __init__(self, num=None):
		self.key=num
	# return key value when called on print or converted to string
	def __str__(self):
		return str(self.key)
	
	# Insert new node to the tree
	def insert(self,num):
		print('\ninsert function is called')
		print('The value to insert is: {}'.format(num))
		z = BST(num)
		y = None
		x = self.root
		while x!=None:
			y=x
			if z.key<x.key:
				x = x.left
			else:
				x=x.right
		z.p = y
		if y==None:
			self.root = z
		elif z.key<y.key:
			y.left=z
		else:
			y.right=z
		self.showBST()
		self.drawBST()

	# Inorder tree walk implementation
	# decorating function for inOrderTreeWalk, to print new line and header 
	def inOrder(self):
		print('\ninOrder function is called')
		print('Printing values in ascending order:')
		self.inOrderTreeWalk(self.root)
		print('')
	# actual algorithm of inorder tree walk presented in lectures
	def inOrderTreeWalk(self, node):
		if node.left!=None:
			self.inOrderTreeWalk(node.left)

		print(node, end = ' ')
	
		if node.right!=None:
			self.inOrderTreeWalk(node.right)

	# Function to print values of BST level by level
	def showBST(self):
		print('\nshowBST function is called')
		print('Printing values stored in the tree:')
		bst_raw_structure = self.retreiveStructure()
		counter = 1
		for arr in bst_raw_structure:
			temp = []
			for value in arr:
				if value!= None:
					temp.append(value.key)
				else:
					temp.append(None)
			print('Row #{}: {}'.format(counter,temp))
			counter=counter+1
	# Compose structure of the tree into single list
	def retreiveStructure(self):		
		tree_root = [self.root]
		bst_structure = [tree_root]
		try:
			for item in self.traverseTree(tree_root):
				bst_structure.append(item)
		except:
			pass
		return bst_structure
	# iterate through the tree using recursion to obtain tree components level by level
	def traverseTree(self, nodes):
		result = []
		childrens=[]
		contd=False
		for node in nodes:
			if node.left!=None:
				childrens.append(node.left)
				contd=True
			else:
				childrens.append(None)
			if node.right!=None:
				childrens.append(node.right)
				contd=True
			else:
				childrens.append(None)
		if contd:
			result.append(childrens)
			try:
				for item in self.traverseTree(childrens):
					result.append(item)
			except:
				pass
			return result 
		return
	# Function to draw the composed tree using traverseTree method
	def drawBST(self):
		print('\ndrawBST function is called')
		print('Printing tree:\n')
		lists = self.retreiveStructure()
		longest_array = int(len(lists[-1])/2)
		steps = int(len(lists))*4
		for arr in lists:
			print('   '*longest_array, end = '')
			longest_array = int(longest_array/2)
			for field in arr:
				print(field, end = ' '*(steps))
			steps=int(steps/2)
			print('\n')

	    	

# Main function
arr = [40, 70, 50, 60, 20, 80, 30, 10, 90]
tree = BST()
print("Initial array: {}".format(arr))
# Inserting values into the tree
for value in arr:
	tree.insert(value)

tree.inOrder()

