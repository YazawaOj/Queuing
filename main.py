import numpy as np
import matplotlib.pyplot as plt

v=(1,1)#到达速率
u=(1,1)#窗口服务速率
M=(1,1)#柜员人数
L=(1,1)#队列初始人数
Mbusy=(1,1)#初始时刻正在服务的柜台数
#0为银行,1为药店

def randExp(v):
    return np.random.exponential(1/v)

def simulation(a,b):
    '''
    单次仿真先去a后去b的情况下所花费的时间
    '''
    global v,u,M,L,Mbusy
    t=0#时间
    Q=[L[a],L[b]]#队列人数Q(t)
    Q[0]=L[a]+Mbusy[a]-M[a]
    while True:
        if(Q[0]<0):break
        t+=randExp(M[a]*u[a])
        Q[0]-=1
    t+=randExp(u[a])
    #在a排队+接受服务所花的时间

    Q[1]=np.random.poisson(v[b]*t)+L[b]+Mbusy[b]-np.random.poisson(u[b]*M[b]*t)-M[b]#在a的过程中b队列发生的变化
    while True:
        if(Q[1]<0):break
        t+=randExp(M[b]*u[b])
        Q[1]-=1
    t+=randExp(u[b])
    #在b排队+接受服务所花的时间
        
    return t

def main():
    times=1000#模拟次数
    total1=[]
    total2=[]#模拟结果
    while(times):
        total1.append(simulation(0,1))
        total2.append(simulation(1,0))
        times-=1
    print('先去银行得到总时间：')
    print(sum(total1)/len(total1))
    print('先去药店得到总时间：')
    print(sum(total2)/len(total2))

if(__name__=='__main__'):
    main()