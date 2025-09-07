s1 = input()
s2 = input()
s3 = input()

unique_chars = []
for ch in set(s1 + s2 + s3):
    count = (ch in s1) + (ch in s2) + (ch in s3)
    if count == 1:
        unique_chars.append(ch)

print(", ".join(unique_chars))
