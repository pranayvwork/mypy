message = 'My Wolrd'
print(message)
#apostrophe 
myString = "Cat's world"
print(myString)
#multi line string literal
longString = """This is a multi line string
spanning to the second line. """
print(longString)
#find the length of string
print(len(myString))
#upper or lower
print(myString[6:].upper())
#count method
print(myString.count('r'))
#replace method 
print(myString.replace('Cat\'s', 'Bobby\'s'))
print(myString)
greeting = "hello"
name = "john"
#concat string
message = greeting + ", " +  name
print(message)
#formatted string
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)
#using formatting with f strings
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)
#find what all methods can be applied on a variable
print(dir(message))