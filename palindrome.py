#You will be given a list of words, write a function to return all palindromes inside the list.
#Our code should return a list of palindromes from our determined list
#Ensure the the check allows all cases/case insensitive
#Our code should overlook punct. and whittespaces and focus on letters

def choose_palindromes(words):
     #return [p for p in words if p.lower() == p.lower()[::-1]]
     palindromes = [] #our list of palindromes
     # Iterate through each word in the list

     #1. lowercase the word
     for p in words:
         cleaned_word = p.lower()
     #2. Spaces
         cleaned_word = ''.join(filter(str.isalnum, cleaned_word))
     #3. Check if the cleaned word is a palindrome
         if cleaned_word == cleaned_word[::-1] and cleaned_word != '':
             palindromes.append(p)

     return palindromes

words_list = [
      "civic",
      "kayak",
      "racecar?",
      "cookie",
      "madam",
      "cartoon",
      "noon",
      "Common",
     "deed",
     "No lemon, no melon!"
]

print(choose_palindromes(words_list))

