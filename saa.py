from math import exp,pow,sqrt
import time

time_start=time.time()

def f0(n,x1,r):
    sum=0
    for j in range(1,n+1):
        sum=sum+x1*pow(r,j-1)
    
    sum=sum-1
    return sum

def f1(q,x1,r,quantile):
    sum=0

    for j in range(1,q+1):
        sum=sum+x1*pow(r,j-1)
    
    sum=sum-quantile
    return sum

def d_f0_x1(n,r):
    sum=0
    for j in range(1,n+1):
        sum=sum+pow(r,j-1)
    
    return sum

def d_f0_r(n,r,x1):
    sum=0
    for j in range(1,n+1):
        sum=sum+x1*(j-1)*pow(r,j-2)
    
    return sum

def d_f1_x1(q,r):
    sum=0
    for j in range(1,q+1):
        sum=sum+pow(r,j-1)
    
    return sum

def d_f1_r(q,r,x1):
    sum=0
    for j in range(1,q+1):
        sum=sum+x1*(j-1)*pow(r,j-2)
    
    return sum

def newton(n,q,x1,r,quantile,err):
    # alpha1=alpha
    # beta1=beta
    while abs(f0(n,x1,r))>err:

        one=f0(n,x1,r)*d_f1_r(q,r,x1)-f1(q,x1,r,quantile)*d_f0_r(n,r,x1)
        two=f1(q,x1,r,quantile)*d_f0_x1(n,r)-f0(n,x1,r)*d_f1_x1(q,r)
        three=d_f1_x1(q,r)*d_f0_r(n,r,x1)-d_f0_x1(n,r)*d_f1_r(q,r,x1)
        
        # print([one,two,three])

        if three==0:
            return [0,0]
        x1=x1+one/three
        r=r+two/three
        # print(f0(n,x1,r))
        # if f0(n,x1,r)==False:
        #     return [0,0]
        # if alpha<0 or beta<0:
        #     return [0,0]
    
    return [x1,r]


n=100
quantile=0.9
q=0
k=0
l=0






err=0.001
distributioins=[]


while l<=n:
    while k<=l:
        q=k
        while q<=l:
            tmp=[0 for i in range(n+1)]
            
            newN=l-k+1
            newQ=q-k+1
            print([k,q,l])
            
            
            # if newN==0 or newQ==0:

            #     v=v+1
            #     continue
            # elif newK==0:
            #     alpha=newtonAlpha(newK,newL,e,a,1,err)
            #     beta=1
            # elif newL==0:
            #     v=v+1
            #     continue
            try:

                [x1,r]=newton(n,q,1,1,quantile,err)
            except:
                q=q+1
                continue
            # if alpha==0 or beta==0:
            #     v=v+1
            #     continue
            # if alpha+beta>0:
            #     v=v+1
            #     continue
            # row=funRow(newK,newL,alpha,beta)
            
            
            
            for j in range(newN):
                tmp[j+k]=x1*pow(r,j)
            
            if abs(1-sum(tmp))>0.01:
                q=q+1
                continue
            distributioins.append({
                'q':q,
                'x':tmp
            })
            print([x1,r])
            print(tmp)
            q=q+1
        if k==l:
            k=0
            break
        else:
            k=k+1
    l=l+1


def tackle(distributioins):
    WMS=True
    bestDistribution=[]
    for i in distributioins:
        tmpQ=i['q']
        tmpX=i['x']
        left=0
        right=0
        for j in range(len(tmpX)):
            if j<tmpQ:
                left=left+j*tmpX[j]
            elif j>tmpQ:
                right=right+j*tmpX[j]
        
        tmpWMS=(right-left)*tmpX[tmpQ]
        if WMS==True:
            WMS=tmpWMS
            bestDistribution=i
        elif WMS>tmpWMS:
            WMS=tmpWMS
            bestDistribution=i
    print(bestDistribution)

tackle(distributioins)

time_end=time.time()
print('totally cost',time_end-time_start)

