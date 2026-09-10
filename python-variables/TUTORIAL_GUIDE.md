# Python Variables — Notes & Understanding

This README summarizes the following topics in Python Variables:

- [Python Variables](https://www.w3schools.com/python/python_variables.asp)
- [Python Variable Names](https://www.w3schools.com/python/python_variables_names.asp)
- [Assign Multiple Values](https://www.w3schools.com/python/python_variables_multiple.asp)
- [Output Variables](https://www.w3schools.com/python/python_variables_output.asp)
- [Global Variables](https://www.w3schools.com/python/python_variables_global.asp)

---

## 1. What is a Variable?

A variable is a name that refers to a value. It gives us a convenient way to store and work with data in a Python program.

Python does not require a separate variable declaration. A variable is created when a value is assigned to it.

```python
name = "Alice"
age = 25
```

Here:

- `name` refers to the string `"Alice"`.
- `age` refers to the integer `25`.

The basic assignment syntax is:

```text
variable_name = value
```

The `=` operator assigns the value on the right to the variable on the left.

---

## 2. Python Variables Are Dynamically Typed

Python variables do not need a declared type.

The same variable name can later refer to a value of another type:

```python
x = 4
x = "Sally"
```

Initially, `x` refers to an integer. Later, `x` refers to a string.

This is one of the convenient features of Python's dynamic typing.

### Specifying a Type with Casting

If we want to explicitly convert a value to a particular type, we can use functions such as:

```python
x = str(3)      # "3"
y = int(3)      # 3
z = float(3)    # 3.0
```

### Checking a Variable's Type

The `type()` function tells us the type of the value:

```python
x = 5
y = "John"

print(type(x))
print(type(y))
```

---

## 3. Strings in Variables

A string can be written using either single or double quotes:

```python
name = "John"
name = 'John'
```

Both forms create a string containing the same text.

---

## 4. Variable Names

Python allows short variable names such as `x` and `y`, but descriptive names are usually easier to understand:

```python
age = 20
car_name = "Toyota"
total_volume = 100
```

### Rules for Variable Names

A valid Python variable name:

1. Must start with a letter or `_`.
2. Cannot start with a number.
3. Can contain letters, numbers, and underscores.
4. Is case-sensitive.
5. Cannot be a Python keyword.

### Valid Examples

```python
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```

### Invalid Examples

```python
2myvar = "John"    # starts with a number
my-var = "John"    # '-' is not allowed
my var = "John"    # spaces are not allowed
```

### Case Sensitivity

Python treats different capitalization as different names:

```python
age = 20
Age = 30
AGE = 40
```

These are three separate variables.

---

## 5. Naming Variables with Multiple Words

When a variable name contains several words, naming conventions can make it easier to read.

### Camel Case

The first word starts lowercase and later words start with uppercase letters:

```python
myVariableName = "John"
```

### Pascal Case

Every word starts with an uppercase letter:

```python
MyVariableName = "John"
```

### Snake Case

Words are separated with underscores:

```python
my_variable_name = "John"
```

For normal Python variables, snake_case is a common and readable convention.

---

## 6. Assigning Multiple Values

Python allows multiple assignments in one statement.

### Many Values to Multiple Variables

```python
x, y, z = "Orange", "Banana", "Cherry"
```

This is equivalent to assigning each value to its corresponding variable.

```python
print(x)
print(y)
print(z)
```

The number of variables must match the number of values being assigned.

### One Value to Multiple Variables

The same value can be assigned to several variables:

```python
x = y = z = "Orange"
```

Now all three variables refer to `"Orange"`.

---

## 7. Unpacking a Collection

Python can unpack values from a collection such as a list into separate variables:

```python
fruits = ["apple", "banana", "cherry"]

x, y, z = fruits

print(x)
print(y)
print(z)
```

After unpacking:

- `x` gets `"apple"`.
- `y` gets `"banana"`.
- `z` gets `"cherry"`.

The number of variables should correspond to the number of values being unpacked.

---

## 8. Outputting Variables

The `print()` function is commonly used to display the value of a variable.

```python
x = "Python is awesome"
print(x)
```

### Printing Multiple Variables with Commas

Multiple variables can be passed to `print()` separated by commas:

```python
x = "Python"
y = "is"
z = "awesome"

print(x, y, z)
```

This is especially useful when the values have different data types:

```python
x = 5
y = "John"

print(x, y)
```

### Combining Strings with `+`

Strings can also be joined with `+`:

```python
x = "Python "
y = "is "
z = "awesome"

print(x + y + z)
```

The spaces are part of the strings. Without them, the result would be:

```text
Pythonisawesome
```

### `+` with Numbers

With numbers, `+` performs addition:

```python
x = 5
y = 10

print(x + y)
```

Output:

```text
15
```

### Do Not Use `+` to Directly Combine a String and a Number

This causes a type error:

```python
x = 5
y = "John"

print(x + y)
```

When different types need to be displayed together, passing them separately to `print()` is a simple solution:

```python
print(x, y)
```

---

## 9. Global Variables

A variable created outside a function is a **global variable**.

A global variable can be accessed both outside and inside functions:

```python
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()
```

The function can read the global variable `x`.

---

## 10. Local Variables and Same-Named Variables

If a variable is created inside a function, it is local to that function.

A local variable can have the same name as a global variable:

```python
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)
```

The `x` inside the function is local, so it does not replace the global `x`.

Conceptually:

```text
Global x  -> "awesome"
Local  x  -> "fantastic"
```

They are separate variables in different scopes.

---

## 11. The `global` Keyword

Normally, assigning to a variable inside a function creates or changes a local variable.

The `global` keyword tells Python that we want to work with a variable in the global scope.

### Creating a Global Variable from Inside a Function

```python
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)
```

### Changing an Existing Global Variable

The `global` keyword can also be used when changing a global variable inside a function:

```python
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
```

After `myfunc()` runs, the global `x` has the value `"fantastic"`.

---

## 12. Important Ideas to Remember

### Variable creation

Python creates a variable when we assign a value:

```python
score = 100
```

### Variables can refer to different types

```python
value = 10
value = "ten"
```

### Names are case-sensitive

```python
name != Name
```

### Use descriptive names

Prefer:

```python
student_name = "Alice"
```

over:

```python
x = "Alice"
```

when the meaning of the data matters.

### Multiple assignment is possible

```python
a, b, c = 1, 2, 3
```

### The same value can be assigned to multiple variables

```python
a = b = c = 0
```

### Collections can be unpacked

```python
a, b, c = [1, 2, 3]
```

### `print()` can output several values

```python
print("Age:", 25)
```

### Be careful with `+`

`+` adds numbers and concatenates strings, but it cannot directly combine a string and a number:

```python
5 + 10             # 15
"Hello " + "World" # "Hello World"
```

### Understand scope

A variable inside a function is normally local. A variable outside a function is global.

Use `global` when a function needs to create or modify a global variable.

---

## 13. Quick Reference

| Topic | Example |
|---|---|
| Create a variable | `x = 10` |
| String variable | `name = "Alice"` |
| Check type | `type(x)` |
| Convert to string | `str(10)` |
| Convert to integer | `int(10.5)` |
| Convert to float | `float(10)` |
| Multiple assignment | `a, b = 1, 2` |
| Same value | `a = b = 0` |
| Unpacking | `a, b = [1, 2]` |
| Print variable | `print(x)` |
| Print multiple values | `print(x, y)` |
| Global variable | `x = 10` outside a function |
| Modify global in function | `global x` |

---

## 14. A Small Example Combining the Concepts

```python
student_name = "Alice"
student_age = 20
student_course = "Python"

print("Name:", student_name)
print("Age:", student_age)
print("Course:", student_course)

# Multiple assignment
x, y, z = 10, 20, 30

print("Values:", x, y, z)
```

This example demonstrates the main idea: variables give meaningful names to values, and those values can then be used throughout a program.

---

## Conclusion

The main thing I understood from these pages is that **variables are names used to work with values in Python**. Python makes variable creation simple because there is no separate declaration step.

The most important skills are:

- Creating variables with assignment.
- Understanding that Python is dynamically typed.
- Following variable naming rules.
- Using readable naming conventions.
- Assigning several values at once.
- Unpacking collections.
- Printing variables correctly.
- Understanding the difference between local and global variables.
- Using the `global` keyword when a function needs to create or modify a global variable.

Once these concepts are clear, variables become one of the basic building blocks for writing Python programs.

---
