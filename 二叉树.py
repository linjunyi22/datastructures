"""
实现一个二叉树
"""

# 节点类
class Node(object):
	# 节点初始化，数据域，左右指针
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def get_value(self):
		return self.data


class Tree(object):
	def __init__(self):
		self.root = Node()
		self.queue = [] # 队列用于创存储要添加节点的节点

	# 添加树节点
	def add(self,data):
		node = Node(data)
		if self.root.data == None: # 空树，给根节点赋值
			self.root = node
			self.queue.append(self.root)
		else:
			tree_node = self.queue[0] # 把队头的节点记住，下一次就在这个节点下添加
			if tree_node.left == None: # 左子树为空，添加左儿子
				tree_node.left = node
				self.queue.append(tree_node.left) # 左儿子添加到队列中

			else: # 左子树不空，添加右儿子
				tree_node.right = node
				self.queue.append(tree_node.right) #右儿子添加到队列中

				"""----- 到这里左右儿子都添加上了-----"""
				# 把父节点从队列里删掉，然后左儿子充当父节点，再添加他的左右儿子，然后删掉
				# 然后右儿子当父节点，再添加他的左右儿子，然后删掉，以此类推
				self.queue.pop(0) 

	# 递归实现先序遍历
	def front_recursion(self,root):
		if root == None:
			return '空树，请先创建一个树'

		print(root.data, end=' ')
		self.front_recursion(root.left)
		self.front_recursion(root.right)

	# 递归实现中序遍历
	def middle_recursion(self,root):
		if root == None:
			return '空树，请先创建一个树'

		self.front_recursion(root.left)
		print(root.data, end=' ')
		self.front_recursion(root.right)

	# 递归实现后序遍历
	def last_recursion(self,root):
		if root == None:
			return '空树，请先创建一个树'

		self.front_recursion(root.left)
		self.front_recursion(root.right)
		print(root.data, end=' ')

	# 队列层次遍历
	def level_circle(self,root):
		if root == None:
			return '空树，请先创建一个树'
		q_list = []
		node = root
		q_list.append(node)

		# 把节点存进队列，抛出来，再把儿子存进队列，再抛出来，重复操作，直到所有节点都抛出来
		while q_list:
			node = q_list.pop(0)
			print(node.data,end=' ')
			if node.left != None:
				q_list.append(node.left)
			if node.right != None:
				q_list.append(node.right)


tree = Tree()
for data in range(10):
	tree.add(data)

# 先序
tree.front_recursion(tree.root)
print('-------先序')

# 中序
tree.middle_recursion(tree.root)
print('-------中序')

# 后序
tree.last_recursion(tree.root)
print('-------后序')

# 层次遍历
tree.level_circle(tree.root)
print('-------层次')



