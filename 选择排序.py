"""
选择排序
已排序序列:[0,i]
未排序序列:[i+1,n]
"""

def select_sort(l):
    for i in range(0,len(l)): # 只需比较n-1个数，当n-1个数排好序时，最后一个也已排好序
        temp = i
        for j in range(i + 1,len(l)): #从该数的下一个数开始比较
            if l[temp] > l[j]:
                temp = j
        l[i], l[temp] = l[temp], l[i]
    return l

test = list(range(10,0,-1))
print(select_sort(test))
