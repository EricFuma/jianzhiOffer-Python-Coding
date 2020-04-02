
#### 用两个栈实现队列  
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]

###### 方法1：脑子没捋清楚式  
&emsp;&emsp;题目要求是用两个“后进先出”的栈（stack）实现一个队列（queue）的功能——“先进先出”。一开始是这么想的：  
- 插入的时候不用管了，按需存储进去就好了，管他先进先出还是后进后出，因为我没有出啊，所以只需要一个stack就好了（用list的append操作即可），记为`stack1`。但当需要删除的时候，就需要利用到第二个栈stack2了，方法是我们可以将stack1中的所有元素出栈并依次存入stack2中，那么只需要弹出stack2栈顶元素，就是删除队列的第一个元素了（负负得正，逆序逆序为正序）。  
- 这时候“精彩”的地方就来了，我在每一步删除操作中，都执行这样的操作步骤“stack1所有元素-->stack2-->弹出stack2栈顶元素-->stack2所有元素在还原回stack1”，真的好傻啊。    

这个时候有没有问自己：每删除一个元素，时间复杂度都是稳定的`O(2n)`，合理吗？有必要吗？可以避免吗？

###### 方法2：书中的做法
&emsp;&emsp;元素入队仍然是压入stack1，元素出队依然是stack2栈顶元素弹出。如果删除操作的时候stack2中没有元素，就把stack1中的所有元素弹出并压入stack2。  
那stack1没有复原怎么办？为啥要复原啊，就当它是一个队列的元素分别存储在两个栈中不行吗，每个元素之间的相对顺序又没有破坏。。。真是醉了。


#### 进阶题：用两个队列实现栈结构
- 入栈：没啥好说的，就用一个queue来存储就好了
- 出栈：这就没办法了，我能想到的就是按照原题方法1我那种不断“还原”的方式来做，具体流程如下  


初始条件：self.queue1, self.queue2
入栈val：判断哪个queue非空，将val放入非空的那个queue中  
出栈：   判断哪个queue非空，假设queue1非空，就把queue1中的元素出队并存入queue2中，知道queue1中元素只有一个，就把这最后一个元素出队并返回，相当于是元素由queue1转到了queue2中。




来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof

