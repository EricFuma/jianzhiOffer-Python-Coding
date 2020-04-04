class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # 特判：空数组
        if not nums:
            return None
        
        # 3. 计数排序
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
            elif nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                # 切记，这里如果赋值顺序颠倒的话报错，原因应该是没有 deepcopy 吧
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        # 1. 排序算法 --> e.g. 快排，O(nlogn) & O(1)
        '''
        def quickSort(start, end):
            if start >= end:
                return True
            else:
                solder = end
                current = start
                for i in range(start, end):
                    if nums[i] < nums[solder]:
                        nums[i], nums[current] = nums[current], nums[i]
                        current += 1
                nums[current], nums[end] = nums[end], nums[current]
                quickSort(start, current-1)
                quickSort(current+1, end)
        #quickSort(0, len(nums)-1)
        nums.sort()  # 自己写的快排会超时
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
        '''

        # 2. 哈希表   -->  O(n) & O(n)
        '''
        countDict = {}
        for e in nums:
            if e not in countDict:
                countDict[e] = True
            else:
                return e
        '''
        
        # 特判：没有重复 
        return None
