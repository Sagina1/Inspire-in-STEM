# palindrome
word_str = "Yvonne"
word_str = word_str.casefold()
rev_word = reversed(word_str)

if list(word_str) == list(rev_word):
    print("word is a palindrome")
else:
    print("Word is not a palindrome")