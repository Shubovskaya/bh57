y= 3
x= range(0,100)
left = 0
right = len(x)-1
mid=int((left+right)/2)

while x[mid]!=y:
    if x[mid]>y:
        right = mid
        mid=int((left+right)/2)
    if x[mid]<y:
        left = mid
        mid=int((left+right)/2)
print(x)