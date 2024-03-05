def palindrome(word):
    word = word.lower()
    return word == word[::-1]


print(palindrome("racecar"))
print(palindrome("radar"))
print(palindrome("belalugosi"))
