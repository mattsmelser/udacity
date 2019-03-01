from collections import defaultdict
"""
UNIT 3: Functions and APIs: Polynomials

A polynomial is a mathematical formula like:

    30 * x**2 + 20 * x + 10

More formally, it involves a single variable (here 'x'), and the sum of one
or more terms, where each term is a real number multiplied by the variable
raised to a non-negative integer power. (Remember that x**0 is 1 and x**1 is x,
so 'x' is short for '1 * x**1' and '10' is short for '10 * x**0'.)

We will represent a polynomial as a Python function which computes the formula
when applied to a numeric value x.  The function will be created with the call:

    p1 = poly((10, 20, 30))

where the nth element of the input tuple is the coefficient of the nth power of x.
(Note the order of coefficients has the x**n coefficient neatly in position n of
the list, but this is the reversed order from how we usually write polynomials.)
poly returns a function, so we can now apply p1 to some value of x:

    p1(0) == 10

Our representation of a polynomial is as a callable function, but in addition,
we will store the coefficients in the .coefs attribute of the function, so we have:

    p1.coefs == (10, 20, 30)

And finally, the name of the function will be the formula given above, so you should
have something like this:


    '30 * x**2 + 20 * x + 10'

Make sure the formula used for function names is simplified properly.
No '0 * x**n' terms; just drop these. Simplify '1 * x**n' to 'x**n'.
Simplify '5 * x**0' to '5'.  Similarly, simplify 'x**1' to 'x'.
For negative coefficients, like -5, you can use '... + -5 * ...' or
'... - 5 * ...'; your choice. I'd recommend no spaces around '**'
and spaces around '+' and '*', but you are free to use your preferences.

Your task is to write the function poly and the following additional functions:

    is_poly, add, sub, mul, power, deriv, integral

They are described below; see the test_poly function for examples.
"""
def poly(coefs):
    ret_val = eval('lambda x: ' + horner_formula(coefs),{})
    ret_val.coefs = coefs
    polynomial = []
    for exp, coef in reversed(list(enumerate(coefs))):
        polynomial.append(term(coef,exp))
    ret_val.__name__ = " + ".join(polynomial)
    return ret_val

def term(coef, exp):
    "Return a string representing 'coef * x**exp' in simplified form."
    if exp == 0:
        return str(coef)
    xn = 'x' if (exp == 1) else ('x**' + str(exp))
    return xn if (coef == 1) else '-' + xn if (coef == -1) else str(coef) + ' * ' + xn

def horner_formula(coefs):
    c = coefs[0]
    if len (coefs) == 1:
        return str(c)
    else:
        factor = 'x * ' + horner_formula(coefs[1:])
        if c == 0:
            return factor
        else:
            return '(%s + %s)' % (c,factor)





def same_name(name1, name2):
    """I define this function rather than doing name1 == name2 to allow for some
    variation in naming conventions."""

    def canonical_name(name): return name.replace(' ', '').replace('+-', '-')

    return canonical_name(name1) == canonical_name(name2)


def is_poly(x):
    "Return true if x is a poly (polynomial)."
    ## For examples, see the test_poly function
    #This needs to be worked on, I don't understand this or the solution given


def add(p1, p2):
    "Return a new polynomial which is the sum of polynomials p1 and p2."
    N = max(len(p1.coefs), len(p2.coefs))
    coefs = [0] * N
    for c, e in enumerate(p1.coefs):
        coefs[c] = e
    for c, e in enumerate(p2.coefs):
        coefs[c] += e
    return poly(coefs)

def sub(p1, p2):
    "Return a new polynomial which is the difference of polynomials p1 and p2."
    N = max(len(p1.coefs), len(p2.coefs))
    coefs = [0] * N
    for c, e in enumerate(p1.coefs):
        coefs[c] = e
    for c, w in enumerate(p2.coefs):
        coefs[c] -= e
    return poly(coefs)


def mul(p1, p2):
    "Return a new polynomial which is the product of polynomials p1 and p2."
    results = defaultdict(int)
    for a, c in enumerate(p1.coefs):
        for b, d in enumerate(p2.coefs):
            results[a+b] += (c*d)
    return poly([results[i] for i in range(max(results)+1)])



def power(p, n):
    "Return a new polynomial which is p to the nth power (n a non-negative integer)."
    if n == 0:
        return poly(1,)
    elif n == 1:
        return p
    else:
        return n ** p


"""
If your calculus is rusty (or non-existant), here is a refresher:
The deriviative of a polynomial term (c * x**n) is (c*n * x**(n-1)).
The derivative of a sum is the sum of the derivatives.
So the derivative of (30 * x**2 + 20 * x + 10) is (60 * x + 20).

The integral is the anti-derivative:
The integral of 60 * x + 20 is  30 * x**2 + 20 * x + C, for any constant C.
Any value of C is an equally good anti-derivative.  We allow C as an argument
to the function integral (withh default C=0).
"""


def deriv(p):
    "Return the derivative of a function p (with respect to its argument)."
    derivative = []



def integral(p, C=0):
    "Return the integral of a function p (with respect to its argument)."


"""
Now for an extra credit challenge: arrange to describe polynomials with an
expression like '3 * x**2 + 5 * x + 9' rather than (9, 5, 3).  You can do this
in one (or both) of two ways:

(1) By defining poly as a class rather than a function, and overloading the 
__add__, __sub__, __mul__, and __pow__ operators, etc.  If you choose this,
call the function test_poly1().  Make sure that poly objects can still be called.

(2) Using the grammar parsing techniques we learned in Unit 5. For this
approach, define a new function, Poly, which takes one argument, a string,
as in Poly('30 * x**2 + 20 * x + 10').  Call test_poly2().
"""


"""def test_poly1():
    # I define x as the polynomial 1*x + 0.
    x = poly((0, 1))
    # From here on I can create polynomials by + and * operations on x.
    newp1 = 30 * x ** 2 + 20 * x + 10  # This is a poly object, not a number!
    assert p1(100) == newp1(100)  # The new poly objects are still callable.
    assert same_name(p1.__name__, newp1.__name__)
    assert (x + 1) * (x - 1) == x ** 2 - 1 == poly((-1, 0, 1))


def test_poly2():
    newp1 = Poly('30 * x**2 + 20 * x + 10')
    assert p1(100) == newp1(100)
    assert same_name(p1.__name__, newp1.__name__)"""



#p1 = poly([10,20,30])
#p2 = poly([30,40])
p=poly(5)
n=(3)
#print (add(p1,p2))
#print (sub(p1,p2))
#print (mul(p1,p2))
print (power(p,n))