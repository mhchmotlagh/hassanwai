b=[]
for i in range(8):
    b.append([])
for i in range (8):
    if i==0:
        b[i]=['r','h','f','v','k','f','h','r']
    if i==1:
        b[i]=['s0','s1','s2','s3','s4','s5','s6','s7']
    if i==6:
        b[i]=['S0','S1','S2','S3','S4','S5','S6','S7']
    if i==7:
        b[i]=['R','h','F','V','K','F','h','R']
    if 1<i<6:
        b[i]=['0']*8
for i in range (8):
    print(b[i])
rs,cs=input('rowstart and columstar (1-8):').split()
rs,cs=int(rs)-1,int(cs)-1
re,ce=input('rowend and columend (1-8):').split()
re,ce=int(re)-1,int(ce)-1
b[re][ce]=b[rs][ce]
b[rs][cs]='0'
ha=0
for i in range (8):
    for j in range (8):
        if b[i][j]=='si':
            if b[i+1][j]==0:
                ha+=1
                if b[i+2][j]==0:
                    ha+=1
        if b[i][j]=='Si':
            if b[i+1][j]==0:
                ha+=1
                if b[i+2][j]==0:
                    ha+=1
        if b[i][j]=='f':
            x,y=i,j
            while 0=<x,y<=7:
                x+=1
                y+=1
                if b[x][y]==0:
                    ha+=1
                else:
                    x,y=i,j
                    break
            while 0=<x,y<=7:
                x-=1
                y+=1
                if b[x][y]==0:
                    ha+=1
                else:
                    x,y=i,j
                    break
            while 0=<x,y<=7:
                x+=1
                y-=1
                if b[x][y]==0:
                    ha+=1
                else:
                    x,y=i,j
                    break
            while 0=<x,y<=7:
                x-=1
                y-=1
                if b[x][y]==0:
                    ha+=1
                else:
                    x,y=i,j
                    break
for i in range (8):
    print(b[i])

