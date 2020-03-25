#Author： Zhong Zhuoer
#这是我的一次git的实验
#没有任何意义
import numpy as np
import math
n=int(input())
a=[0]*n#用于后面建二维列表
for i in range(0,n):
    a[i]=list(map(int,input().split()))#把输入的数据储存 并得到二维列表
kind=list(map(int,input().split()))#输入种类
y=list(map(int,input().split()))#输入待测样本
l=[]#创建一个空列表
for i in range(0,n):
    array1=np.tile(a[i],(1,1))#得到矩阵
    array2=np.tile(y,(1,1))#得到矩阵
    array3=array1-array2#两个矩阵对应元素相减
    array4=array3**2#对矩阵各元素进行平方
    l.append(math.sqrt(array4.sum(axis=1)))#得到距离并加入到集合l中
m=min(l)#得到l的最小值
print(kind[l.index(m)]) #找到最小值的位置，然后输出最小值出时的种类