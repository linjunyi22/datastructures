"""
冒泡排序，有 n 个数，每一个数比较一趟，那么就要比较 n-1趟
每一个数要跟其他数比较，每比较一次，下一个要比较的数的比较次数就少一次
"""

l = [3,1,4,5,2,0,7,9]

def bubble_sort(lists):
	for i in range(0,len(lists)-1): # n 个数，比较 n-1趟
		for j in range(0,len(lists)-i-1): # 第一个数与 n-1个数比较，第二个数与 n-1-1个数比较，...，第 n 个数与 n-i-1个数比较
			if lists[j+1] < lists[j]: # 比较，符合就调换，不符合就保留原位
				temp = lists[j]
				lists[j] = lists[j+1]
				lists[j+1] = temp
	return lists

test = bubble_sort(l)
print(test)
