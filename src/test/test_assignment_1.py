from sympy import *
import math

def Question1(x):
      
    sign = int(x[0])

    c = 0
    f = 0

    for i in range(1, 12):
        c += int(x[i])*(2**(11-i))


    
    length = len(x)

    for i in range(12, length):
        f += int(x[i])*((1/2)**(i-11))


    result = ((-1)**sign)*(2**(c-1023))*(1+f)


    print('%.4f' % result)
    return result


def Question2(x):
        
        i = 0

        while x > 1:
            x = x/10
            i += 1

        x = float(str(x)[:5])

        while i > 0:
            x = x*10
            i -= 1

        print(x)
        return x


def Question3(x):

        i = 0

        while x > 1:
            x = x/10
            i += 1

        x = round(x , 3) 

        while i > 0:
            x = x*10
            i -= 1

        print(x)
        return x

def Question4(x):

    print("True Value:")
    tValue = Question1(x)

    print("Using Chopping Method:")
    Question2(tValue)

    print("Using Rounding Method:")
    rError = Question3(tValue)
    error = abs( tValue - rError)

    print("Absolute Error:")
    print('%.4f' % error)

    print("Relative Error:")
    print(error / tValue)

#----------------------------------------------------------------------------------
def check_for_negative_1_exponent_term(function: str) -> bool:
    if "-1**k" in function:
        return True
    return False

def check_for_alternating(function_we_got: str):
    term_check = check_for_negative_1_exponent_term(function_we_got)
    return term_check

def check_for_decreasing(function_we_got: str, x: int):
    decreasing_check = True
    k = 1
    starting_val = abs(eval(function_we_got))
    for k in range(2, 10):
        result = abs(eval(function_we_got))
        if starting_val <= result:
            decreasing_check = False

    return decreasing_check

def use_minimum_term_function(function_a, x, tolerance):
    k = symbols("k", positive = true)
    expr = eval(function_a)
    expr = abs(expr.subs(k, k+1)) - tolerance

    solution = solve(expr , k)
    solution[0] = math.ceil(solution[0])

    print("Min number of iterations:")
    print(solution[0])
  



def Question5():
    function_a: str = "(-1**k) * (x**k) / (k**3)"
    tolerance = 10**(-4)
    x: int = 1
    check1: bool = check_for_alternating(function_a)
    check2: bool = check_for_decreasing(function_a, x)
    if check1 and check2:
        use_minimum_term_function(function_a, x, tolerance) 


#----------------------------------------------------------------------------------
def custom_derivative(value):
    return (3 * value* value) + (8 * value)

def bisection_method(left: float, right: float, given_function: str):
    x = left
    intial_left = eval(given_function)
    x = right
    intial_right = eval(given_function)
    if intial_left * intial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the function")
        return
    tolerance: float = 10**(-4)
    diff: float = right - left

    iteration_counter = 0
    while (diff >= tolerance):
        iteration_counter += 1
        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(given_function)
        if evaluated_midpoint == 0.0:
            break

        x = left
        evaluated_left_point = eval(given_function)
        

        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint >0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0
        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point

        diff = abs(right - left)
        
    print("Bisection Method:")
    print(iteration_counter)

    return mid_point

def newton_raphson(initial_approximation: float, tolerance: float, sequence: str):
    iteration_counter = 0
    x = initial_approximation
    f = eval(sequence)
    f_prime = custom_derivative(initial_approximation)
    
    approximation: float = f / f_prime
    while(abs(approximation) >= tolerance):
        x = initial_approximation
        f = eval(sequence)
        f_prime = custom_derivative(initial_approximation)
        approximation = f / f_prime
        initial_approximation -= approximation
        iteration_counter += 1

    print("Newton-Raphson Method:")
    print(iteration_counter)

#----------------------------------------------------------------------------------

def Question6():

    #Bisection Method
    left = -4
    right = 7
    function_string = "(x**3) + 4*(x**2) - 10"
    bisection_method(left, right, function_string)


    #Newton-Raphson Method
    initial_approximation: float = -4
    tolerance: float = 10**(-4)
    newton_raphson(initial_approximation, tolerance, function_string)

    
if __name__ == "__main__":

    Question4("010000000111111010111001")
    Question5()
    Question6()
