import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import matrix

v=(2,2)#到达速率
u=(2,2)#窗口服务速率
M=(1,1)#柜员人数
L=(10,10)#队列初始人数，为0时分情况讨论
#0为银行,1为药店

def randExp(v):
    return np.random.exponential(1/v)

def poissonTimes(v,T):
    '''
    生成一个区间T中的速率为v的泊松过程,返回各个计数的时刻
    '''
    t=0
    ts=[]
    while True:
        t += randExp(v)
        if(t>T): break
        ts.append(t)
    return ts

def comeNum(t1,t2,ts):
    '''
    返回在ts数组中位于(t1,t2]的元素个数
    '''
    ans=0
    for i in ts:
        if t1<i and i<=t2:
            ans+=1
    return ans

def main():
    global v,u,M,L
    times=10#模拟次数
    total=[]#模拟结果
    while(times):
        t=0#时间
        Q=[L[0],L[1]]#队列人数Q(t)
        Mbusy=[1,1]#初始时刻正在服务的柜台数
        while True:
            t+=randExp(M[0]*u[0])#银行走了一个人
            Q[0]-=1
            if(Q[0]<0):break#排队排到了
        t+=randExp(u[0])#我们接受服务所花的时间
        tsbcome=poissonTimes(v[1],t)
        tout=0
        while True:
            dt=randExp(Mbusy[1]*u[1])
            if(tout+dt>t):
                break
            Q[1]+=comeNum(tout,tout+dt,tsbcome)
            if(Q[1]>0):
                Q[1]-=1
            else:
                Mbusy[1]-=1
            tout+=dt
        if Mbusy[1]<M[1]:
            t+=randExp(u[1])
        else:
            while True:
                t+=randExp(Mbusy[1]*u[1])
                Q[1]-=1
                if(Q[1]<0):break
            t+=randExp(u[1])
        total.append(t)
        times-=1
    print(sum(total)/len(total))

if(__name__=='__main__'):
    main()