number=[3,5,6,10,12,21,-7]
higher=number[0]
second_higher=number[higher]
lower=number[0]
second_lower=number[lower]

for num in number:
    if num > higher:
        higher=num
    if second_higher<higher:
        second_higher=num
    if num < lower:
        second_lower=num
    if num < second_lower:
        second_lower=num
print("higher & second_higher is :",higher,second_higher)   
print("lower & second_lower is :",lower,second_lower)   
