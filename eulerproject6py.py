arr=[]
cval=0
sq=0
for i in range(1,100):
    arr.append(i**2)

for val in arr:
    cval += val

sq=cval**2
print("the difference between the sum and sq of sum for digits 0-1 is",sq-cval)
