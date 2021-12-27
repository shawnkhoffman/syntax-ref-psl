import tabulate
import pydoc
tabulate.PRESERVE_WHITESPACE = True


def intro():
    print("\n")
    print("""A string is a sequence of unicode characters. It can be declared
by using single-quotes, double-quotes, or triple-quotes.
Strings are immutable: they cannot be changed.

    """)
    from tabulate import tabulate
    toc = [
        ["""a = 'Hello, World!'""", """Uses single-quotes to assign the string
'Hello, World!' to the variable 'a'."""],
        [' ', ' ', ' ', ' '],
        ["""print("Hello, World!") """, """Uses double-quotes to return the
string "Hello, World!" to the output."""],
        [' ', ' ', ' ', ' '],
        ["""print(
    \"""This is a
multi-line string.\"""
    )""", """Returns a multi-line string to
the output. Also works with triple
single-quotes."""],
        [' ', ' '],
        [' ', ' '],
        [' ', ' ']
    ]

    print(
        tabulate(
            toc,
            headers=[
                'Syntax', 'Description'
                ],
            tablefmt='simple'
            )
        )


def accessing_chars():
    print("""
Accessing characters in Python

Python does not have a character data type. A single
character is simply a "substring" with a length of 1.

Substrings can be accessed by using the method of
Indexing. To use indexing, use square brackets: []
with the number place associated with the character.


        string1 = "Hello, World!"

        print("First character of String is: ")
        print(string1[0])

            Output:
            First character of String is:
            H



Indexing allows negative address references to access
substrings starting the back of the String (e.g. -1
refers to the last character, -2 refers to the second
last character, and so on).

        string1 = "Hello, World!"

        print("Last character of String is: ")
        print(string1[-1])

            Output:
            Last character of String is:
            !


While accessing an index out of the range will cause an
IndexError. Only Integers are allowed to be passed as an
index, float or other types that will cause a TypeError.

""")


def string_slicing():
    pydoc.pager("""
String Slicing

To access a range of characters in the String, the method of
slicing is used. Slicing in a String is done by using a Slicing
operator (colon) in addition to the square brackets.


    string2 = "Hello, World!"

    print("Slicing characters from 0-6: ")
    print(string2[0:6])

    print("Slicing characters from 7-13: ")
    print(string2[7:13])

        Output:
        Slicing characters from 0-6:
        Hello,
        Slicing characters from 7-13:
        World!

""")


def deleting_updating_string():
    pydoc.pager("""
Deleting/Updating from a String

Deleting or updating characters in a String is not supported
because Strings are immutable. Only new strings can be reassigned
to the same variable, or the same string may be assigned to a
different variable.


    string1 = "Hallow, Wurld?"
    print("Initial String: ")
    print(string1)

        Output:
        Initial String:
        Hallo, Wurld?

        string1 = "Hello, World!"
        print("Updated String: ")
        print(string1)

        Output:
        Updated String:
        Hello, World!

""")


def escape_characters():
    pydoc.pager("""
Escape Characters

Printing Strings with single and double quotes in it can
cause a SyntaxError when the String already contains
Single or double quotes and, hence, cannot be printed with
the use of either of these. To print such a String, either
triple quotes are used, or 'escape characters' are used.

Escape characters start with a backslash and can be
interpreted differently. If single quotes are used to
represent a string, then all the single quotes present in
the string must be 'escaped'. The same is true for when
double quotes are used instead.


    string1 = 'I\\'m \\'escaping\\' single quotes.'
    print("Escaping single quotes:")
    print(string1)

        Output:
        Escaping single quotes:
        I'm 'escaping' single quotes.


    string2 = "I'm \\"escaping\\" double quotes."
    print("Escaping double quotes:")
    print(string2)

        Output:
        Escaping double quotes:
        I'm "escaping" double quotes.


    string3 = "C:\\\Escaping\\\Back\\\Slashes"
    print("Escaping backslashes:")
    print(string3)

        Output:
        Escaping backslashes:
        C:\Escaping\Back\Slashes


    string4 = "\\x48\\x65\\x6c\\x6c\\x6f\\x2c\\x20\\x57\\x6f\\x72\\x6c\\x64\\x21"
    print("Printing in HEX with the use of escape characters:")
    print(string4)
    
        Output:
        Printing in HEX with the use of escape characters:
        \x48\x65\x6c\x6c\x6f\x2c\x20\x57\x6f\x72\x6c\x64\x21


    string5 = r"\\x48 \\x65 \\x6c \\x6c \\x6f \\x2c \\x20 \\x57 \\x6f \\x72 \\x6c \\x64 \\x21"
    print("Printing the same HEX value in raw string format:")
    print(string5)

        Output:
        Printing the same HEX value in raw string format:
        \\x48 \\x65 \\x6c \\x6c \\x6f \\x2c \\x20 \\x57 \\x6f \\x72 \\x6c \\x64 \\x21

""")


def string_formatting_method():
    pydoc.pager("""
String Formatting using the format() method

Strings in Python can be formatted with the use of format()
method. The format method contains curly braces {} as
placeholders which can hold arguments according to position
or keyword to specify the order.

    string1 = "{}, {}!".format('Hello', 'World')
    print("Print String in default order:")
    print(string1)

        Output:
        Print String in default order:
        Hello, World!


    string2 = "{1}, {0}!".format('World!', 'Hello')
    print("Print String in Positional order:")
    print(string2)

        Output:
        Print String in Positional order:
        Hello, World!


    string3 = "{h}, {w}!".format(w='World', h='Hello')
    print("Print String in order of Keywords:")
    print(string3)

        Output:
        Print String in order of Keywords:
        Hello, World!



Integers such as binary, hexadecimal, exponents, and
floats can be rounded or displayed in their
representative form with the use of 'format' specifiers.

    string1 = "{0:b}".format(16)
    print("Binary representation of 16 is:")
    print(string1)

        Output:
        Binary representation of 16 is:
        10000


    string2 = "{0:e}".format(165.6458)
    print("Exponent representation of 165.6458 is:")
    print(string2)

        Output:
        Exponent representation of 165.6458 is:
        1.656458e+02


    string3 = "{0:.2f}".format(1/6)
    print("One-sixth in float decimal format:")
    print(string3)

        Output:
        One-sixth in decimal format:
        0.17


    string4 = "|{:<10}|{:^10}|{:>10}|".format('Hello', 'Big', 'World!')
    print("Left, center and right alignment with Formatting:")
    print(string4)

        Output:
        Left, center and right alignment with Formatting: 
        |Hello     |   Big    |    World!|


    string5 = "{0:^16} was written in {1:<4}!".format("This program", 2021)
    print(string5)

        Output:
        This program   was written in 2021!

""")

def string_formatting_mod():
    print("""
String Formatting using the % (modulus) operator.

""")
    from tabulate import tabulate
    toc = [
        ["""   %d""", """    Integers"""],
        [' ', ' '],
        ["""   %f""", """    Floats"""],
        [' ', ' '],
        ["""   %s""", """    Strings"""],
        [' ', ' '],
        ["""   %x""", """    Hexadecimals"""],
        [' ', ' '],
        ["""   %o""", """    Octal"""],
        [' ', ' '],
        ["""   %r""", """    Raw data"""],
        [' ', ' '],
        ["""   %c""", """    ASCII"""],
        [' ', ' ']
    ]

    print(
        tabulate(
            toc,
            headers=[
                'Syntax', 'Description'
                ],
            tablefmt='simple'
            )
        )

    print("""

String Formatting with Strings

    string1 = '15'
    print("string1 as a string = %s" % (string1))

        Output:
        string1 as a string = 15



String Formatting with Raw Data

    string1 = '15'
    print("string1 as raw data = %r" % (string1))

        Output:
        string1 as raw data = '15'



String Formatting with Integers

    string1 = '15'
    integer1 = int(string1)
    print("integer1 as an integer = %d" % (integer1))

        Output:
        integer1 as an integer = 15



String Formatting with Floats
    integer1 = 15
    float1 = float(integer1)
    print("float1 as a float = %f" % (float1))

        Output:
        float1 as a float = 15.000000


    float1 = 12.3456789
    print("Formatting in 3.2f format:")
    print('The value of integer1 is %3.2f' % float1)

        Output:
        Formatting in 3.2f format: 
        The value of integer1 is 12.35


    integer1 = 12.3456789
    print("Formatting in 3.4f format:")
    print('The value of integer1 is %3.4f' % integer1)

        Output:
        Formatting in 3.4f format: 
        The value of integer1 is 12.3457



String Formatting with Hexadecimal

    integer1 = 100
    print("integer1 as Hexidecimal = %x" % (integer1))

        Output:
        integer1 as Hexidecimal = 64



String Formatting with Octal

    integer1 = 100
    print("integer1 as Octal = %o" % (integer1))

        Output:
        integer1 as Octal = 144



String Formatting with ASCII

    codes = [72, 101, 108, 108, 111,
             44, 32, 87, 111, 114,
             108, 100, 33]

    secret_message = ''

    for i in codes:
        secret_message += ("%c" % (i))

    print(secret_message)

        Output:
        Hello, World!
""")


def logical_operations():
    pydoc.pager("""
Logical Operations on Strings

Boolean operators (and, or, not) work on Python strings.
Python considers empty strings as having a boolean value of False
and non-empty strings as having a boolean value of True.

For the 'and' operator, if the left value is True, then the right
value is checked and returned. If the left value is False, then
that value is returned.

For the 'or' operator, if the left value is True, then it is returned.
Otherwise, if the left value is False, then the right value is returned.

NOTE: Bitwise operators (|, &) don't work for strings.


Using the built-in repr() function while checking for boolean
values between two strings.


    string1 = ''
    string2 = 'World!'
    print(repr(string1 and string2))

        Output:
        'World!'


    string1 = ''
    string2 = 'World!'
    print(repr(string2 and string1))

        Output:
        ''

    string1 = ''
    string2 = 'World!'
    print(repr(string1 or string2))

        Output:
        'World!'


    string1 = 'Hello, '
    string2 = 'World!'
    print(repr(string1 and string2))

        Output:
        'World!'

    
    string1 = 'Hello, '
    string2 = 'World!'
    print(repr(string2 and string1))

        Output:
        'Hello, '


    string1 = 'Hello, '
    print(repr(not string1))

        Output:
        False


    string1 = ''
    print(repr(not str1))

        Output:
        True
""")


def template_class():
    print("""

Templatizing Strings

The Template Class allows you to easily create a re-usable string
template. To use this class, you have to import the module
from the string library. Then you create an object from the class.
Once you create the object, you can access the substitute() and
safe_substitute() methods.

Aside from creating templates for strings, another application for
creating a template is separating program logic from the details
of multiple output formats. This makes it possible to substitute
custom templates for XML files, plain text reports, and HTML web
reports.

"""
    )

    from tabulate import tabulate
    toc = [
        ["""substitute(mapping, **kwds)""", """Handles templatizing strings by performing substitutions
using a mapping of keys. Keyword arguments can also be
used for the same purpose. In case the key-based
mapping and the keyword arguments have the same key,
it throws a TypeError. If keys are missing, it returns
a KeyError."""],
        [' ', ' '],
        ["""safe_substitute(mapping, **kwds)""", """Behavior of this method is similar to that of the
substitute method but it doesn't throw a KeyError if a
key is missing, rather it returns a placeholder in the
result string."""],
        [' ', ' ']
    ]

    print(
        tabulate(
            toc,
            headers=[
                'Method', 'Description'
                ],
            tablefmt='simple'
            )
        )

    print("""

Using the substitute() method

    from string import Template

    t = Template('Welcome, $name. Today is $day.')
    welcome_message = t.substitute(name='Sam', day='Monday')

    print(welcome_message)

        Output:
        Welcome, Sam. Today is Monday.


Using the safe_substitute() method

    from string import Template

    t = Template('Welcome, $name. Today is $day.')
    welcome_message = t.safe_substitute(name='Sam')

    print(welcome_message)

        Output:
        Welcome, Sam. Today is $day.



Using a Dictionary with a String Template

    from string import Template

    t = Template('Welcome, $name. Today is $day.')
    d = {'name': 'Sam', 'day': 'Monday'}

    welcome_message = t.substitute(d)

    print(welcome_message)

        Output:
        Welcome, Sam. Today is Monday.



Using a List with a String Template

    from string import Template

    user_template = Template('$user_name')
    basket_template = Template('$number $item')

    shopping_basket = [
        (1, 'Eldest Scrolls Unlimited Edition'),
        (1, 'Street Warriors Online'),
        (1, 'GamerStation Gaming Console')
        ]

    user_name = user_template.substitute(user_name='Isaac DeSnuts')

    print("Hi", "{},".format(user_name), "you have the following items in your basket:")

    for i in shopping_basket:
        print("•", basket_template.substitute(number = i[0], item = i[1]))

        Output:
        Isaac De'Snuts, you have the following items in your basket:
        • 1 Eldest Scrolls Unlimited Edition
        • 1 Street Warriors Online
        • 1 GamerStation Gaming Console



You can use braces to allow strings to be prepended or appended
to a given key.

    from string import Template

    t = Template('Welcome, ${user_name}#001. Today is ${day}.')
    welcome_message = t.substitute(user_name='python_fan', day='Monday')

    print(welcome_message)

        Output:
        Welcome, python_fan#001. Today is Monday.


    from string import Template

    t = Template('${user_name}@yourdomain.com')
    email = t.substitute(user_name='monty.python')

    print(email)

        Output:
        monty.python@yourdomain.com



You don't have to prefix with $... you can use any character you want
to prefix. Here's how to do it with ! instead...

    class MyTemplate(Template):
        delimiter = '!'


You can use $$ to escape the $ sign and treat it as part of the string.

    template = Template('$$ is the symbol for $name')
    string = template.substitute(name='Dollar')
    print(string)

        Output:
        $ is the symbol for Dollar




You can also change the "identifier".


You can also print a template string.

    t = Template('I am $name from $city)
    print('Template String =', t.template)

        Output:
        Template String = I am $name from $city
""")

def splitting_strings():
    pydoc.pager("""

The split() method returns a list of strings after breaking the given
string by the specified separator.

    line = "user1 user2 user3"
    print(line.split())
    print(line.split(' ', 1))

        Output:
        ['user1', 'user2', 'user3']
        ['user1', 'user2 user3']


    line2 = " user4, user5, user6"
    print(line2.split(','))

        Output:
        [' user4', ' user5', ' user6']
""")


def doc_strings():
    pydoc.pager("""
Documentation strings (or docstrings) provide a convenient way of
associating documentation with Python modules, functions, classes,
and methods. Unlike conventional source code comments, a docstring
should describe what the function does, not how.

What a good docstring looks like:
• The docstring line should begin with a capital letter and end
  with a period.
• The first line should be a short description.
• If there are more lines in the documentation string, the second
  line should be blank, visually separating the summary from the
  rest of the description.
• The following lines should be one or more paragraphs describing
  the object's calling conventions, its side effects, etc.


Declaring a Docstring

Docstrings are declared using '''triple single quotes''' or
\"""triple double quotes""\" just below the class, method or
function declaration. All functions should have a docstring.

    def my_function():
        \"""Demonstrates triple double quotes
        docstrings and does nothing really.\"""
   
        return None


Accessing Docstrings

The docstrings can be accessed using the __doc__ method of the
object or using the help function.

    def my_function():
        '''Demonstrates triple single quotes
        docstrings and does nothing really.'''

        return None

    print("Using __doc__:")
    print(my_function.__doc__)
    
    print("Using help:")
    help(my_function)

        Output:
        Using __doc__:
        Demonstrates triple single quotes
            docstrings and does nothing really.
        Using help:
        Help on function my_function in module __main__:

        my_function()
            Demonstrates triple single quotes
            docstrings and does nothing really.


    def my_function():
        \"""Demonstrates triple double quotes
        docstrings and does nothing really.\"""

        return None

    print("Using __doc__:")
    print(my_function.__doc__)
    
    print("Using help:")
    help(my_function)

        Output:
        Using __doc__:
        Demonstrates triple double quotes
            docstrings and does nothing really.
        Using help:
        Help on function my_function in module __main__:

        my_function()
            Demonstrates triple single quotes
            docstrings and does nothing really.



One-line docstrings are used in cases where there is no need
for more-detailed documentation on a class, method or
function.

    def power(a, b):
    \"""Returns arg1 raised to power arg2.\"""
   
        return a**b
    
    print(power.__doc__)

        Output:
        Returns arg1 raised to power arg2.


Multi-line docstrings consist of a summary line just like a
one-line docstring, followed by a blank line, followed by a
more elaborate description. The summary line may be on the
same line as the opening quotes or on the next line.

    def my_function(arg1):
        \"""
        Summary line.
    
        Extended description of function.
    
        Parameters:
        arg1 (int): Description of arg1
    
        Returns:
        int: Description of return value
    
        \"""
    
        return arg1
    
    print(my_function.__doc__)

        Output:
        Summary line.
        Extended description of function.
        Parameters:
        arg1 (int): Description of arg1

        Returns:
        int: Description of return value


Indentation in Docstrings

The entire docstring is indented the same as the quotes at
its first line. Docstring processing tools will strip a
uniform amount of indentation from the second and further
lines of the docstring, equal to the minimum indentation of
all non-blank lines after the first line. Any indentation
in the first line of the docstring (i.e., up to the first
newline) is insignificant and removed. Relative indentation
of later lines in the docstring is retained.


Docstrings in Classes

    class ComplexNumber:
        \"""
        This is a class for mathematical operations on complex numbers.
        
        Attributes:
            real (int): The real part of complex number.
            imag (int): The imaginary part of complex number.
        \"""
    
        def __init__(self, real, imag):
            \"""
            The constructor for ComplexNumber class.
    
            Parameters:
            real (int): The real part of complex number.
            imag (int): The imaginary part of complex number.   
            \"""
    
        def add(self, num):
            \"""
            The function to add two Complex Numbers.
    
            Parameters:
                num (ComplexNumber): The complex number to be added.
            
            Returns:
                ComplexNumber: A complex number which contains the sum.
            \"""
    
            re = self.real + num.real
            im = self.imag + num.imag
    
            return ComplexNumber(re, im)
    
    help(ComplexNumber)  # to access Class docstring
    help(ComplexNumber.add)  # to access method's docstring


        Output:
        Help on class ComplexNumber in module __main__:

        class ComplexNumber
        |  This is a class for mathematical operations on complex numbers.
        |  
        |  Attributes:
        |          real (int): The real part of complex number.
        |          imag (int): The imaginary part of complex number.
        |  
        |  Methods defined here:
        |  
        |  __init__(self, real, imag)
        |      The constructor for ComplexNumber class.
        |      
        |      Parameters:
        |      real (int): The real part of complex number.
        |      imag (int): The imaginary part of complex number.
        |  
        |  add(self, num)
        |      The function to add two Complex Numbers.
        |      
        |      Parameters:
        |              num (ComplexNumber): The complex number to be added.
        |      
        |      Returns:
        |              ComplexNumber: A complex number which contains the sum.

        Help on method add in module __main__:

        add(self, num) unbound __main__.ComplexNumber method
            The function to add two Complex Numbers.
            
            Parameters:
                    num (ComplexNumber): The complex number to be added.
            
            Returns:
                    ComplexNumber: A complex number which contains the sum.


""")