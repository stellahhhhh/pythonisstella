a,b,c=10,20,30
if a>=b and b>=c:
    print("a is largest")
if b>=c and c>=a:
    print("b is greater")
if c>=a and c>=b:
    print("c is greater")

print(max(a,b,c))