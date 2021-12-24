import tabulate
tabulate.PRESERVE_WHITESPACE = True


def intro():
    print("\n")
    print("""Assignment Operators are special symbols that are used to carry
out arithmetic, logical, or bitwise computations. The value that the operator
operates on is known as the 'Operand'.

""")
    from tabulate import tabulate

    toc = [
        ['     =', """Assign value of right side of the expression to the
left side of the operand.""", 'x = y + z'],
        [' ', ' ', ' ', ' '],
        ['    +=', """Add AND: Add right-side operand with left side
operand and then assign to left operand.""", 'a += b', 'a = a + b'],
        [' ', ' ', ' ', ' '],
        ['    -=', """Subtract AND: Subtract right operand from left
operand and then assign to left operand.""", 'a -= b', 'a = a - b'],
        [' ', ' ', ' ', ' '],
        ['    *=', """Multiply AND: Multiply right operand with left
operand and then assign to left operand.""", 'a *= b', 'a = a * b'],
        [' ', ' ', ' ', ' '],
        ['    /=', """Divide AND: Divide left operand with right operand
and then assign to left operand.""", 'a /= b', 'a = a * b'],
        [' ', ' ', ' ', ' '],
        ['    %=', """Modulus AND: Takes modulus using left and right
operands and assign the result to left operand.""", 'a %= b', 'a = a % b'],
        [' ', ' ', ' ', ' '],
        ['    //=', """Divide(floor) AND: Divide left operand with right
operand and then assign the value to left operand.""",
            'a //= b', 'a = a // b'],
        [' ', ' ', ' ', ' '],
        ['    **=', """Exponent AND: Calculate exponent (raise power)
value using operands and assign value to left operand.  """,
            'a **= b', 'a = a ** b'],
        [' ', ' ', ' ', ' '],
        ['    &=', """Performs Bitwise AND on operands and assign value
to left operand.""", 'a &= b', 'a = a & b'],
        [' ', ' ', ' ', ' '],
        ['    |=', """Performs Bitwise OR on operands and assign value to
left operand.""", 'a |= b', 'a = a | b'],
        [' ', ' ', ' ', ' '],
        ['    ^=', """Performs Bitwise xOR on operands and assign value
to left operand.""", 'a ^= b', 'a = a ^ b'],
        [' ', ' ', ' ', ' '],
        ['    >>=', """Performs Bitwise right shift on operands and
assign value to left operand.""", 'a >>= b', 'a = a >> b'],
        [' ', ' ', ' ', ' '],
        ['    <<=', """Performs Bitwise left shift on operands and assign
value to left operand.""", 'a <<= b', 'a = a << b']
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
