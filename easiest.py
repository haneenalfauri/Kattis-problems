list1=[]
N_valid=False

while not N_valid:
    N_input=input()
    if N_input.isnumeric() and int(N_input)>=1 and int (N_input)<=100000:
        n=int(N_input)
        found=False
        i=11
        min_value=100000000
        while not found:
            sum1=0
            sum2=0
            x=i*n
            while x>0:
                sum1+=x%10
                x=x//10
            y=n
            while y >0:
                sum2+=y%10
                y=y//10
            if sum1==sum2 :
                min_value=min(min_value,i)
                found=True
            else:
                i+=1
        list1.append(min_value)
    if N_input.isnumeric() and int(N_input)==0:
        N_valid=True
    
for j in range(len(list1)):
    print(list1[j])

