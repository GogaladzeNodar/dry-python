"""
Assignment 1: HTTP Request Builder
Goal: Use functools.partial to simplify HTTP request construction.
Given the following function:

def make_request(method, url, headers=None, data=None):
   print(f"Making {method} request to {url}")
   print(f"Headers: {headers}")
   print(f"Data: {data}")

Your tasks:
1. Create a partial function called post_json that always uses:
   method='POST'
   headers={"Content-Type": "application/json"}

2. Create a partial called get_request that only requires the url.

3. Create a lambda + partial combo that:
   Uses GET method
   Automatically appends ?token=XYZ to every URL.


Call each variant at least 3 times with different values and make sure the printed output reflects the partial bindings.
"""

from functools import partial


def make_request(method, url, headers=None, data=None):
    print(f"Making {method} request to {url}")
    print(f"Headers: {headers}")
    print(f"Data: {data}")


post_json = partial(make_request, "POST", headers={"Content-Type": "application/json"})

get_request = partial(
    make_request, method="GET", headers={"Content-Type": "application/json"}, data=None
)
get_request1 = partial(make_request, method="GET")


x = lambda url: make_request(
    "GET", f"{url}?token=XYZ", headers={"Content-Type": "application/json"}
)


print(
    "Using post_json:",
    post_json(url="http://example.com/api", data={"key": "value"}),
    "\n",
)
print(
    "Using post_json:",
    post_json(url="http://example.com/api2", data={"key": "value2"}),
    "\n",
)
print(
    "Using post_json:",
    post_json(url="http://example.com/api3", data={"key": "value3"}),
    "\n",
)

print("Using get_request:", get_request(url="http://example.com/api"), "\n")
print("Using get_request:", get_request1(url="http://example.com/api2"), "\n")
print("Using get_request:", get_request(url="http://example.com/api3"), "\n")

print("Using lambda + partial:", x(url="http://example.com/api"), "\n")
print("Using lambda + partial:", x(url="http://example.com/api2"), "\n")
print("Using lambda + partial:", x(url="http://example.com/api3"), "\n")


# position in args is important, # if you change the order of the args in the make_request function,
# you will need to adjust the partials accordingly.
# for example, print("Using post_json:",post_json("http://example.com/api", data={"key": "value"}), "\n")
# This will not work because the url is not the first argument in the make_request function.
# and "http://example.com/api" will be passed as the method argument.


# THERE ARE SOME PARAMETERS TOO
print(
    post_json.func
)  # This will print the original function that the partial is based on.
print(
    get_request.keywords
)  # This will print the keyword arguments that were bound in the partial.
print(
    get_request.args
)  # This will print the positional arguments that were bound in the partial.
print(post_json.args)


"""Assignment 2: Text Formatter with Partial
Goal: Use partial to format lines of text and apply it in a file processing workflow.
Given the function:

def format_line(line: str, prefix: str, suffix: str, uppercase: bool = False):
    line = line.strip()
    if uppercase:
        line = line.upper()
    return f"{prefix}{line}{suffix}"
    
Your tasks:
Create a partial function that:
Adds "* " as prefix
Adds " *" as suffix
Converts lines to uppercase
Read from a file named "input.txt" (you can create this manually with a few lines of text).
Use map() to process each line with the partial function.
Write the formatted lines to "output.txt"."""


def format_line(line: str, prefix: str, suffix: str, uppercase: bool = False):
    line = line.strip()
    if uppercase:
        line = line.upper()
    return f"{prefix}{line}{suffix}"


my_formater = partial(format_line, prefix="* ", suffix=" *", uppercase=True)


def main(input_file: str, output_file: str):
    with open(input_file, "r") as infile:
        lines = infile.readlines()

    formatted_lines = map(my_formater, lines)

    with open(output_file, "w") as outfile:
        outfile.writelines(formatted_lines)


if __name__ == "__main__":
    main("input.txt", "output.txt")

    # here, file creation doesn't work but you can create a file named "input.txt" manually
    # or nevermind, I'm trying to understand functools not file handling.
