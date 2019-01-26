# Python实现顺序表

class Seqlist(object):
    # 初始化顺序表
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.data = []
        self.last = -1

    # 判断是否为空表
    def isEmpty(self):
        return self.last == -1

    # 判断表是否已满
    def isFull(self):
        return self.last == (self.maxsize - 1)

    # 清空顺序表 
    def clearlist(self):
        if not self.isEmpty():
            self.data = []
            self.last = -1
            return True
        return False

    # 返回当前表的长度，下标+1
    def length(self):
        return self.last + 1

    # 查找元素
    def search(self, element):
        if self.isEmpty(): # 空表，返回 False
            return False
        for i in range(self.last+1): # 找到元素，返回该元素下标
            if self.data[i] == element:
                return i
        return False # 既不为空表，也没找到元素，返回 False

    # 插入元素
    def insert(self, element, index):
        if self.isFull():
            return False # 表已满，无法插入
        elif index < 0 or index >= self.maxsize:
            return False # 插入位置错误
        elif index == self.last + 1:
            self.data.append(element) # 默认在表末插入元素
            self.last += 1
            return self.data
        else:
            self.data.append(None) #先申请一个位置
            for i in range(self.last, index-1, -1): # 表尾往后移一个位置
                self.data[i+1] = self.data[i]
            self.data[index] = element
            self.last += 1
        return self.data

    # 删除元素
    def delete(self, element):
        if self.isEmpty(): # 空表，无法删除
            return False 
        else:             # 找出元素所在位置，从该位置开始循环，元素往前移 
            for i,v in enumerate(self.data):
                if element == v:
                    for j in range(i,self.last):
                        self.data[i] = self.data[i+1]
                    self.last -= 1
                    return v
            return False

l = Seqlist(10)
print(l.isEmpty())
print(l.isFull())
print(l.clearlist())
print(l.length())
l.insert(10,0)
l.insert(8,1)
l.insert(7,1)
print(l.length())
print(l.delete(10))
