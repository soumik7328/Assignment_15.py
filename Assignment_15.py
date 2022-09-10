#1. Write a python script to create a String in 3 different possible ways
a=123
print(str(a))
b=['1','2','3','4']
print(''.join(b))
c='''Soumik
Ghosh'''
print(c)
#2. Write a python script to Get the characters from the start to position 5 (Given String “iNeuron” using the slice syntax)
a="iNeuron"
print(a[0:6])
#3. Write a python script to Get the characters from position 2 to position 5 (Given String
#“Hello Learners” using the slice syntax)
a="Hello Learners"
print(a[2],a[5])
#4. Write a python script to demonstrate String Concatenation adding space in between ( Given Strings a=”Learning” b=”Python” )
a='Learning'
b='Python'
print(a+' '+b)
#5. Write a python script to get the count of total number of characters in String a=“iNeuron”
a='iNeuron'
ch=0
for e in a:
    ch=ch+1
print("Total characters is:-",ch)
#6. Write a python script to reverse a String. (“iNeuron”)
a='iNeuron'
print(a[ ::-1])
#7. Write a python script to determine whether a string contains a specific substring.
a=input("Enter a String=")
b=input("Enter a Sub-String=")
for e in range(len(a)):
    for j in range(len(b)):
        if a[e]==b[j]:
            j=j+1
            print("Substring is found at index",e)
        else:
            print("Substring Not found")    
#8. Write a python script to check if a string contains only numbers.
u="1457328"
if u.isnumeric():
    print("Yes,string contains only numbers")
else:
    print("No,string not contains only numbers")        
#9. Write a python script to check if a string contains only characters of the alphabet.
u="Soumik7328"
if u.isalpha():
    print("Yes,,string contains only characters of the alphabet"")
else:
    print("No,string not contains only characters of the alphabet"")    
#10. Write a python script to convert an integer to a string.
a=123
b=str(a)
print(b,type(b))
