# list containing the words with correct spelling
num=['ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT', 'NINE','TEN']
w=input("Enter The Number Name:")
w=w.upper()
word=[]
c=[]
# Everytime the a letter in the input is found in one of the words, their corresponding integer count is incremented
for i in range(len(num)):
 e=num[i]
 if len(w) == len(e):
    word.append(e)
for i in word:
 count=0
 for j in range(len(w)):
    if w[j] == i[j]:
        count+=1
#checking the counter value to print correct spelling
 if count == (len(w)-1):
    print("The Correct Number Name Is:",i)