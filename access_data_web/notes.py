
# REGULAR EXPRESSIONS

Python Regular Expression Quick Guide

^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times
         (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times
         (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end

# re.findall(r'\w+', open('hamlet.txt').read().lower())
#r' means the expression is a raw string for which escape sequences are not parsed
#"[\\w]" is equivalent to r"[\w]"
################################################################################

#they are not built-in
import re

#returns a True/False depending on the string matches the regex --> similar to str.find()
re.search()

#EXTRACT portion of string that match the regex --> similar to combine find() and slicing
re.findall()

################################################################################

#Wildcards

"^X.*:"
#The line starts with char 'X'
#followed by any character (.) any number of times (*)
#followed by char ":"

################################################################################

#[] matches one character
#[0-9] matches one digit!
#[0-9]+ matches multi-digit numbers

import re
x = "My 2 favourite numbers are 19 and 42"
print(x)
#My 2 favourite numbers are 19 and 42
y = re.findall("[0-9]+", x)
print(y)
#['2', '19', '42']   note it returns a list of STRINGS
y = re.findall("[AEIOU]+", x)
print(y)
#[]         #there are no upper case VOWEL

################################################################################

#Warning: GREEDY MATCHING   --> as large possible string

#The repeat characters (* and +) push to match the largest possible string!
import re
x = "From: Using the : character"
print(x)
y = re.findall("^F.+:", x)
print(y)
#['From: Using the :']     #!! it does not stop at the first ":"

################################################################################

#Non-Greedy Matching   --> add the ?
import re
x = "From: Using the : character"
print(x)
y = re.findall("^F.+?:", x)
print(y)
#['From:']

#First character is 'F'
#any character (.) one or more times (+)
#but don't be greedy (?)

################################################################################

#Escape character

#use \
#to make a regex beahave as normal character

################################################################################

# NETWORKED TECHNOLOGY

#we use socket!
#to connect to a TCP/IP port

#Commonly, we can expect the following TCP ports (but they can differ):
        #Telnet - 23: login
        #SSH - 22: secure login
        #HTTP - 80
        #HTTPS - 443: secure
        #SMTP - 25: mail
        #IMAP - 143/220/993: mail retrieval
        #POP - 109/110: mail retrieval
        #DNS - 53: domain name
        #FTP - 21: file transfer

################################################################################

#Sockets in Python

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#The connection happens when we call the .connect() method
mysock.connect( ("data.pr4e.org", 80) )   #(host, port)

################################################################################

#HTTP
#set of rules that allows browsers to retrieve web documents from servers over the internet
#with HTTP: first you send to server and after you receive from the server


# http://            protocol
# www.dr-chuck.com   host
# /page1.htm        document

#href = value     when you click on a href object and interacts with the page
    #it issues a GET request  --> GET the content of the page at the specific URL


#usually, it is the browser to take care of the socket and parse what it retrieves from GET request

#Request
# GET http://www.dr-chuck.com/page1.htm HTTP/1.0
# GET URL                               Protocol/Version

################################################################################

#HTTP Request

#First you receive metadata
#then you receive the data

#if in metadata status: 200 then you are good
#if in metadata status: 404 then page not found
#if in metadata status: 302 then you are being redirected to the correct page

#Content-type header: can be text, jpeg, ...

################################################################################

#Representing simple string

#Each char is represented by a number between 0 and 256 stored in 8 bits of memory

print(ord('H'))
#72   ASCII
print(ord('e'))
#101
print(ord('\n'))
#10


#UNICODE/UTF: overcome ASCII (American) representation to include all languages
#...but in UNICODE/UTF each character requires more than 1 byte!

#UTF-8 is reccomended practice for encoding data to be exchanges between systems
#note that UTF-8 overlap with ASCII ;)
#each char can require between 1 (ASCII) up to 4 byte

################################################################################

#Type of STRINGS
x = 'abc'   #regular string
type(x)
#str
x = u'abc'  #unicode string
type(x)
#str
x = b'abc'  #bytes string (1 byte per character)
type(x)
#bytes      #this string is raw, unencoded. It might be UTF-8, UTF-16, ASCII. WE DON'T KNOW WHAT ITS ENCODING IS

#This is something we have to manage when dealing with data from outside
#however, decoding is relatively simple because 99% of the stuff is UTF-8


#NB: In Python 3, all strings internally are UNICODE

################################################################################

# WEB SERVICES AND XML

#When data leaves your system to go through the web, you SERIALIZE them
#serialization: transform data in a more general format that can be read from any system

#When data arrives to destination system, they are DESERIALIZED
#deserialization: convert serialize data (general format) to format used in the other system

################################################################################

#serialization
#1) XML
#2) JSON  --> more modern
#3) ...

#XML: eXtensible Markup Language
#it works similarly to HTML because it uses tags
# <person>
#     <person>
#         <name>Chuck</name>
#         <phone>1234 5678</phone>
#     </person>
# </person>

#simple element: basic component with no child
#complex element: components with at least one child
#identing is not relevant


#The standard XML schema to be used is defined by W3C and is called XSD (S stands for Schema)
#remember the schema is used to validate and accept the XML content
    #we can see the schema as the structure/onstraints of the XML content

################################################################################

#Parsing XML

import xml.etree.ElementTree as ET

################################################################################

# JSON AND REST ARCHITECTURE

#JSON: JavaScript Object Notation

#XML is very powerful and in simple situation it can be more than we need

#JSON represents data as nested "lists" and "dictionaries" --> easier to use


#Use XML ONLY if you are dealing with something very complex that does not work with JSON

################################################################################

#Service Oriented Approach:
#the data in each application is offered up as a service which any other application can consume
    #APIs:  ways to use web protocols to access data on systems, using well defined
    #       and structured approaches
    #APIs consists of a service layer to offer data in a common format reusable elsewhere
    #the strenght is that new or different applications can simply plug to the API and access the data

################################################################################

#API: Application Programming Interface

#The API is the specification for what the URL patterns are,
#what is the syntax of data to send
#what is the syntax of data we can expect to get back

################################################################################
