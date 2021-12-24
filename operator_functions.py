import tabulate
tabulate.PRESERVE_WHITESPACE = True


def intro():
    print("\n")
    print("""Operator Functions are a part of the "operator" module in the
Python Standard Library that contains predefined functions for many
mathematical, logical, relational, bitwise, etc.

NOTE: You must first import the operator module to access Operator Functions.

""")
    from tabulate import tabulate

    toc = [
        [' add(a, b)', """Returns the sum of a + b."""],
        [' ', ' ', ' '],
        [' sub(a, b)', """Returns the difference of a - b."""],
        [' ', ' ', ' '],
        [' mul(a, b)', """Returns the product of a * b."""],
        [' ', ' ', ' '],
        [' truediv(a, b)', """Returns the quotient from a / b."""],
        [' ', ' ', ' '],
        [' pow(a, b)', """Returns the exponentiation of a ** b."""],
        [' ', ' ', ' '],
        [' mod(a, b)', """Invokes modulus division and returns the
remainder of a / b."""],
        [' ', ' ', ' '],
        [' lt(a, b)', """Returns True if a < b; else returns False."""],
        [' ', ' ', ' '],
        [' le(a, b)', """Returns True if a <= b; else returns False."""],
        [' ', ' ', ' '],
        [' eq(a, b)', """Returns True if a == b; else returns False."""],
        [' ', ' ', ' '],
        [' gt(a, b)', """Returns True if a > b; else return False."""],
        [' ', ' ', ' '],
        [' ge(a, b)', """Returns True if a >= b; else return False."""],
        [' ', ' ', ' '],
        [' ne(a, b)', """Returns True if a != b; else return False."""],
        [' ', ' ', ' '],
        [' setitem(obj, pos, val)',
            """Assigns the value ('val') to a specific position
('pos') in a list or dict object ('obj')."""],
        [' ', ' ', ' '],
        [' setitem(obj, slice(a, b), vals)  ',
            """Assigns a set of values ('vals') at a given slice
in a list object ('obj')."""],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' delitem(obj, pos)',
            """Deletes the value ('val') at a particular position
('pos') in a list or dict object ('obj')."""],
        [' ', ' ', ' '],
        [' delitem(obj, slice(a, b))',
            """Deletes a set of values ('vals') at a given slice
in a list object ('obj')."""],
        [' ', ' ', ' '],
        [' getitem(obj, pos)',
            """Gets the value at a particular position ('pos') in
a list or dict object ('obj')."""],
        [' ', ' ', ' '],
        [' getitem(obj, slice(a, b))',
            """Gets the value at a given slice in a list object
('obj')."""],
        [' ', ' ', ' '],
        [' concat(obj1, obj2)',
            """Concatenates two collection objects ('obj1' + 'obj2'),
such as strings, lists, list items, tuples, tuple items,
and dictionary items. Can do slice operations using
concat(obj1[a:b], obj2[a:b]).
"""],
        [' ', ' ', ' '],
        [' contains(obj1, obj2)', """Check if 'obj2' is present in 'obj1'."""],
        [' ', ' ', ' '],
        [' and_(a, b)', """Computes Bitwise AND of 'a' and 'b'."""],
        [' ', ' ', ' '],
        [' or_(a, b)', """Computes Bitwise OR between 'a' and 'b'."""],
        [' ', ' ', ' '],
        [' xor(a, b)', """Computes Bitwise xOR between 'a' and 'b'."""],
        [' ', ' ', ' '],
        [' invert(a)', """Computes Bitwise Inversion of 'a'"""],
        [' ', ' ', ' '],
        [' ', ' ', ' '],

    ]

    print(
        tabulate(
            toc,
            headers=[
                'Operator', 'Description'
                ],
            tablefmt='simple'
            )
        )
