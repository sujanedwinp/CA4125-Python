
def removeDupEl(word:str):
    newWord=""
    for ch in word:
        if ch not in newWord:
            newWord+=ch
    return newWord

strList=["banana", "apple", "mango", "strawberry"]
for i in range(0, len(strList)):
    strList[i]=removeDupEl(strList[i])

print(strList)

