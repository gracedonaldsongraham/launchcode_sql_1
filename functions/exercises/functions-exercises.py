# Part 1 A -- Make a Line

def make_line(size):
    line = ""
    for i in range(size):
        line += '#'
    return line

print(make_line(7))

# Part 1 B -- Make a Square
# create a function using your make_line function to code a square

#function name: make_square
#data (parameters): size of square
#datatype of parameters: int
#parameter name: size
#function will return a value
#return value datatype: string


def make_square(size):
    square = '' # TO DO make a square of hashes, size by size 
    for i in range(size):
        square += make_line(size)
        if i < size - 1:
            square += '\n'
    return square #strings of hash squares

print(make_square(5))

# Part 1 C -- Make a Rectangle

def make_rectangle(width, height):
    rectangle = ''
    for i in range(height):
        rectangle += make_line(width)
        if i < height - 1:
            rectangle += '\n'
    return rectangle

print(make_rectangle(3, 4))


def make_line(size):
    line = ""
    for i in range(size):
        line += '#'
    return line

print(make_line(10))

# Part 2 A -- Make a Stairs

def make_downward_stairs(height):
    stairs = ''
    for i in range(height):
        stairs += make_line(i+1)
        if i < height - 1:
            stairs += '\n'
    return stairs

print(make_downward_stairs(7))


# Part 2 B -- Make Space-Line 

def make_space_line(numSpaces, numChars):
    line = '' # print the spaces, print the chars, print the spaces again
    for i in range(numSpaces):
        line += ' '
    for i in range(numChars):
        line += '#'
    for i in range(numSpaces):
        line += ' '
    return line

print(make_space_line(3,5))

# Part 2 C -- Make Isosceles Triangle
# Then line i is a space-line with [height - i - 1] spaces and [2 * i + 1] hashes.

def make_isosceles_triangle(height):
    triangle = ''
    for i in range(height):
        triangle += make_space_line((height - i - 1), (2 * i + 1))
        if i < height - 1:
            triangle += "\n"
    return triangle

print(make_isosceles_triangle(5))

# Part 3 -- Make a Diamond

def make_diamond(height):
   diamond = ""
   for i in range(height):
      spaces = " " * (height - i - 1)
      hash = "#" * (2 * i + 1)
      diamond += spaces + hash + "\n"

   for i in range(height - 2, -1, -1):
      spaces = " " * (height - i - 1)
      hash = "#" * (2 * i + 1)
      diamond += spaces + hash + "\n"

   return diamond

print(make_diamond(5))