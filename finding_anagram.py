# Following instructions in the LMS, this method seem more appropriate
# METHOD 1

def find_anagrams(*args):
    stripd_string=word.strip()
    sorted_word=sorted(stripd_string)
    stripd_test_string=test_word.strip()
    sorted_test_word=sorted(stripd_test_string)
    if sorted_word==sorted_test_word:
        return True
    else:
        return False

word=input('Enter a string:')
test_word=input('Enter a test string:')

if find_anagrams(word,test_word)== True:
    print('The words are anagrams')
else:
    print('The words are not anagrams')

print()
print()

# While following the guide (skeleton) found in the main.py file, this method somewhat fits better
# METHOD 2

def find_anagrams(word):
    sorted_word=sorted(word)
    return sorted_word

word=input('Enter a word:')
test_word=input('Check if this is an anagram:')
sorted_test_word=sorted(test_word)

if find_anagrams(word)==sorted_test_word:
    print('The words are anagrams')
else:
    print('The words are not anagrams')

# Both methods outputs the same result
