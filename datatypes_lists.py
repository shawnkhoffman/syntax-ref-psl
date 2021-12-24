import tabulate
tabulate.PRESERVE_WHITESPACE = True


def intro():
    print("\n")
    print("""Lists are just like arrays declared in other programming languages;
however, they do not always need to be homogeneous. A single list can contain
strings, integers, as well as objects. They also can be used for implementing
stacks and queues. They are mutable: they can be altered once declared.

    """)
    from tabulate import tabulate
    toc = [
        ["""list1 = ["string1", "string2", "string3"]  """,
            """Assigns a list of strings to the variable 'a'."""],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        ["""list2 = [
    "a_string",
    ("a", "tuple"),
    {"a": "dict"},
    ["another", "list"],
    0, 1, 2, 3
]""",
            """Assigns a list of different data types to the
variable 'b'."""]
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
