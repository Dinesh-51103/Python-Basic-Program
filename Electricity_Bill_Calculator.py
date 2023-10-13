# Variables containing price and rate for each slabs
rate1 = 1.50
rate2 = 2.00
rate3 = 3.00
rate4 = 3.50
rate5 = 4.60
rate6 = 6.60
fixed_rate1 = 20
14
fixed_rate2 = 30
fixed_rate3 = 50
# Calculating the EB bill based on TNEB standards
unit=int(input("Enter The Electricity Consumed in Units:"))
amount=0
if unit<=100:
 print("No Amount is Charged in accordance with 100 units free scheme")
elif unit>100 and unit<=200:
 amount=((unit-100)*rate1)+fixed_rate1
elif unit>200 and unit<=500:
 amount=(100*rate2)+((unit-200)*rate3)+fixed_rate2
else:
 amount=(100*rate4)+(300*rate5)+((unit-500)*rate6)+fixed_rate3
print("Amount To Be Payed For The Given Units is:",amount)