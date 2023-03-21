vals = [0,1]
answer=0
while vals[-1]+vals[-2] < 4000000:
    vals.append(vals[-1]+vals[-2])
    

for i in vals:
    if i % 2 ==0:
        answer += i
