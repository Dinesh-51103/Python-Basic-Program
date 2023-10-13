# A list of codes of all the letters
value = [1, 2, 3, 4, 5, 8, 3, 5, 1, 1, 2, 3, 4, 5, 7, 8, 1, 2, 3, 4, 6, 6, 6, 5, 1, 7]
# A function for sum of digits if in case the code is not single digit
def sum_of_digits(n) :
 while n >= 10 :
    n = sum([int(x) for x in str(n)])
    return n
# Function to convert name to code :
# Works as follows :
# * Traverse through the name
# * Add the respective code of each letters
# * If the final result is not single digit, sum its
# digits
def encrypt(name) :
 num = 0
 for i in name :
    num += value[ord(i) - ord('A')]
    if num >= 10 :
        num = sum_of_digits(num)
    return num
# Getting name input and print its respective code
name = input("Enter the name : ")
name = name.upper()
print(name + " : " + str(encrypt(name)))
# To print alternative names
print("\nAlternative Possible Names : ")
f = [x for x in name]
for i in name :
 f.insert(f.index(i), i)
 print(encrypt(''.join(f)) , ":", ''.join(f))
 f.remove(i)