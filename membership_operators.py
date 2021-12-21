import tabulate
tabulate.PRESERVE_WHITESPACE = True


def intro():
    print("\n")
    print(
        """Membership Operators are used to check whether a value (or a variable) is in a sequence
or collection.
    """
    )
    from tabulate import tabulate
    toc = [
        ['    in', 'Returns True if value is found in the sequence', 'x in list'],
        [' ', ' ', ' ', ' '],
        ['  not in', 'Returns True if value is not found in the sequence', 'y not in list']
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
