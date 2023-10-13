#reading the files and storing them in list
file_1=open('cart1.txt','r')
variable_1=file_1.read()
list_1=variable_1.split("\n")
file_2=open('cart2.txt','r')
variable_2=file_2.read()
list_2=variable_2.split("\n")
file_3=open('cart3.txt','r')
variable_3=file_3.read()
list_3=variable_3.split("\n")
cart=[]
#Getting input from the User and storing them in list
n=int(input("Enter The Number Of Item In The Cart:"))
for i in range(n):
 v=input("Enter The Name Of Product["+str(i+1)+"]:")
 v=v.upper()
 cart.append(v)
#Searching the presence of the item in different list
for i in cart:
 if i in list_1 :
    print("The GST For The Product",i,"is 5%")
 if i in list_2 :
    print("The GST For The Product",i,"is 12%")
 if i in list_3:
    print("The GST For The Product",i,"is 18%")