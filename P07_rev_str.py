
word="0123456789"

revWord=""
for ch in word:
    revWord=ch+revWord

print(f"Orginal Word: {word}")
print(f"Slice Reversed: {word[-1:-5:-1]}")
print(f"Loop Reversed: {revWord}")

