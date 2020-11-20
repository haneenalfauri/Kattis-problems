#The first line of input contains the fire safety limit 1≤L≤200
#The number of events 0≤x≤100.
correct_L=False
correct_x=False
while not correct_L and not correct_x :
    all_input=input().split()
    L_input=all_input[0]
    if L_input.isnumeric()and int(L_input)<=200 and int(L_input)>=1:
        L=int(L_input)
        correct_L=True
    x_input=all_input[1]
    if x_input.isnumeric()and int(x_input)<=100 and int(x_input)>=0:
        x=int(x_input)
        correct_x=True
total_people=0
total_number_of_groups=0
for i in range(x):
    Correct_input= False
    while not Correct_input:
        input_value=input().split()
        if str(input_value[0]).isalpha() and input_value[1].isnumeric():
            if input_value[0]=='enter':
                if total_people+int(input_value[1]) <=L:
                    total_people+=int(input_value[1])
                else:
                    total_number_of_groups+=1
                Correct_input= True   
            elif input_value[0]=='leave':
                if total_people>0:
                    total_people-=int(input_value[1])
                    Correct_input= True
                
    
print(total_number_of_groups)
