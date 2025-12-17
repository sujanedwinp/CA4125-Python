
word=input("Enter string: ")

revWord=""
for ch in word:
    revWord=ch+revWord

print(f"Orginal Word: {word}")
print(f"Slice Reversed: {word[::-1]}")
print(f"Loop Reversed: {revWord}")

