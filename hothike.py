min2=100
correct_n=False
while not correct_n:
    n_input=input()
    if n_input.isnumeric()and int(n_input)>=3 and int(n_input)<=50:
        n=int(n_input)
        correct_n=True

temp=[0 for i in range(n)]
correct_t=False
temp2=[]
while not correct_t:
    count=0
    t_input=input()
    temp=t_input.split()
    if len(temp)==n:
        for i in range(n):
            if temp[i].isnumeric()and len(temp)==n and int(temp[i])>=-20 and int(temp[i])<=40 :
                count+=1
            if count==n:
                correct_t=True
        for m in temp:
            if not(m.isalpha()):
                tem=m.split('-')
                for i in range(len(tem)):
                    if tem[i]=='':
                        temp2.append(str(-1*int(tem[i+1])))
                    if tem[i]!='' and tem[i-1]!='':
                        temp2.append(tem[i])
            temp=temp2
            correct_t=True
            
#print(temp)
min_index=0               
for i in range(len(temp)-2):
    min1=max(int(temp[i]),int(temp[i+2]))
    if min1==min2:
        compare=max(int(temp[i]),int(temp[i+2]))
        #print('no')
        if out>compare:
            min_index=i+1
            out=compare
            #print('yes')
    if min1<min2:
        min2=min1
        min_index=i+1
        out=max(int(temp[i]),int(temp[i+2]))
    
print(min_index,out)
