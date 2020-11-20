final=[]
stop=False
count=0
break2=False
while not stop:
    correct_n=False
    while not correct_n:
        n_input=input()
        if n_input.isnumeric()and int(n_input)>=0 and int(n_input)<16:
            if int(n_input)>=1:
                n=int(n_input)
                correct_n=True
            else:
                break2=True
                break
        else:
            print('please enter valid input n')
    name_list1=[]
    name_list2=[]
    if break2:
        break
    for i in range(n):
        correct_name=False
        while not correct_name:
            name_input=input()
            if name_input.isalpha()and len(name_input)>0 and len(name_input)<26:
                correct_name=True
                if(i%2==0):
                    name_list1.append(name_input)
                else:
                    name_list2.append(name_input)
            else:
                print('please enter valid name')
    count+=1
    final.append('SET '+str(count))
    for m in name_list1:
        final.append(m)
    for m in name_list2[::-1]:
        final.append(m)
      
    
for i in range(len(final)):
    print(final[i])
