my_str = input("""Hello! Enter the word that you want to check if it is a palindrome or not: """)

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
   print("The word is a palindrome.")
else:
   print("The word is not a palindrome.")