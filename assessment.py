# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%

def total_item_cost(cost, state_abbreviation, tax=.05):

    """Calculates an item cost by adding tax, depending on a state"""

    if state_abbreviation == "CA":
        return cost + cost * 0.07
    else:
        return cost + cost * tax

# calling function with other than California ctate, without providing tax
print total_item_cost(50, "NY")

# calling function providing a tax of 9%.
print total_item_cost(50, "AL", .09)

# calling function with the state of California, will add 7% tax by default.
print total_item_cost(50, "CA")

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry".

def is_berry(fruit_name):

    """
    Returns True or False if an input of a fruit_name is "strawberry", "cherry",
    or 'blackberry'.

    """

    return fruit_name == "strawberry" or fruit_name == "cherry" or fruit_name == "blackberry"


#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def shipping_cost(fruit_name):

    """
    Returns 0 if calling the function is_berry with the provided fruit_name
    returns True, and 5 if it returns False.

    I don't have to write the whole expression is_berry(fruit_name) == True inside
    the if statement. It is by default has to evaluate to True.

    """

    if is_berry(fruit_name):
        return 0
    else:
        return 5

# calling function shipping_cost with the argument "strawberry" which should
#evaluete to True and return 0
print shipping_cost("strawberry")  # --> 0


# calling function shipping_cost with the argument "melon" which should
#evaluete to False and return 5
print shipping_cost("melon")  # --> 5


# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.

def is_hometown(town_name):

    """
    Returns a boolean depends on an input of the town_name
    It will evaluete to my hometown, which is Moscow

    """
    return town_name == "Moscow"

#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.

def full_name(first_name, last_name):

    """Returns the full name based on the first_name and last_name inputs"""

    return first_name + " " + last_name

#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you
#        from?" depending on what `is_hometown()` evaluates to.

def hometown_greeting(town_name, first_name, last_name):

    """
    Prints greeting depends on the return of calling is_hometown() and full_name()
    functions with town name and name inputs.

    If is_hometown() evaluates to True it will print first greeting, calling the
    full_name() function.

    If it evaluets to False it will print the second greeting, also calling the
    full_name() function.

    """

    if is_hometown(town_name):
        print "Hi, %s, we're from the same place!" % (full_name(first_name, last_name))
    else:
        print "Hi %s, where are you from?" % (full_name(first_name, last_name))

# Calling the function. It has to evaluate is_hometown() function to True and
#print the first message
hometown_greeting("Moscow", "Natasha", "Zhoglo")

#Calling the function with the inputs which will evaluate is_hometown() function
#to False and print the second message
hometown_greeting("Paris", "Kate", "Simpson")

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()``
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

def increment(x=1):

    """
    Returns the inner function add(y), which sums x and y.

    To get access to the add() inner function we should call it's outter function
    increment() with any value of x we want (it's 1 by default) and store it
    in a variable.

    This variable will store the inner function with x value, that we passed with
    the outter function. But to return a value from the inner function add(),
    we should call this variable with any integer as an argument we want to be
    incremented by 1 (since x = 1 by default).

    """
    def add(y):
        return x + y
    return add

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call
#    addfive with y = 5. Call again with y = 20.


# Here we are passing 5 to the function increment().
# This value is captured and stored in the inner function that gets returned
# So whatever value it will be called with in future, will be increased by 5.
addfive = increment(5)

# we return the value of the inner function by calling it, with any value we want to be
# increased by 5

print addfive(5)  # --> 10
print addfive(20)  # --> 25

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def append_number_to_list(number, input_list):

    """

    Takes a number and a list of numbers and appends the number to the end of the list.
    Returns an updated list.

    """

    input_list.append(number)
    return input_list

# calling the function with a number and a list of numbers
print append_number_to_list(10, [1, 5, 8, 9, 20])    # --> [1, 5, 8, 9, 20, 10]



#####################################################################
