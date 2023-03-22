#create list, add only even prime so we can skip the rest
primes = [2]
counter=1

for i in range(3,999999999999999,2):
    limit=i**(1/2)+1
    factorfindercount = 0
    for j in range(3,int(limit),2):
        factorfindercount+=1
        if i % j == 0:
            break
    else:
        primes.append(i)
        counter+=1
        
    if counter == 10001:
        break

print("the 10001st prime is",primes[-1])

