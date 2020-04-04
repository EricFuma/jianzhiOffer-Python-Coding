class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, mid, right = 0, 0, len(numbers)-1
        
        # 如果不满足 while 中的条件，说明 numbers[left:right+1] 是递增序列，那么直接返回 numbers[left] 即可，为了保证统一性，返回 numbers[mid]，所以把 mid 初始化为 left=0，防止一开始遇到的就是递增序列
        # 跳出循环的边界条件1：数组有序
        while numbers[left] >= numbers[right]:
            # 跳出循环的边界条件2：只剩一个或两个元素
            # 默认是让 left 指向左递增序列，right 指向右递增序列，所以 right 代表的元素肯定更小
            if right-left <= 1:
                mid = right
                break    # 不加这个就会无限循环
  
            mid = left + (right-left) // 2
            # 无法使用二分法，则遍历；注意这里 left += 1 就不行，因为我们是想让 right 表示更小的那个元素的，所以让right变化来寻找；如果这边想不明白，可以不区分left+还是right-，但要在跳出循环2中对left和right代表的数值加以判断，赋给mid更小元素的下标
            if numbers[left] == numbers[mid] == numbers[right]:
                #left += 1
                right -= 1
            # 注意这是和上面这一个条件连在一起的；第一个条件就不用连了，因为它是跳出循环的
            elif numbers[mid] >= numbers[left]:
                left = mid
            else:  # if numbers[mid] <= numbers[right]
                right = mid
        return numbers[mid]



