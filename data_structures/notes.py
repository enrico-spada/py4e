#slicing: up to but not including
"banana"[0:3]
# 0 -> b
# 1 -> a
# 2 -> n

################################################################################

#String Manipulation
#+ : concactenate
"ciao"+"Pino"
#ciaoPino
"ciao" + " " + "Pino"
#ciao ciao

#in : can be used to check if one string is "in" another String
"n" in "banana"
#True

if "n" in "banana" :
    print("Found it!")
#Found it!

################################################################################

"z" < "a"
#True

"Z" < "z"
#True

"Z" < "a"
#True

################################################################################

#String Library
great = "Hello Bob"
zap = greet.lower()
print(zap)
#"hello bob"

print("Hi There".lower())
#"hi there"

################################################################################

stuff = "Hello world"
type(stuff)
#<class 'str'>
#it is a type 'str'
#'class' is an object-oriented term saying this is a thing that's category string


dir(stuff) #list all possible methods for this class
stuff.capitalize()  #"abc" --> "Abc"; "ABC" --> "Abc"
stuff.center(width[, fillchar])
stuff.endswith(suffix[, start[, end]])
stuff.find(sub[, start[, end]])
stuff.lstrip([chars])
stuff.replace(old, new[, count])
stuff.lower()
stuff.rstrip([chars])
stuff.strip([chars])
stuff.upper()

#NB: methods are functions that does not change the input variable!

################################################################################

str.find(sub[, start[, end]])
#instead of returning True/False, it returns where it found it

#returns the first occurrence of the string
#if not found, returns -1

################################################################################

str.replace(old, new[, count])
#replaces all the occurences of the search string with the replacement string

################################################################################

#Sometimes we want to trim whitespaces (or other characters) at the beginning or the end or both

#by default, chars = ""
stuff.rstrip([chars])
stuff.strip([chars])
stuff.strip([chars])

################################################################################

line = "Please have a nice day"
line.startswith("Please")
#True
line.startswith("p")
#False

################################################################################

# PARSING AND EXTRACTING
data = "From stephen.marquard@uct.ac.za Sat Jan  5  09:14:16 2008"
#we want to extract the host
atpos = data.find("@")
print(atpos, data[atpos])
sppos = data.find(" ", atpos)
print(sppos, data[sppos])
host = data[atpos + 1 : sppos]
print(host)

################################################################################

# FORMAT OPERATOR
#when first term of % is a string, it has a different effect
'%d' % 42
#'42'
#The format operator applies the format of the first term to the second term

"I have spotted %d camels." % 42
#'I have spotted 42 camels.'

"In %d years I have spotted %g %s." % (3, 0.1, 'camels')
#'In 3 years I have spotted 0.1 camels.'

'%d' % 'dollars'
#%d format: a number is required, not str

################################################################################

# FILES
open(filename, mode)  #mode can be read or write, ...
#it does not read the file, it just makes it available for the code we're going to write

fhand = open('mbox.txt', 'r')
#file handle (or connections or sockets ...) is just a way to get to the data

#A File Handle open for read can be treated as a sequence of strings
#where each line in the file is a string in the sequence

#We can use For to iterate through the sequence

#NB: a sequence is an ordered set!

################################################################################

# New Line character

#\n is just one character that when print it goes in new Line
stuff = "Hello\nWorld!"
stuff
#"Hello\nWorld!"
print(stuff)
#Hello
#World!

len("X\nY")
#3     #and not 4 as we could expect! :)
"X\nY"[1]
#"\n"

################################################################################

# READING THE "WHOLE" FILE

#We can readd the whole file (newlines and all) into a singe string

fhand = open("mbox-short.txt")
inp = fhand.read()   #this does not split into lines!
print(len(inp))
print(inp[ : 20])

################################################################################

s = '1 2\t 3\n 4'
print(repr(s))
#'1 2\t 3\n 4'
#repr returns the string representation of an object!

################################################################################

# LISTS
[]

#a list element can be any Python object - even another list

friends = ['Joseph', 'Glenn', 'Sally']
friends[1]
#'Glenn'


#Strings are immutable: we cannot change the content 'Joseph'[1] = 0 ERROR
#Lists are mutable: we can change an element using the index operator

#len() tells us the number of elements of any set or sequence
len(friends)
#3

#range() returns a list of numbers that range from zero to one less than the parameter
print(range(4))
#[0, 1, 2, 3]
print(range(len(friends)))
#[0, 1, 2]


#+: concatenate lists like Strings
[1, 2, 3] + [1, 2, 3]
#[1, 2, 3, 1, 2, 3]

#slicing: the second parameter is "up to but not including"
friends[0 : 1]
"Joseph"

dir(list)

#create empty list
stuff = list()
stuff.append("Cookie")

#Since lists are mutable, str.append() method actually change the variable!

################################################################################

#List: linear collection of values that stay in order

# DICTIONARIES --> key-value pair
#a "bag" of values, each with its own label

#Dictionaries are like lists except they use keys instead of numbers to look up values


purse = dict()
purse["money"] = 12   #list to list.append()
purse["candy"] = 3
purse["tissues"] = 75
print(purse)
#{'money': 12, 'candy': 3, 'tissues': 75}
print(purse["candy"])
#3
purse["candy"] = purse["candy"] + 2
print(purse["candy"])
#{'money': 12, 'candy': 5, 'tissues': 75}


purse = {"money": 12, "candy": 3, "tissues": 75}
print(purse)
#{'money': 12, 'candy': 3, 'tissues': 75}


ccc = dict()
print(ccc["csev"])
#KeyError: 'csev'

#Better to use in operator
"csev" in ccc
#False


#get method
#find if a key is present in the dictionary, else assign a default value
counts[name] = counts.get(name, 0)


#key and values
#we can convert dict to lists but loose some information..
purse = {"money": 12, "candy": 3, "tissues": 75}
print(list(purse))
#["money", "candy", "tissues"]
print(purse.keys())
#["money", "candy", "tissues"]
print(purse.values())
#[12, 3, 75]
print(purse.items()) #results in a LIST composed of TUPLES --> immutable
#[("money", 12), ("candy", 3), ("tissues", 75)]   #("candy", 3) is a tuple

################################################################################

# DEBUGGING

#write sanity check: to see if solution is completely illogical
    #e.g. means is less than minimum value
#write consistency check: compare results of different computations

################################################################################

# FORMATTING
print ("So, you're %r old, %r tall and %r heavy.") % (age, height, weight)
print("So, you're {} old, {} tall and {} heavy.".format(age, height, weight))


################################################################################

# TUPLES: UNmodifiable lists           (note strings are also immutable)
#tuples are a limited version of lists --> more efficient version


#WE USE TUPLES WHEN WE ARE MAKING "TEMPORARY VARIABLES"


x = ("Glenn", "Sally", "Joseph")
x[0]
#"Glenn"

y = "ABC"
y[1] = "D"
#'str' object does not support item assignment

x = ("Glenn", "Sally", "Joseph")
x[1] = "Mimmo"
#'tuple' object does not support item assignment

#tuples are efficient because they are not mutable (can be stored more densily than lists)

#Tuples you CAN'T:
    #sort
    #append
    #extend
    #reverse
    #...

t = tuple()
dir(t)
#['count', 'index ']

################################################################################

# HOW CAN WE USE TUPLES

#1) Multiple assignment
(x, y) = (4, "fred")
print(y)
#'fred'
#we can also omit parenthesis
a, b = 98, 99

#2) Comparison
(0, 1, 2) < (5, 0, 0)
#True    --> it just compares the first element of the two tuples
(0, 1, 200000) < (0, 3, 4)
#True    --> if the first element of the two tuples matches, it compares the second element
("Jones", "Sally") < ("Jones", "Sam")
#True    --> same line of reasoning

#3) Exploit properties of point 2) to: Sorting Lists of Tuples
d = {"a": 10, "b": 1, "c": 22}
d.items()
#dict_items([("a", 10), ("b", 1), ("c", 22)])
sorted(d.items())
#[('a', 10), ('b', 1), ('c', 22)]

#4) Key in dictionaries
#since TUPLES are hashable and LISTS are # NOT
#TUPLES can be used as Key in dictionaries
directory[(last, first)] = 5
#or also directory[last, first]

#5) It is best practice to pass sequence in the structure of TUPLE for input to functions
#because it reduces the potential for unexpected behaviour due to aliasing

################################################################################


################################################################################
