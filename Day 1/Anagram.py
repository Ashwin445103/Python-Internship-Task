word1 = input("Enter first word:- ")
word2 = input("Enter second word:- ")

if sorted(word1) == sorted(word2):
    print("Anagram")
else:
    print("Not Anagram")