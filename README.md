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