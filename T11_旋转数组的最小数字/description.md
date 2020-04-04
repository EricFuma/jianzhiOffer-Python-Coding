#### 旋转数组的最小数字

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：  
输入：[3,4,5,1,2]  
输出：1  

示例 2：  
输入：[2,2,2,0,1]  
输出：0  

&emsp;&emsp;（部分）有序数组的查找问题，肯定是倾向于用二分查找的方式将时间复杂度降至O(logn)，那么在这一题
中如何实现呢？我们仍然是要定义`left`、`mid`和`right`标签，具体步骤如下：  
- 如果 nums[left] < nums[right]，说明 nums[left:right+1] 是一个有序数组，最小值为 nums[left]  
- 如果 nums[left]==nums[mid]==nums[right]，此时我们无法通过二分法判断 nums[left:right+1] 内的情况，只能通过遍历的方式查找最小值，在实际实现的时候，我们只需要令left+=1或right-=1即可  
剔除以上两种情况，也就是 1）一定是两个递增序列  2）不会出现“连等于”，我们就可以用二分查找的方式确定数组中的最小值了：  
- 如果 nums[mid] >= nums[left]，则 mid 处在左递增序列中，最小值在右边，left = mid
- 如果 nums[mid] <= nums[right]，则 mid 处在右递增序列中，最小值在左边，right = mid

为何不用 nums[mid] >= nums[right] 来判断 mid 是否处在左递增序列中呢，看这个例子： [2 0 1 1 1]。
选择用哪个条件来判断，就看这个条件和我们的假设相比有没有漏洞，是不是符合要求。
我们的目标是令left=mid以将搜索空间减半，当 nums[mid] >= nums[left] 的时候，边界条件就是 nums[mid] == nums[left]（当nums[mid]>nums[left]时，mid一定在左序列），
那么这种条件下执行left=mid是否会让最小值丢失呢，就看 nums[mid] == nums[left] 是时候最小值是否会出现在 nums[left:mid] 中。可以用反证法：  
left   mid    right    
k......k......x  
假设left\~mid之间有个最小值m，m<k，那么mid一定在右递增序列，因为mid、right都在有序列，所以x>=k，
又因为旋转的特性，x<=k，所以x==k，则有 nums[left]==nums[mid]==nums[right]，不符合要求，所以不存在这种情况，原假设是没问题的。


同理：首先我们根据前两个条件的过滤，已经能够确保nums中一定有两个递增序列了。
对于 nums[mid] <= nums[right] 这个条件，当 nums[mid] < nums[right] 的时候，mid一定在右序列中
当 nums[mid] == nums[right] 的时候，用反证法：  
left   mid    right  
x......k......k  
如果 mid+1\~right+1 之间有最小值m，那么mid在左序列，有x<=k，又right在右序列，有 x>=k，所以有 x == k，那么
nums[left] == nums[mid] == nums[right]，不满足过滤条件，所以原假设是没有问题的。

脑子清晰后，题目也没有那么难。

题目来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
