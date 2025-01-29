number=[3,5,1,8,-3,7,2]
higher=number[0]
lower=number[0]
 
for num in number:
 if num > higher:
   higher=num
if num < lower:
  lower=num
  print("Lagest element is :",higher)
  print("Lower element is :",lower)