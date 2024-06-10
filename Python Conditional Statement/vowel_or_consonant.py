# 15. Vowel or Consonant: Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.

# Take input from the user
character = input("Enter a single character: ")

# Check if the input is a single character
if len(character) == 1:
    character = character.lower()
    
    # Check if the input is a vowel
    if character in 'aeiou':
        print("The character is a vowel.")
    else:
        print("The character is a consonant.")
else:
    print("Please enter only a single character.")
