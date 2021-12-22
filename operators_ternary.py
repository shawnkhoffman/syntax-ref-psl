def intro():
    print("\n")
    print("""Also known as conditional expressions, these are operators that evaluate something based
on a condition being True or False. Most useful when a full if/then/else statement is too
verbose for the sake of setting a single variable based on a condition.

NOTE: Ternary operators have the lowest priority amongst all Python operations.

    Syntax: [do_this] if [expression_is_true] else [do_this_on_false]

""")

    from tabulate import tabulate
    toc = [
        ["""Standard Syntax:
Returns the value of 'a' as the value of 'v'
if (a < b).
Else, returns the value of 'b' as the value of 'v'.""", 'v = a if a < b else b'],
        [' ', ' '],
        [' ', ' '],
        ["""Syntax with Tuples:
If [a < b] is true, return 1; so the element with
the index of 1 in the tuple  (in this case 'a')
will be assigned to 't'.
Else, if [a < b] is false, return 0; so the
element with the index of 0 in the tuple (in this
case 'b') will be assigned to 't'.""", 't = (b, a)[a < b]'],
        [' ', ' '],
        [' ', ' '],
        ["""Syntax with Dictionaries:
Returns the value associated with the True key in
the dictionary if [a < b] is true.
Else, returns the value associated with the False
key in the dictionary if [a < b] is false.""", 'd = {True: a, False: b}[a < b]'],
        [' ', ' '],
        [' ', ' '],
        ["""Syntax with Lambda functions:
Returns the value assigned to 'a' if [a < b] is
true.
Else, returns the value assigned to 'b' (does not
evaluate both).""", 'l = (lambda: b, lambda: a)[a < b]()']
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
