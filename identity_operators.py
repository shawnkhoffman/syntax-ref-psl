import tabulate
tabulate.PRESERVE_WHITESPACE = True


def intro():
    print("\n")
    print("""Identity Operators are used to check if two values are located in the same memory
space. Two variables that are equal do not imply that they are identical.    
    """)
    from tabulate import tabulate
    toc = [
        ['    is', 'Returns True if the operands are identical.', 'a is c'],
        [' ', ' ', ' ', ' '],
        ['  is not', 'Returns True if the operands are not identical.', 'a is not c']
    ]

    print(
        tabulate(
            toc,
            headers=[
                'Operator', 'Description', 'Syntax', 'Alt Syntax'
                ],
            tablefmt='simple'
            )
        )
