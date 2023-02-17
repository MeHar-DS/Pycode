# def f(a, L = None):
#     L = []
#     L.append(a)
#     return L


# def f(a, L=[]):
#     """ Default values are evaluated only once and at the beginning of the definition"""
#     """ Invoking f multiple times  creates accumulation of values rather than assigning unique individual values"""
#     L.append(a)
#     return L


def f(a= "StringsOfBeethoven"):
    print("Value of a: ", a)
    #return a


print(f(1))
print(f(2))
print(f(3))