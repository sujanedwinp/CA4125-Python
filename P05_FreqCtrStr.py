
sen=input("Enter String: ")
charFreq={}
for x in sen:
    if x not in charFreq.keys():
        charFreq[x]=1
    charFreq[x]=charFreq[x]+1

for i,v in charFreq.items():
    print(f"{i} : {v}")
