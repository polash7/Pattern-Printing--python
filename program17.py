'''
Pattern printing

*
***
*****
*******
*********

'''

n = int(input("you text number : "))
q = str(input("your text item : "))

for i in range(n+1):
    print((i*2-1)*q)

