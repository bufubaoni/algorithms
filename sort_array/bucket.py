def bucketSort(nums):
    bucket = [0]*100000
    out = [0]*len(nums)
    
    for i in nums:
        bucket[i+50000] +=1
        # 由于可能会存在负数 所以从中间开始
    j = 0
    for i, v in enumerate(bucket):
        
        while v > 0:
            
            out[j] = i-50000
            v -= 1
            j += 1
    return out
