import tabulate
tabulate.PRESERVE_WHITESPACE = True


def intro():
    print("\n")
    print("""'Any' and 'All' are two built-in functions to identify successive And/Or in an iterable.
    """)
    from tabulate import tabulate
    toc = [
        ['   any()', """Returns True if any of the items are True,
and returns False if the iterable is empty
or if all are False.""", 'any([False, False, False])'],
        [' ', ' ', ' '],
        [' ', """Returns True because one of the items are True.  """, 'any([False, True, False])'],
        [' ', ' ', ' '],
        [' ', """Using any() on a list:

    list1 = []
    list2 = []

    for i in range(1, 11):
        list1.append(4 * i)

    for i in range(0, 10):
        list2.append(list1[i] % 5 == 0)
    print(any(list2))
""", ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        ['    all()', """Returns True if all of the items are True
(or if the iterable is empty), and returns
False if there is a single False value or
if all are False.""", 'all([True, True, True])'],
        [' ', ' ', ' '],
        [' ', """Returns False because one of the items is False.  """, 'all([False, True, True])'],
        [' ', ' ', ' '],
        [' ', """Returns False because all of the items are not True.""", 'all([False, False, False])'],
        [' ', ' ', ' '],
        [' ', """Using all() on a list:

    list1 = []
    list2 = []

    for i in range(1, 21):
        list1.append(4 * i - 3)

    for i in range(0, 20):
        list2.append(list1[i] % 2 == 1)
    print(all(list2))
""", ' '],

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
