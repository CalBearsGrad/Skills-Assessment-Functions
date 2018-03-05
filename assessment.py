"""
Skills function assessment.

Please read the instructions first. Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

#    (a) Write a function that takes a town name as a string and returns
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.

###############################################################################

# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry",
#        "blackberry", or "currant."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a fruit name and a list of fruits. It should
#        return a new list containing the elements of the input list, along with
#        given fruit, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price of $100 or less and $3 for items over $100. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.


def is_hometown(town_name):
    """ This function takes a town name as a string and returns `True` if it is your hometown, and `False` otherwise. """
    if town_name.lower() == "oakland":
        #I added a print statement to see if it worked
        #print True
        return True
    else:
        #print statement to check if it worked
        #print False
        return False
        
is_hometown("oakland")

def make_name(first_name, last_name):
    """This function takes a first and last name as arguments and returns the concatenation of the two names in one string.  """
    #print first_name + " " + last_name
    return first_name + " " + last_name
    
make_name("Marijane", "Castillo")

def meet(hometown, first_name, last_name):
    """ This is a function that takes a home town, a first name, and a last name as arguments, calls both functions from part (a) and (b) and prints "Hi, 'full name here', we're from the same place!", or "Hi 'full name here', I'd like to visit 'town name here'!" depending on what the function from part (a) evaluates to. """
    town = is_hometown(hometown)
    full_name = make_name(first_name, last_name)
    if town == True:
        print "Hi", full_name, ", we're from the same place!"
    else:
        print "Hi", full_name, ", I'd like to visit", hometown, "!"
meet("Gilroy", "Marijane", "Castillo")

def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """
    if fruit.lower() == "strawberry" or fruit.lower() == "rasberry" or fruit.lower() == "blackberry" or fruit.lower() == "currant":
        return True
    else:
        return False
    pass



def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """
    shipping_cost_if_berry = is_berry(fruit)
    if shipping_cost_if_berry == True:
        #print 0
        return 0
    else:
        #print 5
        return 5        

    pass

shipping_cost("RASBERRY")


def append_to_list(fruit_list, fruit):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list(['banana', 'apple', 'blackberry'], 'dragonfruit')
    ['banana', 'apple', 'blackberry', 'dragonfruit']

    >>> fruits = ['banana', 'apple', 'blackberry']
    >>> append_to_list(fruits, 'dragonfruit')
    ['banana', 'apple', 'blackberry', 'dragonfruit']
    >>> fruits
    ['banana', 'apple', 'blackberry']

    """

    new_fruit_list = fruit_list[0:]
    new_fruit_list.append(fruit)
    #print "this is new list of fruit: ", new_fruit_list
    return new_fruit_list

    pass

append_to_list(['banana', 'apple', 'blackberry'], 'dragonfruit')




def calculate_price(base_item_price, two_letter_state_abr, state_tax =0.05):
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """
    subtotal = base_item_price + (base_item_price * state_tax)
    
    if two_letter_state_abr.upper() == "CA":
        Cal_fees = 0.03
        total = subtotal + (subtotal * Cal_fees)
        #print total
        return total
    elif two_letter_state_abr.upper() == "PA":
        PA_fees = 2.00
        total = subtotal + PA_fees
        #print total
        return total
    elif two_letter_state_abr.upper() == "MA" and base_item_price <= 100:
        MA_fees = 1.00
        total = subtotal + MA_fees
        #print total
        return total
    elif two_letter_state_abr.upper() == "MA" and base_item_price >= 100:
        MA_fees = 3.00
        total = subtotal + MA_fees
        #print total
        return total
    else:
        total = subtotal
        #print total
        return total

    pass

calculate_price(126, "MA")


###############################################################################

# PART THREE

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.

#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def append_to_list_two(list, *items):
    
    
    for item in items:
        list.append(item)
    #print list to double check
    return list
    
append_to_list_two([1, 2, 3], 1, 2)

final_list = append_to_list_two

def triple_word(word):
    return word + word + word
    
triple_word('balloonicorn')


def multiply_function(word, function):
        
    triplicate = function(word)

    #print word, "", triplicate
    return word, "", triplicate
    

multiply_function('Balloonicorn', triple_word)




###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
