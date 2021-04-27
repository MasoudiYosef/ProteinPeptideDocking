import numpy as np
inp=np.zeros([8,6]);
inp[0,0:6]=[0,0,0,10.39,10.39,7.17]
for i in range(1,8):
    f1=inp[i-1,5]
    f2=inp[i-1,3]
    m=20.57
    inp[i,2]=inp[i-1,2]-(f2-f1)/(pow(2,i)*m)
    inp[i,0]=0-inp[i,2]
    inp[i,1]=inp[i,0]
    inp[i,3]=10.39+9.45*inp[i,0]+0.73*pow(inp[i,0],2)
    inp[i,4]=10.39+9.45*inp[i,1]+0.73*pow(inp[i,1],2)
    inp[i,5]=7.17+6.24*inp[i,2]-0.56*pow(inp[i,2],2)
print(inp)
    
    
