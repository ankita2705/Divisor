number=int(input("Enter a number: "))
divisor_list=[]

for divisor in range(1,number+1):
    if(number%divisor==0):
        divisor_list.append(divisor)

print(divisor_list)        
