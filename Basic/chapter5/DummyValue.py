__author__ = 'hzliyong'

word = input('Please enter a word:')
while word:
    print('The word was ' + word)
    word = input('Please enter a word:')

while True:
    word = input('Please enter a word:')
    if not word:
        break
    print(word)
