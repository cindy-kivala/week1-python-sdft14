#You will be given a list of words, write a function to return all palindromes inside the list.
#Our code should return a list of palindromes from our determined list
#Ensure the the check allows all cases/case insensitive
#Our code should overlook punct. and whittespaces and focus on letters

def choose_palindromes(words):
     return [p for p in words if p.lower() == p.lower()[::-1]]

words_list = [
      "civic",
      "kayak",
      "racecar",
      "cookie",
      "madam",
      "cartoon",
      "noon",
      "Common",
     "deed",
     "No lemon, no melon"
]

print(choose_palindromes(words_list))

