import tabulate
tabulate.PRESERVE_WHITESPACE = True


def intro():
    print("\n")
    print("""Operator Overloading gives operators extended meaning beyond their
predefined operational meaning.

To do operator overloading, you define a 'magic/dunder' method for a class
using a pre-defined operator. You can overload all existing operators but you
cannot create a new operator.

A magic/dunder method is one that is automatically invoked when it is
associated with a particular operator. For example, when you use the '+'
operator, the magic method '__add__' is automatically invoked because it is
what is defined to the operation for '+'. To change that behavior, you define
a new magic/dunder method for it in the class that is associated with that
operation.

""")

    from tabulate import tabulate
    toc = [
        ['       +', '__add__(self, other)'],
        ['       -', '__sub__(self, other)'],
        ['       *', '__mul__(self, other)'],
        ['       /', '__truediv__(self, other)'],
        ['      //', '__floordiv__(self, other)'],
        ['       %', '__mod__(self, other)'],
        ['      **', '__pow__(self, other)'],
        ['               ', ' '],
        ['               ', ' ']
    ]

    toc2 = [
        ['      >>', '__rshift__(self, other)'],
        ['      <<', '__lshift__(self, other)'],
        ['       &', '__and__(self, other)'],
        ['       |', '__or__(self, other)'],
        ['       ^', '__xor__(self, other)'],
        ['               ', ' '],
        ['               ', ' ']
    ]

    toc3 = [
        ['       <', '__LT__(SELF, OTHER)'],
        ['       >', '__GT__(SELF, OTHER)'],
        ['      <=', '__LE__(SELF, OTHER)'],
        ['      >=', '__GE__(SELF, OTHER)'],
        ['      ==', '__EQ__(SELF, OTHER)'],
        ['      !=', '__NE__(SELF, OTHER)'],
        ['               ', ' '],
        ['               ', ' ']
    ]

    toc4 = [
        ['      -=', '__ISUB__(SELF, OTHER)'],
        ['      +=', '__IADD__(SELF, OTHER)'],
        ['      *=', '__IMUL__(SELF, OTHER)'],
        ['      /=', '__IDIV__(SELF, OTHER)'],
        ['     //=', '__IFLOORDIV__(SELF, OTHER)'],
        ['      %=', '__IMOD__(SELF, OTHER)'],
        ['     **=', '__IPOW__(SELF, OTHER)'],
        ['               ', ' '],
        ['               ', ' ']
    ]

    toc5 = [
        ['     >>=', '__IRSHIFT__(SELF, OTHER)'],
        ['     <<=', '__ILSHIFT__(SELF, OTHER)'],
        ['      &=', '__IAND__(SELF, OTHER)'],
        ['      |=', '__IOR__(SELF, OTHER)'],
        ['      ^=', '__IXOR__(SELF, OTHER)'],
        ['               ', ''],
        ['               ', ' ']
    ]

    toc6 = [
        ['       -', '__NEG__(SELF, OTHER)'],
        ['       +', '__POS__(SELF, OTHER)'],
        ['       ~', '__INVERT__(SELF, OTHER)'],
        ['               ', ''],
        ['               ', ' ']
    ]

    print(
        tabulate(
            toc,
            headers=[
                ' Binary', ' Magic Method'
                ],
            tablefmt='simple'
            ),
        tabulate(
            toc2,
            headers=[
                'Bitwise', 'Magic Method'
                ],
            tablefmt='simple'
            ),
        tabulate(
            toc3,
            headers=[
                'Comparison', 'Magic Method'
                ],
            tablefmt='simple'
            ),
        tabulate(
            toc4,
            headers=[
                'Assignment', 'Magic Method'
                ],
            tablefmt='simple'
            ),
        tabulate(
            toc5,
            headers=[
                'Bitwise Asgmt', 'Magic Method'
                ],
            tablefmt='simple'
            ),
        tabulate(
            toc6,
            headers=[
                'Unary', 'Magic Method'
                ],
            tablefmt='simple'
            )
        )
