# Scientific_Computing_with_Python

## Built-in Functions
##### def (definition) -> doesn't run a code it remembers it and stores it there (store face) creates a bit of code and records it like a macro and it names whatever you choose -> we do this so we can't reuse the same lines and if there is a problem we can fix it easier
##### break -> ends the current loop and jumps the statemnet immediatly following the loop
##### continue -> ends the current iteration and jumps to the top of the loop and starts the next iteartion
##### .find() -> function to search for a substring within another string, if not found returns -1
##### .upper() -> upper case
##### .lower() -> lower case 
##### .replace() -> search and replace operation, replaces all the occurences of the search string with the replacement string
##### lstrip() and rstrip() -> remove the whitespace at the left or right
##### strip() -> removes both beginning and ending whitespace
##### .startswith() -> does this line starts with a particular thing (letter or word), returns True or False
##### open(fname) -> returns a "file handle" (a variable used to perform operations on the file)
##### quit() -> use to quit the program, never returns
##### range() -> returns a list of numbers that range from zero to less than the parameter
##### append -> add elemnts in the list
##### count -> look for certain values on a list
##### extend -> add things in the end of the list
##### index -> looks things up in a list
##### insert -> allows the list to expand in the middle
##### pop -> pulls things off the top
##### remove -> removes an item in the middle
##### reverse -> flips the order of them
##### sort -> puts them in sorted order based on the values
##### split() -> if we have a string it breaks it out, looks for blanks and gives us a list of strings; split the things based on spaces
##### .encode() -> prepare the data to go across the internet

## Some Definitions
##### parameter -> is a variable which is used in the function definition. It is a "handle" that allows the code in the function to access the argument for a particular function invocation.
##### return -> often a function will take its arguments, do some computation, and return a value to be used as the value of the function call in the calling expression. 
##### loops (repeated steps) -> have iteration variables that change each time through a loop. Often these iteration variables go through a sequance of numbers.
##### Indefinite Loops -> "while" loops because they keep going until a logical condition becomes False
##### Deinite Loops -> "for" loops because they execute an exact number of times
##### is Operator -> can be used in logical expression, implies "is the same as", similar to but stronger than "=="
##### is not -> also an operator
##### string -> is a sequence of characters, for strings, "+" means "concatenate"
##### "in" keyword -> can be used to check to see if one string is "in" another string, is a logical expression that returns True or False and can be used in an if statement -> has Built-in string functions, called "string library" 

## Opening a file
##### Before reading we have to tell Python which file we are going to work and what we'll be doing in this file
##### Done -> "open()" function
##### open() -> returns a "file handle" (a variable used to perform operations on the file)
##### Similar to "File -> Open" in a Word Processor
##### handle = open(filename, mode), mode -> read it (r) or write it (w), -> Ex. fhand = open("mbox.txt", "r") (fhand - file handle), \n -> new line
##### .read() -> used to read the file

## Lists
##### What is not a Collection -> Variables are not collections -> you can store only one value in a variable
##### What is a Collection -> like suitcases, we can put a lot of things in them. Ex. -> a list friends = ["Joseph", "Glenn", "Sally"]
##### List constants are surrounded by square brackets and the elements in the list are separated by commas
##### A list element can be any Python object - even another list
##### A list can be empty
##### Lists are mutable -> they can change
##### the range function -> returns a list of numbers that range from zero to less than the parameter, can construct an index loop using for and an integer iterator
##### We can concatenate lists using "+"
##### Lists can be sliced
##### dir -> remind the commends on a list (dir(x)) , [append, count, extend, index, insert, pop, remove, reverse, sort]
##### we can create an empty list and add elemnts using append
##### "in" -> used to see if True or False
##### lists are sortable 

### Compare Lists and Dictionaries
##### Lists -> a linear collection of values that stay in order
##### Dictionary -> a "bag" of values, each with its own label (key-value pairs)

## Dictionaries
##### Python's most powerful data collection
##### do fast database-like operations
##### Different names in different languages -> Associative Arrays (Perl/PHP); Properties or Map or HashMap (Java); Property Bag (C#/.Net)
##### Lists index their entries based on the position in the list
##### are like bags -> no order
##### index the things we pu oin the dictionary with a "lookup tag"
##### Dictionaries like lists -> except they use keys instead of numbers to look up values
##### we can overwrite values just like at lists
##### Dictionaries Literals (Constants) -> use curly braces and have a list of key : value pairs
##### Common Aplication of dictionaries -> Counters, making Histograms, counting the frequency of things
##### Error -> can get an error to refrence a key which is not in the dictionary; can use "in" to see if a key is in the dictionary 
##### get method -> counts.get(name, 0); counts - dictionary; name - key; 0 - default
##### we can loop through the key-value pairs in a dictionary using "two" iteration variables; in each iteration the first value is the key and the second one is the corresponding value for the key; ONLY PYTHON FEATURE

## Tuples 
##### -> are like lists; limited lists
##### -> are another kind of sequence that functions much like a list; they have elements which are indexed starting at 0
##### -> they don't use square brackets; but you to look at the positions you have to use square brackets
##### -> are immutable, unlike a list, once you create a tuple, you cannot alter its contents - similar to a string
##### Build-in -> count() & index(); these are the only ones from list that work at tuples
##### -> we like them because they are more efficent in memory use and performance than lists
##### -> can put tuple on the left-hand side of an assignment statement; Ex. (x, y) = (4, 'fred') -> x = 4 & y = fred
##### -> the items() method in dictionaries returns a list of (key, value) tuples
##### -> tuples can be compared; if the first item is equal, Python goes on to the next element, and so on, until it finds elements that differ

## Regular Expressions
##### regex/regexp -> provide a concise and flexible means for matching string of text
##### -> a regular expression is a written in a formal language that can be interpreted by a regular expresion processor (find or search)
##### -> very powerful and quite cryptic; like a language unto themselves; programming with characters; "old school" language - compact
##### -> it is character based not line based or keyword based
##### -> is not part of python; have to import it; "import re"
##### re.search() -> see if a string matches a regular expression, similar to find() method for strings
##### re.findall() -> extract portions of a string that match your regular expression

## Regular Expression Quick Guide
##### ^        Matches the beginning of a line
##### $        Matches the end of the line
##### .        Matches any character
##### \s       Matches whitespace
##### \S       Matches any non-whitespace character
##### *        Repeats a character zero or more times
##### *?       Repeats a character zero or more times (non-greedy)
##### +        Repeats a character one or more times
##### +?       Repeats a character one or more times (non-greedy)
##### [aeiou]  Matches a single character in the listed set
##### [^XYZ]   Matches a single character not in the listed set
##### [a-z0-9] The set of characters can include a range
##### (        Indicates where string extraction is to start
##### )        Indicates where string extraction is to end

## Network Programming
### TCP Connections/Sockets
##### Internet Socket -> is an endpoint of a bidirectonal inter-process communication flow across an Internet Protocol-based computer network, such as the Internet
### TCP Port Numbers
##### -> application-specific or process-specific software communications endpoint
##### -> multiple applications can coexist on the same server
##### Python has built-in support for TCP Sockets
##### UTF-16 -> Fixed length -> Two bytes
##### UTF-32 -> Fixed Length -> Four bytes
##### UTF-8 -> 1-4 bytes
###### Compatible with ASCII
###### automatic detection between ASCII and UTF-8
###### UTF-8 -> recommended practice for encoding data to be exchanged between systems
##### Python 3 -> all strigs internally are UNICODE

## HTTP
##### HyperText Transfer Protocol -> is the set of rules to allow browsers to retrieve web documents from servers over the internet
##### Protocol -> a set of rules that all parties follow so we can predict each other's behaviour; and not bump into each other
##### Since HTTP is so common -> have a library that does all the socket work for us and makes web pages look like a file

## Web Scraping
##### -> the act of retreiving a web page or extracting the links from those webpage, making a q of unretrieve links 
### Why Scrape?
##### -> pull data from a social data
##### -> get your own data back out of some system that has no "export capability"
##### -> monitor a site for new info
##### -> spider the web to make database for a search engine
##### Socket -> its goal is to have one application process sending data to another application process

## Web Services
##### Decide a protocol that is independent of any programming language => the "Wire Protocol"
##### Two ways to mark up data: XML & JSON
### XML (eXtensible Markup Language) => Marking up data to send across the network
##### Primary purpose -> help information system share structured data
##### Think XML as a Tree, as Paths
#### Terminology
##### Tags -> indicate the beginning and the ending of elemnts
##### Attributes -> Keyword/value pairs on the opening tag of XML
##### Serialize/De-Serialize -> Convert data in one program into common format that can be stored and/or transmitted between systems in a programming language-independent manner
### XML Schema -> description of the legal format of an XML document
##### -> a language that allows if a particular document meets a contract
##### XSD XML Schema -> World Wide Web Consortium (W3C), files end with .xsd
### JSON (JavaScript Object Notation) => Object literal notation in JavaScript
##### XML better for rich and hirerchial documents; JSON best for pulling data out of a system and moving between two systems (simplier)
### SOA (Service Oriented Approach) => non-trivial web applications use services
##### Credit Card Charge
##### Hotel Reservation systems
### API (Application Program Interface) -> specifies an inteface and controls the behavior of the objects specified in that inteface
##### The software that provides functionality is an "implementation" of the API
#### URL encoded
##### "+" -> means space
##### "%2C" -> comma
##### We use a library in python that takes care of this

## Object Oriented Programming
##### -> a program is made up of many cooperating objects
##### -> instead of being a whole program - each object is a little island within the program and cooperatively working with other objects
##### -> a program is made up of one or more objects working together
##### -> a self contained Code and Data
##### -> break the problem into smaller understandable parts

## Definitions
##### Class -> a template -Dog
##### Method/Message -> a defined capability of a class - bark()
##### Field/attribute -> a bit of a data in a class - length
##### Object/Instance -> a particular instance of a class - Lassie
##### Instance -> the actual object created at a runtime. We can have a kit of instances created from one class(We can have a lot of dogs with different name that come from the dog class)
##### Method -> a bit of code that lives inside of an object
##### Special blocks of code (methods) get called automatically from Python in our behalf -> constructor and destructor
##### Constructor used to set up any initial values or variable if neccessary 
#### Inheritance -> we can create a new class and reuse and inherit all the capabilities of an existing class and add whatever we want to (extend/subclass)


## Common TCP Ports
##### Telnet(23) -> Login
##### SSH(22) -> Secure Login
##### HTTP(80)
##### HTTPS(443) -> Secure
##### SMTP(25) -> Mail
##### IMAP(143/220/993) -> Mail Retrieval
##### POP](109/110) -> Mail Retrieval
##### DNS(53) -> Domain Name
##### FTP(21) -> File Transfer

## urllib
##### substitutes the socktes (does the work of sockets but you don't need to write all the code)