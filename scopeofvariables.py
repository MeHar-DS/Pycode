
def var_scope_demo():
    global x
    x = 20
    print(x)


#var_scope_demo()

def var_scope_demo1():
    print(x)   # accessed due to global definition in var_scope_demo()


# LEGB RULE - > Local-> Enclosing-> Global -> Built-In

def var_scope_demo2():
    global x
    x = 20
    print(x)

    def var_scope_demo3():   # Nesting of functions
        print(x)
        #var_scope_demo3()  # This doesnt work somehow doesnt invoke 3()-not sure why
        def grandchild():
            print(x)
        grandchild()
    var_scope_demo3()


var_scope_demo2()