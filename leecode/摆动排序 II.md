# 摆动排序 II
  [摆动排序 II](https://leetcode-cn.com/problems/wiggle-sort-ii/) 
给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]… 的顺序。
**示例 1:**
```
*输入:*nums = [1, 5, 1, 1, 6, 4]
*输出:*一个可能的答案是 [1, 4, 1, 5, 1, 6]
```
**示例 2:**
```
*输入:*nums = [1, 3, 2, 2, 3, 1]
*输出:* 一个可能的答案是 [2, 3, 1, 3, 1, 2]
```
**说明:**
你可以假设所有输入都会得到有效的结果。
**进阶:**
你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？
```
nums = [1, 5, 1, 1, 6, 4]
nums = [1, 3, 2, 2, 3, 1]
nums = [1, 2, 3, 4, 5, 6]
def wiggle(nums):
    nums.sort(reverse=True)
    c = [0,0,0,0,0,0]
#     nums = [(idx, item)for idx, item in enumerate(nums)]
#     print nums
#     print nums[::2], nums[1::2] , nums[len(nums)/2:], nums[:len(nums)/2], "sssss"
    c[::2], c[1::2] = nums[len(nums)/2:],  nums[:len(nums)/2]
    print c
    print nums
```
先倒叙排序
然后 将数列分成两半，
后半段 穿插入前半段即可

#leecode-cn/中等