"""
二分查找的一个很重要的性质是对有序列表的查找！！有序列表！！
"""

def bin_search(l,val):
	left = 0
	right = len(l) - 1
	while left < right:
		mid = (left + right)//2

		if l[mid] > val:
			right = mid - 1 # 右指针往左移
		elif l[mid] < val:
			left = mid + 1 # 左指针往右移
		else:
			result = '{}的位置是第{}个'.format(val, mid)
			return result
	if l[right] == val:
		return '{}的位置是第{}个'.format(val, right)
	return '没有这个元素'

a = list(range(1,9))
print(bin_search(a,6))
