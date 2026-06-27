*variables in python*

A variable is a reference bound to an object in Python's memory model. Understanding this matters because mutable objects, references, copying, and debugging behavior depend on this.

1. Assignment vs. Copying
Because variables are just references, assigning one variable to another (b = a) only copies the reference, not the underlying object.

# Both variables point to the exact same list ID in memory
a = [1, 2, 3]
b = a 
print(id(a) == id(b))  # True

If you want a new object, you must explicitly copy it using methods like .copy() or the copy module.


*how Python handles variables and memory.*

1. The Setup
a = [1, 2, 3]
b = a
Instead of creating two separate lists, Python makes both variables
a and b point to the same location in your computer's memory.
They are like two different nicknames for the exact same person.

2. The Modification
b.append(4)
When you modify b, you are modifying the underlying list object that b points to. Since a is pointing to that exact same object, any changes made through b will naturally reflect when you look at a.

3. How to prevent this (How to copy a list)
If you actually want b to be a completely independent copy so that modifying it doesn't affect a, you have a few easy ways to do it:

Using the .copy() method:
a = [1, 2, 3]
b = a.copy()  # Creates a brand new list with the same values
b.append(4)
print(a)  # Output: [1, 2, 3]
print(b)  # Output: [1, 2, 3, 4]

Using list slicing [:]:
b = a[:]  # Another common way to clone a list

