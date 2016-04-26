__author__ = 'hzliyong'

sentence = input("Sentence:")
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2
str_leftMargin = ' ' * left_margin
print()
print(str_leftMargin + "+" + "-" * (box_width - 2) + '+')
print(str_leftMargin + "|" + " " * text_width + '|')
print(str_leftMargin + '|' + sentence + '|')
print(str_leftMargin + '|' + ' ' * text_width + '|')
print(str_leftMargin + '+' + '-' * (box_width - 2) + '+')
