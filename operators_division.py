import tabulate
tabulate.PRESERVE_WHITESPACE = True


def intro():
    print("\n")
    print("""
    """)
    from tabulate import tabulate
    toc = [
        ['   /', """The operator used for true division.""", '5/2 = 2.5'],
        [' ', ' ', ' '],
        [
            '  //', """Floor division for int and float arguments used to
return the closest integer value that is less than
or equal to a specified expression or value. You know
that 5/2 is 2.5, so the closest integer that is less
than or equal to that is 2.""",
            '5//2 = 2'
        ]
    ]

    print(
        tabulate(
            toc,
            headers=[
                'Operator', 'Description', 'Syntax'
                ],
            tablefmt='simple'
            )
        )
