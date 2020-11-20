#The first line of input contains a single positive integer T≤50
correct_T=False
while not correct_T:
    T_test=input()
    if T_test.isnumeric()and int(T_test)<=50 and int(T_test)>0:
        T=int(T_test)
        correct_T=True
Output_list=[0 for i in range(T)]

for i in range(T):
    city_list=[]
    Correct_City_Number= False
    while not Correct_City_Number:
        city_number=input()
        if city_number.isnumeric() and int(city_number)<=100:
            number=int(city_number)
            Correct_City_Number= True
    for j in range(number):
        Correct_City_Name= False
        while not Correct_City_Name:
            city_name=input()
            if city_name.isalpha() and len(city_name)<=20:
                Correct_City_Name= True
                if city_name not in city_list:
                    city_list.append(city_name)
    Output_list[i]=len(city_list)
    
for i in range(len(Output_list)):
    print(Output_list[i])
