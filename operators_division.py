import tabulate
tabulate.PRESERVE_WHITESPACE = True


def intro():
    print("\n")
    print("""
    """)
    from tabulate import tabulate
    toc = [
        [
            '  //', """Floor division for int and float arguments used to
return the closest integer value which is less than or equal to a specified
expression or value. You know that 5/2 is 2.5, the closest integer which is
less than or equal is 2[5//2].""",
            '5//2'
        ]
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
