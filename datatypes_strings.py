import tabulate
tabulate.PRESERVE_WHITESPACE = True


def intro():
    print("\n")
    print("""A string is a sequence of characters. It can be declared by using
single-quotes or double-quotes. Strings are immutable: they cannot be changed.
    """)
    from tabulate import tabulate
    toc = [
        ['print("Hello, World!") ', """Returns the string 'Hello, World!' to the output."""],
        [' ', ' ', ' ', ' '],
        ['a = "Hello, World!"', """Assigns the string 'Hello, World!' to the variable 'a'."""],
        [' ', ' ', ' ', ' '],
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
