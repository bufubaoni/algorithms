# -*- coding: utf-8 -*-
# 1. build segment tree
# 2. query
# 3. update

# 首先计算一下 tree 的长度
MAX_LEN = 15
tree = [0]*MAX_LEN
arr = [1, 3, 5, 7, 9, 11]

def build(arr, tree, node,  start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        node_left  = 2 * node + 1 
        node_right = 2 * node + 2
        # "中间树"
        mid = (start + end) / 2
        build(arr, tree, node_left, start, mid)
        build(arr, tree, node_right, mid + 1, end)
        tree[node] = tree[node_right]+tree[node_left]
def update_tree(arr, tree, node,  start, end, idx, val):
    if start == idx:
        tree[node] = arr[idx] = val
    else:
        node_left  = 2 * node + 1 
        node_right = 2 * node + 2
        mid = (start + end) / 2
        if idx > mid:
            update_tree(arr, tree, node_right, mid + 1, end,  idx, val)
        else:
            update_tree(arr, tree, node_left, start, mid, idx, val)
        tree[node] = tree[node_right]+tree[node_left]

def query_tree(arr, tree, node, start, end, L, R):
    print ('start', start)
    print ('end  ', end)
    if L > end or R < start:
        # L, R 不在区间
        return 0
    elif start >= L and R <= end:
        return tree[node]
    elif start == end:
        return tree[node]
    else:
        node_left  = 2 * node + 1 
        node_right = 2 * node + 2
        mid = (start + end) / 2

        sum_left = query_tree(arr, tree, node_left, start, mid, L, R)
        sum_right = query_tree(arr, tree, node_right,mid+1, end, L, R)
        return sum_left + sum_right

if __name__ == "__main__":
    build(arr, tree, 0, 0, len(arr)-1)
    print tree, arr
    update_tree(arr, tree, 0, 0, len(arr)-1, 4, 6)
    print tree, arr
    print query_tree(arr, tree, 0, 0, len(arr)-1, 2, 5)