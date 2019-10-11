def reverse(strng):
    word=strng.split()
    word.reverse()
    new_word=' '.join(word)
    print(new_word)

reverse('help')