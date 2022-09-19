word = input()
valid = False
# both 'a' and 'z' are in lower case
if 'a' <= word[0] <= 'z':
    if word[0] == word[-1]:
        valid = True
print(valid)