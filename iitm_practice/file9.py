word = input()
match = False
if word.count('(') == word.count(')'):
    if word.count('[') == word.count(']'):
        if word.count('{') == word.count('}'):
            match = True
if match:
    print('PERFECT!')
else:
    print('IMPERFECT!')