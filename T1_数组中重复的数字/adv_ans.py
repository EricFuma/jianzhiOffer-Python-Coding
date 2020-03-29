# 1~n  n+1
nums = [7, 1, 4, 6, 2, 5, 3, 6]  # n = 7, 
pos = [i for i in range(1, len(nums)+1)]
#nums = [2, 3, 5, 4, 3, 2, 6, 7]
#nums = [0] + nums   # 0占位用
def count_num(left, mid, right):
    count_l, count_r = 0, 0
    for i in range(len(nums)):
        if left <= nums[i] < mid:
            count_l += 1
        elif right >= nums[i] > mid: 
            count_r += 1
    return count_l, count_r

def find_ele(left, right):
    if left < right:
        mid = left + (right-left) // 2
        count_l, count_r = count_num(left, mid, right)
        #print(left, mid, right, count_l, count_r)
        if len(nums) - count_l - count_r > 1:
            return mid
        elif count_l > mid-left:
            return find_ele(left, mid-1)
        elif count_r > right-mid:
            return find_ele(mid+1, right)
    else:
        return left

print(find_ele(1, len(nums)-1))
