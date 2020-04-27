
def merge(L, R):
    a_idx = 0
    arr = [0]*(len(L)+len(R))
    while L and R:
        if L[0] < R[0]:
            arr[a_idx] = L.pop(0)
        else:
            arr[a_idx] = R.pop(0)
        a_idx += 1
    while L:
        arr[a_idx] = L.pop(0)
        a_idx += 1
    while R:
        arr[a_idx] = R.pop(0)
        a_idx += 1
    return arr
def get_mid(arr):
    mid = len(arr) / 2
    return mid

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    elif not arr:
        return []
    
    mid = get_mid(arr)

    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])
    return merge(L, R)

if __name__ == "__main__":
    lst = [1,7,8 ,2,4,5, 9,0]

    print merge_sort(lst)