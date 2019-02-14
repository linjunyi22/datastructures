# Python 实现链表

# 定义节点类
class Node(object):
    def __init__(self, data, pnext = None):
        self.data = data # 节点数据
        self._next = pnext # 节点指针

# 定义链表类
class LinkedList(object):
    #初始化链表
    def __init__(self):
        self.head = None # 头指针指向 None，空表
        self.length = 0 #表长度为零

    # 是否为空表
    def isEmpty(self):
        return self.length == 0

    # 遍历链表
    def traverse(self):
        if self.isEmpty():
            print('空表，无法遍历')
            return False

        pre = self.head
        while pre:
            print(pre.data)
            pre = pre._next

    # 链表添加元素
    def append(self, data):
        item = Node(data)   # 初始化节点

        # 没有头结点，直接插在头指针后
        if not self.head:
            self.head = item
            self.length += 1

        # 有头结点，遍历链表
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item # 链表尾指针指向插入元素，更新链表尾
            self.length += 1

    # 删除元素
    def delete(self, index):
        if self.isEmpty(): # 空表无法删除
            print('空表，无法删除元素！')
            return False

        if index < 0 or index >= self.length:
            print('超出链表范围')
            return False

        j = 0
        node = self.head # 当前节点
        prev = self.head # 前导节点
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index: # 找到了指定删除的索引指针
            prev._next = node._next # 前导节点直接指向当前节点的后一个节点
            self.length -= 1

    # 插入元素
    def insert(self, index, data):
        if self.isEmpty():
            return False

        if index < 0 or index >= self.length:
            return False

        item = Node(data)

        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return

        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            item._next = node
            prev._next = item
            self.length += 1

    # 检索元素
    def find(self, index):
        if self.isEmpty() or index < 0 or index >= self.length:
            return False
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1

        return node.data

    # 索引指针在表中位置
    def getIndex(self, data):
        j = 0
        if self.isEmpty():
            return False
        node = self.head
        while node:
            if node.data == data:
                return j
            node = node._next
            j += 1

        if j == self.length:
            return 'not found'

    # 清空链表        
    def clear(self):
        self.head = None
        self.length = 0

l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.insert(2,77)
l.traverse()
