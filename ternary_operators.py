def intro():
    print("\n")
    print("""Also known as conditional expressions, these are operators that evaluate something based
on a condition being true or false. Most useful when a full if/then/else statement is too
verbose for the sake of setting a single variable based on a condition.

NOTE: Ternary operators have the lowest priority amongst all Python operations.

    Syntax: [on_true] if [expression] else [on_false]

""")

    from tabulate import tabulate
    toc = [
        ['Standard Syntax: \nReturns the value of \'a\' as the value of \'v\' if \n(a < b). Else, returns the value of \'b\' as the \nvalue of \'v\'.', 'v = a if a < b else b'],
        [' ', ' '],
        [' ', ' '],
        ['Syntax with Tuples: \nIf [a < b] is true, return 1; so the element with \nthe index of 1 in the tuple (in this case \'a\') \nwill be assigned to \'t\'. \nElse, if [a < b] is false, return 0; so the element \nwith the index of 0 in the tuple (in this case \'b\') \nwill be assigned to \'t\'.  ', 't = (b, a)[a < b]'],
        [' ', ' '],
        [' ', ' '],
        ['Syntax with Dictionaries: \nReturns the value associated with the True \nkey in the dictionary if [a < b] is true. \nElse, returns the value associated with the False \nkey in the dictionary if [a < b] is false.', 'd = {True: a, False: b}[a < b]'],
        [' ', ' '],
        [' ', ' '],
        ['Syntax with Lambda functions: \nReturns the value assigned to \'a\' if [a < b] is true.  \nElse, returns the value assigned to \'b\' \n(does not evaluate both).', 'l = (lambda: b, lambda: a)[a < b]()']
    ]

    print(
        tabulate(
            toc,
            headers=[
                'Description', 'Syntax'
                ],
            tablefmt='simple'
            )
        )
