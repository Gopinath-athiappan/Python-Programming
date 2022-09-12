a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=int(input("enter d"))
Max = "a is max" if a>b and a>c and a>d else "b is max" if b>c and b>d else "c is max" if c>d else "d is max"
print (Max)
