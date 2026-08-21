# Python Fundamentals Tutorial Guide

This guide distills the key beginner concepts covered by the five W3Schools Python pages supplied for this task: syntax, statements, output, numeric output, and comments.

## 1. Python Syntax

Python code can be run interactively in the Python command line or saved in a `.py` file and executed with Python. A major feature of Python syntax is **indentation**: spaces at the beginning of a line define blocks of code, so indentation is part of the language syntax rather than merely a formatting convention.

### Running Python

Interactive example:

```python
>>> print("Hello, World!")
Hello, World!
```

A Python file can be run from a command line with:

```text
python myfile.py
```

### Indentation

Indentation is required when a statement belongs to a block such as an `if` statement.

```python
if 5 > 2:
    print("Five is greater than two!")
```

Important rules:

- A block must be indented.
- The amount of indentation is up to the programmer, but at least one space is required.
- Four spaces are a common convention.
- Statements in the same block should use the same indentation.
- Inconsistent indentation can produce a syntax or indentation error.

### Variables

A variable is created when a value is assigned to a name:

```python
x = 5
message = "Hello, World!"
```

Python does not require a separate variable-declaration command before assignment.

---

## 2. Python Statements

A **statement** is an instruction that Python executes. A program normally consists of a sequence of statements.

```python
print("Hello World!")
print("Have a good day.")
print("Learning Python is fun!")
```

Python normally treats the end of a line as the end of a statement, so semicolons are not required.

### Statement Execution Order

Statements are normally executed from top to bottom, in the order in which they appear:

```python
print("First")
print("Second")
print("Third")
```

Output:

```text
First
Second
Third
```

### Semicolons

Python permits multiple statements on one line when they are separated by semicolons:

```python
print("Hello"); print("How are you?"); print("Bye!")
```

However, this style is rarely recommended because separate lines are easier to read.

This is invalid because there is no separator between the statements:

```python
print("Python is fun!") print("Really!")
```

**Best practice:** normally put one statement on each line.

---

## 3. Printing Output

The `print()` function displays text or values as output.

```python
print("Hello World!")
```

You can call `print()` multiple times:

```python
print("Hello World!")
print("I am learning Python.")
print("It is awesome!")
```

Each call normally ends with a newline, so each message appears on a separate line.

### Strings Need Quotes

Text should be enclosed in quotes. Both single and double quotes are valid:

```python
print("This will work!")
print('This will also work!')
```

Leaving text unquoted can cause a syntax error:

```python
print(This will cause an error)
```

Use quotes when the value is literal text.

### Printing on the Same Line

By default, `print()` ends with a newline. The `end` parameter lets you change what is printed at the end.

```python
print("Hello World!", end=" ")
print("I will print on the same line.")
```

Output:

```text
Hello World! I will print on the same line.
```

---

## 4. Printing Numbers

Numbers are printed without quotation marks:

```python
print(3)
print(358)
print(50000)
```

If you put a number inside quotes, Python treats it as text rather than as a numeric value.

### Arithmetic in `print()`

Python can calculate an expression inside `print()`:

```python
print(3 + 3)
print(2 * 5)
```

Output:

```text
6
10
```

This makes `print()` useful for displaying calculated results.

### Mixing Text and Numbers

Text and numbers can be passed to `print()` as separate arguments, separated by commas:

```python
print("I am", 35, "years old.")
```

Python displays the values together with spaces between the arguments.

---

## 5. Python Comments

Comments are notes in source code that Python does not execute. They can be used to:

- Explain code.
- Make code easier to understand.
- Temporarily prevent a line from executing while testing.

### Single-Line Comments

A comment starts with `#`:

```python
# This is a comment
print("Hello, World!")
```

Python ignores everything after `#` on that line.

### Comments After Code

A comment can also appear after executable code:

```python
print("Hello, World!")  # This is a comment
```

Only the code before the `#` is executed.

### Temporarily Disabling Code

A line can be commented out to prevent it from executing:

```python
# print("Hello, World!")
print("Cheers, Mate!")
```

The first `print()` does not run because it has been turned into a comment.

### Multiline Comments

Python does not have a dedicated multiline-comment syntax. The straightforward approach is to put `#` at the beginning of each line:

```python
# This is a comment
# written across
# several lines
print("Hello, World!")
```

A triple-quoted string can also appear as an unassigned string literal:

```python
"""
This is a multiline note.
It spans several lines.
"""
print("Hello, World!")
```

For ordinary comments, using `#` is clearer. Triple-quoted strings have other legitimate uses in Python, especially as documentation strings when placed in the appropriate context.

---

## 6. Putting the Concepts Together

The following small program combines syntax, indentation, statements, output, numbers, variables, and comments:

```python
# Store values in variables
name = "Alex"
age = 20

# Print text and numbers
print("Name:", name)
print("Age:", age)

# Use an indented block
if age >= 18:
    print("Adult")

# Perform arithmetic and print the result
print("Next year:", age + 1)
```

### What This Demonstrates

1. `#` starts comments.
2. `name = "Alex"` and `age = 20` create variables through assignment.
3. Each line is normally a separate statement.
4. `print()` displays text, variables, and calculated values.
5. Numbers can be used directly in arithmetic without quotes.
6. The `if` block is identified by indentation.
7. The program executes its statements in order.

---

## 7. Beginner Rules to Remember

| Topic | Rule |
|---|---|
| Indentation | Use indentation to define code blocks. |
| Indentation consistency | Keep the same indentation level within a block. |
| Statements | Python normally ends a statement at the end of a line. |
| Semicolons | They are optional but usually unnecessary. |
| Output | Use `print()` to display values. |
| Text | Put string literals inside single or double quotes. |
| Numbers | Numeric literals do not need quotes. |
| Arithmetic | Expressions can be evaluated inside `print()`. |
| Same-line output | Use the `end` parameter with `print()`. |
| Comments | Start a comment with `#`. |
| Commented-out code | Prefix executable code with `#` to prevent that line from running. |

---

## 8. Practice Exercises

### Exercise 1: Basic Output

Write a program that prints three separate lines:

```text
Hello!
I am learning Python.
Python is fun!
```

### Exercise 2: Numbers

Print the numbers `10`, `25`, and `100`, then print the result of:

```python
7 + 8
```

### Exercise 3: Variables

Create variables for a person's name and age, then print both values.

### Exercise 4: Same-Line Output

Use `end` so that two `print()` calls appear on the same line.

### Exercise 5: Indentation

Write an `if` statement that prints `"You are an adult."` when an `age` variable is at least 18. Make sure the `print()` statement is indented.

### Exercise 6: Comments

Add comments explaining what each part of a short Python program does. Then comment out one `print()` statement and observe that it no longer executes.

---

## 9. Quick Reference

### Print text

```python
print("Hello")
```

### Print a number

```python
print(42)
```

### Print a calculation

```python
print(10 + 5)
```

### Print text and a number

```python
print("Score:", 95)
```

### Print without moving to a new line

```python
print("Hello", end=" ")
print("World")
```

### Create a variable

```python
x = 10
```

### Create an indented block

```python
if x > 5:
    print("x is greater than 5")
```

### Write a comment

```python
# Explain what the next line does
print("Hello")
```

---

## 10. Key Takeaway

The core beginner ideas from these lessons fit together simply:

**Python programs are sequences of statements. Statements are normally written one per line. Indentation defines blocks of code. `print()` displays output, numbers can be calculated directly, and comments beginning with `#` help explain or temporarily disable code.**

Once these rules become familiar, you have the foundation needed to move on to variables, data types, operators, conditions, loops, and functions.

## Sources

The guide is based on the five W3Schools pages supplied for this task:

- [Python Syntax](https://www.w3schools.com/python/python_syntax.asp)
- [Python Statements](https://www.w3schools.com/python/python_statements.asp)
- [Python Output](https://www.w3schools.com/python/python_output.asp)
- [Python Output Numbers](https://www.w3schools.com/python/python_output_numbers.asp)
- [Python Comments](https://www.w3schools.com/python/python_comments.asp)
