# Python 实现栈

class Stack(object):
	# 初始化栈
	def __init__(self,MaxSize):
		self.MaxSize = MaxSize
		self.stack = []
		self.Top = -1
 	
 	# 判断栈是否空
	def isEmpty(self):
		if self.Top == -1: # 下标为-1则空栈，否则不为空栈
			return True # 为空
		return False # 不为空

  	# push 元素
	def push(self,x):
		self.stack.append(x)
		self.Top += 1
		return self.stack

	# pop 元素
	def pop_(self):
		if self.isEmpty():
			return False
		else:
			pop_item = self.stack.pop()
			self.Top -= 1
			return pop_item

	# 栈的个数
	def size(self):
		return len(self.stack)
