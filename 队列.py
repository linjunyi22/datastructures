# Python 使用内置类型 list 实现队列

class Queue(object):
	# 初始化队列
	def __init__(self):
		self.queue = []

	# 队列长度
	def size(self):
		return len(self.queue)

	# 队列是否为空
	def isEmpty(self):
		return self.size == 0

	# 队尾增加元素
	def enqueue(self,x):
		self.queue.append(x)

	# 队头删除元素
	def dequeue(self):
		self.queue.pop(0)


