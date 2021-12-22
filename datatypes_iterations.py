import tabulate
tabulate.PRESERVE_WHITESPACE = True


def intro():
    print("\n")
    print("""Iterations or looping can be performed by 'for' and 'while' loops. Apart from
iterating upon a particular condition, we can also iterate on strings, lists,
tuples, and dictionaries.

    """)
    from tabulate import tabulate
    toc = [
        ["""i = 1
while (i < 10):
    i += 1
    print(i)""", """Sets 1 to the variable 'i', then creates a conditional
to run a loop 'while i is less than 10'. On each
iteration, 1 is added to 'i' and then 'i' is printed.
The loop terminates only when 'i' is equal to 10."""],
        [' ', ' '],
        [' ', ' '],
        ["""s = "Hello World"
for i in s:
    print(i)""", """Sets the string "Hello World" to the variable 's',
then runs a 'for' loop over it to print out each character
one-by-one. The variable 'i' (after the 'for' keyword)
will start at the first item in the list. Then, at each
subsequent iteration, the variable 'i' will be equal to
the next item in the list. The loop terminates when every
character has been printed."""],
        [' ', ' '],
        [' ', ' '],
        ["""list1 = [1, 4, 5, 7, 8, 9]  
for i in list1:
    print(i)""", """Sets a list of integers to the variable 'list1', then runs
a 'for' loop over it to print out each list item
one-by-one. The variable 'i' (after the 'for' keyword)
will start at the first item in the list. Then, at each
subsequent iteration, the variable 'i' will be equal to
the next item in the list. At each iteration, the value
assigned to 'i' will be printed."""],
        [' ', ' '],
        [' ', ' '],
        ["""for i in range(0, 10):
    print (i)""", """Runs a 'for' loop over a range of integers starting from 0
and ending at 10 and prints out each value one-by-one.
The variable 'i' (after the 'for' keyword) will start
at the first number in the range. Then, at each
subsequent iteration, the variable 'i' will be equal
to the next number. At each iteration, the value
assigned to 'i' will be printed."""]
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
