import tabulate
tabulate.PRESERVE_WHITESPACE = True


def intro():
    print("\n")
    print("""A tuple is an immutable sequence of Python objects. They are just
like lists with the exception that tuples cannot be changed once declared.
Also, tuples are usually faster than lists.

    """)
    from tabulate import tabulate
    toc = [
        ["""tup1 = (1, "a", "string", 1 + 2)  """,
            """Assigns a tuple of various data types to the
variable 'tup1'."""],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        ["""tup2 = (
    ['a', 'nested, 'list'],
    {'a': 'nested_dictionary'},
    'string1', 'string2',
    0, 1, 2
)""",
            """Assigns a tuple of various data types to the
variable 'tup2'."""]
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
