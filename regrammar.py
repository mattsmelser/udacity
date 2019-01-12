# ---------------
# User Instructions
#
# In this problem, you will be using many of the tools and techniques
# that you developed in unit 3 to write a grammar that will allow
# us to write a parser for the JSON language.
#
# You will have to visit json.org to see the JSON grammar. It is not
# presented in the correct format for our grammar function, so you
# will need to translate it.

# ---------------
# Provided functions
#
# These are all functions that were built in unit 3. They will help
# you as you write the grammar. Add your code at line 102.

from functools import update_wrapper
# from string import split
import re


def grammar(description, whitespace=r'\s*'):
"""Convert a description to a grammar. Each line is a rule for a
non-terminal symbol; it looks like this:
Symbol => A1 A2 ... | B1 B2 ... | C1 C2 ...
where the right-hand side is one or more alternatives, separated by
the '|' sign. Each alternative is a sequence of atoms, separated by
spaces. An atom is either a symbol on some left-hand side, or it is
a regular expression that will be passed to re.match to match a token.

Notation for *, +, or ? not allowed in a rule alternative (but ok
within a token). Use '\' to continue long lines. You must include spaces
or tabs around '=>' and '|'. That's within the grammar description itself.
The grammar that gets defined allows whitespace between tokens by default;
specify '' as the second argument to grammar() to disallow this (or supply
any regular expression to describe allowable whitespace between tokens)."""
G = {' ': whitespace}
description = description.replace('\t', ' ') # no tabs!
for line in str.split(description, '\n'):
lhs, rhs = str.split(line, ' => ', 1)
alternatives = str.split(rhs, ' | ')
G[lhs] = tuple(map(str.split, alternatives))
return G


def decorator(d):
"Make function d a decorator: d wraps a function fn."

def _d(fn):
return update_wrapper(d(fn), fn)

update_wrapper(_d, d)
return _d


@decorator
def memo(f):