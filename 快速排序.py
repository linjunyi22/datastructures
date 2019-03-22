"""
快速排序
"""

# 进行一次分区操作，并找出基准值的位置
def partion(array, begin, end):
    pivot_index = begin
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end - 1

    while True:
        # 左边寻找大于基准值 pivot 的那个值
        while left <= right and array[left] < pivot:
            left += 1

        # 右边寻找小于基准值 pivot 的那个值
        while left <= right and array[right] >= pivot:
            right -= 1

        # left 和 right 发生了交叉，直接退出循环，否则交换 left 和 right 的值
        if left > right:
            break
        else:
            # 交换元素
            array[left], array[right] = array[right], array[left]
    # right 与 基准值 pivot 进行交换,保证基准值左边的值全部小于基准值，右边全部大于基准值
    array[right], array[pivot_index] = array[pivot_index], array[right]
    return right

def quick_sort(array, begin, end):
    # 递归出口
    if begin < end:
        pivot_index = partion(array, begin, end)
        quick_sort(array, begin, pivot_index)
        quick_sort(array, pivot_index + 1, end)
            
if __name__ == '__main__':
    l = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    quick_sort(l, 0, len(l))
    print(l)
