# leetcode
leetcode study


1.判断边界函数  return 0，return -1

2.动态规划核心-----会有子查询重复的问题，记住子查询的花销，然后依次更改。

3.动态规划创建一些空间，来存储数值

-------------------------------------------------------------------
1.https://www.cnblogs.com/sun-haiyu/p/7096918.html
Python可变变量：list\set\dict,
当‘=’赋值时，原来变量一同改变。但是不可变量str、元祖是不会改变的

alist = [1, 2, 3] # alist实际上是对对象的引用，blist = alist即引用的传递，现在两个引用都指向了同一个对象（地址）
blist = alist
print(id(alist), id(blist))  # id一样 # 所以其中一个变化，会影响到另外一个
blist.append(4)
print(alist)  # 改变blist, alist也变成了[1 ,2 ,3 4]
print(id(alist), id(blist))  # id一样，和上面值没有改变时候的id也一样

---------------------------------------------------------------
2.can only assign an iterable,整数没有办法迭代
lis = range(10)
lis[:] = range(5) 
lis               #all items of `lis` replaced with range(5)
  [0, 1, 2, 3, 4]

lis[:] = 5        #Non-iterable will raise an error.
Traceback (most recent call last):
  File "<ipython-input-77-0704f8a4410d>", line 1, in <module>
    lis[:] = 5
TypeError: can only assign an iterable

lis[:] = 'foobar' #works for any iterable/iterator
lis
   ['f', 'o', 'o', 'b', 'a', 'r']
   
 3.https://www.cnblogs.com/lemonbit/p/6864179.html
 np.random.randint(low,high,取多少个)
 high取不到
 
 4.list.extend()将列表中数值放进去,而extend方法只能接收list，且把这个list中的每个元素添加到原list中。


5.https://blog.csdn.net/charles_neil/article/details/78940831
数组切片
