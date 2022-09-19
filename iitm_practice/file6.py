L=int(input())
# L is a positive integer that has already been defined at this stage
word = input()
space = ' ' # there is a single space
if len(word) < L:
    word = 'short' + space + word
elif L <= len(word) < 2 * L:
    word = 'medium' + space + word
else:
    word = 'long' + space + word
print(word)