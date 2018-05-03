"""
插入排序
"""

l = [2,6,5,4,1,7,8,9,0]

def insert_sort(lists):
    for i in range(1, len(lists)): # 插入排序一定要有一个已经排好序的，一般选下标为零那个
        temp = lists[i] # 记住当前还没排序的元素
        j = i - 1 # 从i-1到0是已经排好序的，待会要比较
        while j >= 0: # 从 i-1到0开始遍历
            if lists[j] > temp: # 如果已经排好序的元素里有比当前待排序的元素大，那么把元素往后移动一个位置
                lists[j + 1] = lists[j] # 从 j 位置移动到 j+1
                lists[j] = temp
            j -= 1
    return lists

test = insert_sort(l)
print(test)
