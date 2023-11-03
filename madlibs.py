import random
personName=input('Name:')
cityName=input('City:')
hobbyName=input('Hobby:')
heroName=input('Hero:')

mablibs=f"My name is {personName} and I am from {cityName}.I Love to play {hobbyName}\n and when i am playing ,it feels like i am {heroName} "
print(mablibs)


# List of words inputted by the user
words = []

# Ask the user to input words
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb: ")


# Mad Libs template with placeholders
mad_libs_template = f"The {adjective}  {noun} is {verb} {adverb}."
# Shuffled words list
words = [adjective, noun, verb, adverb]
random.shuffle(words)

# Mad Libs template with shuffled placeholders
shuffled_mad_libs = f"The {words[0]} {words[1]} is {words[2]} {words[3]}."
# Print the original and shuffled Mad Libs
print("Original Mad Libs: ", mad_libs_template)
print("Shuffled Mad Libs: ", shuffled_mad_libs)
