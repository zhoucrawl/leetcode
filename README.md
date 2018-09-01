# leetcode
leetcode study


1.判断边界函数  return 0，return -1

2.动态规划核心-----会有子查询重复的问题，记住子查询的花销，然后依次更改。

3.动态规划创建一些空间，来存储数值

Python可变变量：list\set\dict,
当‘=’赋值时，原来变量一同改变。但是不可变量str、元祖是不会改变的

alist = [1, 2, 3]
# alist实际上是对对象的引用，blist = alist即引用的传递，现在两个引用都指向了同一个对象（地址）
blist = alist
print(id(alist), id(blist))  # id一样
# 所以其中一个变化，会影响到另外一个
blist.append(4)
print(alist)  # 改变blist, alist也变成了[1 ,2 ,3 4]
print(id(alist), id(blist))  # id一样，和上面值没有改变时候的id也一样
