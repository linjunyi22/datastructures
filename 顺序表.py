# Python实现顺序表

class Seqlist(object):
	# 初始化顺序表
	def __init__(self, maxsize):
		self.maxsize = maxsize
		self.data = []
		self.last = -1

	# 判断是否为空表
	def isEmpty(self):
		if self.last == -1:
			return True
		return False

	# 判断表是否已满
	def isFull(self):
		if self.last == maxsize - 1:
			return True
		return False

	# 清空顺序表	
	def clearlist(self):
		if not self.isEmpty(self):
			self.data = []
			self.last = -1
		return False

	# 返回当前表的长度，下标+1
	def length(self):
		return self.last + 1

	# 查找元素
	def search(self, element):
		if self.isEmpty(self): # 空表，返回 False
			return False
		for i in range(self.last+1): # 找到元素，返回该元素下标
			if self.data[i] == element:
				return i
		return False # 既不为空表，也没找到元素，返回 False

	# 插入元素
	def insert(self, index=self.last+1, element):
		if isFull(self):
			return False # 表已满，无法插入
		elif index < 0 or index >= self.maxsize:
			return False # 插入位置错误
		elif:
			self.data.append(element) # 默认在表末插入元素
			self.last += 1
			return self.data
		else:
			for i in range(self.last, index-1, -1): # 表尾往后移一个位置
				self.data[i+1] = self.data[i]
			self.data[index] = element
			self.last += 1
		return self.data

	# 删除元素
	def delete(self, element):
		if isEmpty(self): # 空表，无法删除
			return False 
		else:			  # 找出元素所在位置，从该位置开始循环，元素往前移 
			index = -1
			for item in self.data:
				index += 1
				if element == item:
					break
			for i in range(index, self.data):
				self.data[i] == self.data[i+1]
			self.last -= 1
		return self.data[]



