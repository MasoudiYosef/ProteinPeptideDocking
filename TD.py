f=open('DT.txt','r');
l=f.readline()
Base_info=[]
while len(l)>0:
    k=l.split('\t')
    n1=[]
    for i in range(0,len(k)):
        if len(k[i])>0:
            n1.append(k[i])
            if len(n1)>11:
                break;
    Base_info.append(n1)
    l=f.readline()
f.close()
nf=open("base.txt",'w');
for i in range(0,len(Base_info)):
    nf.write(str(Base_info[i])+"\n")
nf.close()
