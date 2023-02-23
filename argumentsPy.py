# Keyword arguments

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# Valid function calls
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# Invalid function calls

# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument


# No argument may receive a value more than once

def function(a):
    pass


function(0, a=1)  # This causes an error - function argument has multiple values

# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])
#
#
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")


# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#     -----------    ----------     ----------
#     |                 | |
#     |         Positional or keyword   |
#     |                              - Keyword
#     -- Positional                    only
#          only
#
# def standard_arg(arg):
#     print(arg)
#
# def pos_only_arg(arg,/):
#     print(arg)

# def kwd_only_arg(*,arg):
#     print(arg)
#
# def combined_example(pos_only,/,standard,*,kwd_only):
#     print(pos_only,standard,kwd_only)
#
#
# standard_arg(2)
# standard_arg(arg=3)
# # both the above method of calling is similar
#
# pos_only_arg(2)
# pos_only_arg(arg=2)  # Passing positional only param as keyword is not allowed

# kwd_only_arg(2)  # Not allowed - Expects 0 positional arg but given one keyword arg

# kwd_only_arg(a=2)  # Not allowed - name of the parameter does not match - Param and argument name should match

# kwd_only_arg(arg=2)
#
# combined_example(1, standard=2,kwd_only =3)

# **kwds to be passed as keywords


# def foo(n, **kwds):
#     if 'name' in kwds:
#         return True
#     elif 'no' in kwds:
#         return True   # name is actually a key within **kwds
#     #return 'name' in kwds


# print(foo(1, **{'name': 2}))

# But using / (positional only arguments), it is possible since it allows name as a
# positional argument and 'name' as a key in the keyword arguments:


def foo(name, /, **kwds):
    # print(name)
    return 'name' in kwds


print(foo(1, **{'name': 2}))

# A return statement ends a function
# Raising an error ends a program
# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
#
#
# ask_ok('Do you really want to quit?')

# i = 5
#
#
# def foo(arg=i):
#     print(arg)
#
#
# i = 6
# foo()   # Note that parameter is not passed because during definition the var i is available defined on line 93
