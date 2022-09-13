n = int(input())
if n%2==0 and (n>=2 and n<=6) :
    print ('Not Weird')
elif n%2==0 and (n>=6 and n<=20) :
    print ('Weird')
elif n%2 ==0 and (n>20) :
    print ('Not Weird')
elif n%2 ==1 : print ('Weird')

#print ('Not Weird') if n%2 <1 and (n>=2 and n<=6) else print ('Weird') if n%2 <1 and (n>=6 and n<=20) else print ('Not Weird') if n%2 <1 and (n>20) else print ('Weird')
