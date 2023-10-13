#function for pattern 12345 12345
def fun1(n):
 if n[0:5] == n[5:10]:
    return True
 else:
    return False
#function for pattern 12345 54321
def fun2(n):
 l=[]
 for i in range(5,10):
    l.append(n[i])
 for i in range(0,5):
    if n[i]==l[4-i]:
        return True
    else:
        return False
# function for pattern 11111 22222
def fun3(n):
    if (n[0] == n[1] == n[2] == n[3] == n[4]) and (n[5] == n[6] == n[7] == n[8] == n[9]) :
        return True
    else :
        return False
# function for pattern 11122 33344
def fun4(n) :
    if ((n[0] == n[1] == n[2]) and (n[3] == n[4])) and ((n[5] == n[6] == n[7]) and (n[8] == n[9])) :
     return True
    else :
     return False
# function for pattern 11111 23456 or 23456 11111
def fun5(n) :
    if (n[0] == n[1] == n[2] == n[3] == n[4]) or (n[5] == n[6] == n[7] == n[8] == n[9]) :
        return True
    else :
        return False
# function for pattern 12121 34343
def fun6(n) :
    if ((n[0] == n[2] == n[4]) and (n[1] == n[3])) and ((n[5] == n[7] == n[9]) and (n[6] == n[8])) :
        return True
    else :
        return False
no=input("Enter The Phone Number:")
if fun1(no) or fun2(no) or fun3(no) or fun4(no) or fun5(no) or fun6(no):
 print("The Given Phone Number is a Fancy Number ")
else:
 print("The Given Phone Number is Not a Fancy Number ")