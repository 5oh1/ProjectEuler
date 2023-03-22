answer=0
for i in range(20,99999999999999999999,20):
    for j in range(19,1,-1):
        if i % j != 0:
            break
    else:
        print(i,"is smallest int evenly divisible by [1:20]")
        break
        
        
