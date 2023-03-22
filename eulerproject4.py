answer=0
for i in range(100,999):
    for j in range(100,999):
        p = j*i
        l = len(str(p))
        m = str(p)
        fh = ""
        bh = ""
        if l % 2 == 0:
            for k in range(0,int(l/2)):
                fh = fh + (m[k])
                bh = bh + (m[-(k+1)])
            if bh == fh:
                answer=p

print(answer,"is the highest palindrome product of 2 3 digit numbers.")
            
