my_sentence = "pythpon is fun and powerful"
print(len(my_sentence))

print(my_sentence[0])

print(my_sentence[10:26])

print(my_sentence.lower())

print(my_sentence.count('o'))

print(my_sentence.find('fun'))

my_sentence.replace('powerful', 'amazing')
print(my_sentence)

new_message = "learning python is exciting!"

sentence =my_sentence + new_message
print(sentence)

sentence = my_sentence + ',' + new_message
print(sentence)

sentence = f'{my_sentence} {new_message}'
print(sentence)

print(dir(sentence))

print(help(str.replace))

