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