# 链表

我们知道用数组存放数据时，必须事先定义数组的长度（即元素个数）。当事先难以确定有多少个元素时，则必须把数组定义的足够大，以保证成功。无疑，这会造成内存浪费。因此可以考虑设计一种物理存储单元上非连续、非顺序的存储结构，来避免数组带来的问题，链表正是这样的一种数据结构。

链表由一系列结点（链表中每一个元素称为结点）组成，每个结点包括两个部分：一个是存储数据元素的数据域，另一个是存储下一个结点地址的指针域。

更多内容参考  [LinkedList](https://github.com/xuelangZF/LeetCode/tree/master/LinkedList)

# 栈

栈是一种最基本、最常用的数据结构，一个词来总结栈的特点就是后进先出。我们可以将栈看作是一个数据仓库，向栈内增加数据的操作叫入栈(push)操作，从栈内取出数据的操作叫出栈(pop)操作。不过不像一般的仓库一样，可以随意取出任何位置的物品，从一个栈取出的数据必须是最后一次增加的数据。换句话就是说，最后一个进入栈的数据，会被第一个取出来。

生活中有很多场景包含有后进先出的思想，比如刷盘子这个过程，我们将已经洗好的盘子叠在一起，每次洗好一个盘子就将堆在顶部，而我们需要用一个盘子时也是从最上面取走。

栈有许多典型应用场景，比如函数调用，表达式计算，表达式转换，模拟递归等。

更多内容参考 [Stack](https://github.com/xuelangZF/LeetCode/tree/master/Stack)  

# 堆

堆（Heap）是计算机科学中一类特殊的数据结构的统称。堆通常是一个可以被看做一棵树的数组对象。在队列中，调度程序反复提取队列中第一个作业并运行，因为实际情况中某些时间较短的任务将等待很长时间才能结束，或者某些不短小，但具有重要性的作业，同样应当具有优先权。堆即为解决此类问题设计的一种数据结构。

更多内容参考 [Heap](https://github.com/xuelangZF/LeetCode/tree/master/Heap)

# Hashtable

哈希表就是一种以键-值(key-indexed) 存储数据的结构，我们只要输入待查找的值即 key，即可查找到其对应的值。例如若关键字为k，则其值存放在 f(k) 的存储位置上，由此不需比较便可直接取得所查记录。称这个对应关系 f 为散列函数，按这个思想建立的表为哈希表（散列表）。

哈希查找第一步就是使用哈希函数将键映射成索引，这种映射函数就是`哈希（散列）函数`。哈希函数需要易于计算并且能够均匀分布所有键。一个好的哈希函数必须在理论上非常的快、稳定并且是可确定的。
	
对不同的关键字可能得到同一散列地址，即k1 != k2，而f(k1)=f(k2)，这种现象称为冲突（Collision），避免hash碰撞碰撞的方法有：拉链法，开放定址法，再散列，建立一个公共溢出区等。

更多内容参考  [HashTable](https://github.com/xuelangZF/LeetCode/tree/master/HashTable)

# 树

树（Tree）是n（n≥0）个有限数据元素的集合。当n＝0 时，称这棵树为空树。在一棵非空树T 中：

1. 有一个特殊的数据元素称为树的根结点，根结点没有前驱结点。
2. 除根结点之外的其余数据元素被分成m（m>0）个互不相交的集合T1，T2，…，Tm，其中每一个集合Ti（1≤i≤m）本身又是一棵树。树T1，T2，…，Tm 为这个根结点的子树（subtree）。

二叉树是`每个节点最多有两个子树`的树结构。二叉树的每个结点至多只有二棵子树，二叉树的子树有左右之分，次序不能颠倒。

二叉查找树，也称排序二叉树，是指一棵空树或者具备下列性质的二叉树(每个结点都不能有多于两个儿子的树)：

1. 若任意结点的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
2. 若任意结点的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
3. 任意结点的左、右子树也分别为二叉查找树；
4. **没有键值相等的结点**。

更多内容参考 [BS_Tree](BS_Tree.md)

AVL树是最早提出的`自平衡二叉树`，它是一种特殊的二叉搜索树，任一节点的左子树深度和右子树深度相差不超过1，所以它也被称为高度平衡树。

更多内容参考 [AVL_Tree](AVL_Tree.md)

红黑树是一种自平衡二叉查找树。它的统计性能要好于平衡二叉树（AVL树），因此，红黑树在很多地方都有应用。在C++ STL中，很多部分(目前包括set, multiset, map, multimap)应用了红黑树的变体(SGI STL中的红黑树有一些变化，这些修改提供了更好的性能，以及对set操作的支持)。它是复杂的，但它的操作有着良好的最坏情况运行时间，并且在实践中是高效的: 它可以在O(log n)时间内做查找，插入和删除等操作。

更多内容参考 [RB_Tree](RB_Tree.md)

# 图

图（Graph）是由顶点的有穷非空集合和顶点之间边的集合组成，通常表示为：G(V,E)，其中，G表示一个图，V是图G中顶点的集合，E是图G中边的集合。 

更多内容参考 [Graph](https://github.com/xuelangZF/LeetCode/tree/master/Graph/README.md)

# bitmap

位图（bitmap）是一种非常常用的结构，在索引，数据压缩等方面有广泛应用，能同时使存储空间和速度最优化。例如可用一个10位长的字符串来表示一个所有元素都小于10的简单的非负整数集合，可以用 `01110100100` 表示集合 {1,2,4,5,8} ，对应位置数字存在标记为1，否则标记为0。

C 语言位图实现如下：

![][1]

主要程序如下：

    #define SHIFT 5  
    #define MASK 0x1F  

    //set 设置所在的bit位为1  
    //clr 初始化所有的bit位为0  
    //test 测试所在的bit为是否为1  
    
    set(int i) {
        a[i>>SHIFT] |=  (1<<(i & MASK)); }  
    clr(int i) {
        a[i>>SHIFT] &= ~(1<<(i & MASK)); }  
    test(int i){
        return a[i>>SHIFT] & (1<<(i & MASK)); } 

字节位置=数据/32 (采用位运算即右移5位)  
位位置=数据%32   (采用位运算即跟0X1F进行与操作)。

特定适用场合：

1. 对10亿个不重复的整数进行排序。
2. 找出10亿个数字中重复的数字。

如果用普通的排序算法，数据放进内存就需要 ( 10^9 * 4)/( 2^30 ) = 3.7G。改用 Bitmap 的话，一个数字占一位，一共需要 3.7/32 ＝ 0.1 G 内存。


# 更多阅读

《剑指 Offer》  
[树、森林与二叉树的转换](http://c.biancheng.net/cpp/html/987.html)  
[数据结构之树](http://c.biancheng.net/cpp/u/shuju7/)  
[轻松搞定面试中的二叉树题目](http://blog.csdn.net/luckyxiaoqiang/article/details/7518888)  
[卡特兰数](https://zh.wikipedia.org/wiki/卡塔兰数)  
[详解bitmap算法](http://www.wjxfpf.com/2015/10/300404.html)  
[浅谈算法和数据结构: 十一 哈希表](http://www.cnblogs.com/yangecnu/p/Introduce-Hashtable.html)  
[哈希碰撞](http://alexyyek.github.io/2014/12/14/hashCollapse/)  



[1]: https://cs-offer-1251736664.cos.ap-beijing.myqcloud.com/DataStructure_1.jpg
