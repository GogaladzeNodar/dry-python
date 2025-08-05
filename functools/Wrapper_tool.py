"""
Exercise 1: Timing Wrapper
Objective:
Build a decorator measure_time that measures and prints how long a function takes to run.
Requirements:
Use time module to calculate execution duration in seconds.
Use wraps.
Apply to a function that simulates a delay (e.g. time.sleep(2)).
Print result like:
Executed slow_function in 2.0013 seconds
"""

from functools import wraps
import time


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"Executed in {duration:.4f} seconds")
        return result

    return wrapper


# @timer
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)


# fibonacci(10)
# print("---------------------------------------------------", "\n")
# fibonacci(20)
# print("---------------------------------------------------", "\n")
# fibonacci(10)

# BECAUSE THE ABOVE FUNCTION IS RECURSIVE, IT COUNTS THE TIME FOR EACH RECURSIVE CALL.
# i didn't know that it would be like this.

# let's try with a function that has a delay


@timer
def sum_numbers(n):
    """This function sums numbers from 0 to n-1 with a delay."""
    total = 0
    for i in range(n):
        total += i
        time.sleep(0.001)
    return total


sum_numbers(1000)


# now let's talk about @wraps, what difference does it make?
# code without @wraps works same way as with @wraps


def timer2(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"Executed in {duration:.4f} seconds")
        return result

    return wrapper


@timer2
def sum_numbers2(n):
    """This function sums numbers from 0 to n-1 with a delay."""
    total = 0
    for i in range(n):
        total += i
        time.sleep(0.001)
    return total


sum_numbers2(1000)
"""
(venv) nodara@nodars-Laptop functools % "/Users/nodara/Desktop/py_lab/functools/venv/bin/python"
 "/Users/nodara/Desktop/py_lab/functools/Wrapper_tool.py"
Executed in 1.2602 seconds
Executed in 1.2682 seconds
"""

# the difference is that with @wraps, the original function's name and docstring are preserved.
print("sum number.name -> ", sum_numbers.__name__)
print("sum number.doc -> ", sum_numbers.__doc__)

print("sum number2.name -> ", sum_numbers2.__name__)
print("sum number2.doc -> ", sum_numbers2.__doc__)

# answer is:
"""
Executed in 1.2662 seconds
Executed in 1.2628 seconds
sum number.name ->  sum_numbers
sum number.doc ->  This function sums numbers from 0 to n-1 with a delay.
sum number2.name ->  wrapper
sum number2.doc ->  None
"""
# because sum_numbers function is decorated with @wraps, it meintains original functions name and docstring.
# but sum_number2 have docs and name of the wrapper function, not the original function.

# this is not only metadata that is preserved, in python offocial documentation,
# '__module__', '__name__', '__qualname__', '__annotations__', '__doc__', '__type_params__' are WRAPPER_ASSIGNMENTS
# https://docs.python.org/3/library/functools.html


"""
Exercise 3: Permission Checker with Arguments (Advanced)
Objective:
Create a parameterized decorator require_permission(permission_name) that:
Wraps a function
Checks if a user has a certain permission
If yes, runs the function
If not, prints: "Access denied: missing <permission_name>"
Requirements:
Simulate a user object/dict with a list of permissions.
Use three-level decorator structure (wrapper inside decorator inside parameterized decorator).
Use functools.wraps.
Example:
user = {"username": "noda", "permissions": ["read", "write"]}
@require_permission("delete")
def delete_item():
    print("Item deleted.")
"""

user = {"username": "noda", "permissions": ["read", "write"]}


def require_permission(permission_name):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if permission_name in user.get("permissions", []):
                return func(user, *args, **kwargs)
            else:
                print(f"Access denied: missing {permission_name}")

        return wrapper

    return decorator


@require_permission("delete")
def delete_item(user):
    print("Item deleted.")


@require_permission("write")
def write_item(user):
    print("Item written.")


delete_item(user)
write_item(user)
