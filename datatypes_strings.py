import tabulate
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



Indexing allows negative address references to access
substrings starting the back of the String (e.g. -1
refers to the last character, -2 refers to the second
last character, and so on).

        string1 = "Hello, World!"

        print("Last character of String is: ")
        print(string1[-1])


While accessing an index out of the range will cause an
IndexError. Only Integers are allowed to be passed as an
index, float or other types that will cause a TypeError.


---(END)---
    """)


def string_slicing():
    print("""
String Slicing

To access a range of characters in the String, the method of
slicing is used. Slicing in a String is done by using a Slicing
operator (colon) in addition to the square brackets.


    string2 = "Hello, World!"

    print("Slicing characters from 0-6: ")
    print(string2[0:6])

    print("Slicing characters from 7-13: ")
    print(string2[7:13])


---(END)---

""")


def deleting_updating_string():
    print("""
Deleting/Updating from a String

    """)
