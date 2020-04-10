# -*- coding: utf-8 -*-
# 堆排序
# 建立顶大堆
def heapify(heap, n, i):
    '''
    heap 堆
    n 堆的长度
    i 需要排序的 节点
    '''
    
    if i >= n:
        return 
    p = i

    l = 2*p + 1
    r = 2*p + 2

    mx = i

    if l < n and heap[l] > heap[mx]:
        mx = l
    
    if r < n and heap[r] > heap[mx]:
        mx = r
    
    if i != mx:
        heap[i], heap[mx] = heap[mx], heap[i]
        heapify(heap, n, mx)

# 如果是无序的堆，需要创建成大顶堆
def build_heap(nums, n):
    # 从最小的一层的父节点开始计算
    # 也就是 最小的节点是 n - 1 那么他的父节点就是 (n - 1) / 2

    p = (n - 1) / 2

    for i in range(p-1, -1, -1):
        heapify(nums, n, i)

def heap_sort(nums):
    ln = len(nums)
    build_heap(nums, ln)
    # 最后一个 和 最顶上的交换，然后从新调整堆
    for i in range(ln-1, -1, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    return nums


if __name__ == "__main__":
    print heap_sort([2,1,3,4,5,56,1,12,32])