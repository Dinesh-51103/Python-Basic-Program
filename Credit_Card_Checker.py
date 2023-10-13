#function to store the credit card numbers in list
def digits_of(n):
 return [int(d) for d in str(n)]
card_num=input("Enter The Card Number:")
digits = digits_of(card_num)
#partitioning the number into odd and even index
odd_digits = digits[-1::-2]
even_digits = digits[-2::-2]
checksum = 0
# Doubling the even index number and summing all the number
checksum += sum(odd_digits)
for i in even_digits:
 checksum += sum(digits_of(i*2))
if checksum%10==0:
 print('The Credit Card Number is Valid')
else:
 print('The Credit Card Number is Invalid')