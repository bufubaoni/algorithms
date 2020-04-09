# -*- coding: utf-8 -*-
# 堆排序

def max_heapify(heap, root, heap_len):
    p = root
    while p*2+1 < heap_len:
        l, r = p*2+1, p*2+2
        if heap_len <=r or heap[r] < heap[l]:
            nxt = l
        else:
            nxt = r
        
        if heap[p] < heap[nxt]:
            heap[p], heap[nxt] = heap[nxt], heap[p]
            p = nxt
        else:
            break
            
def build_heap(heap):
    for i in range(len(heap)-1, -1, -1):
        max_heapify(heap, i, len(heap))

def heepSort(nums):
    # 建堆
    build_heap(nums)
    for i in range(len(nums)-1, -1, -1):
        # 下沉过程
        nums[i], nums[0] = nums[0], nums[i]
        # 重新排序
        max_heapify(nums, 0, i)

def sortArray(nums):
    heepSort(nums)
    return nums

if __name__ == "__main__":
    print sortArray([2,1,3,4,5,56,1,12,32])