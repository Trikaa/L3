def check(a, word):
    for key, value in a.items():
        for words in value:
            if word == words:
                print (key)
a = {
     'apple': ['malum', 'pomum', 'popula'],
     'fruit': ['baca', 'bacca', 'popum'],
     'punishment': ['malum', 'multa']
    }
word = input()
check(a, word)





