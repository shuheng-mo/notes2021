```python
import pybryt
from lecture import ok, pybryt_reference
```

# Introduction to programming in Python

# Lecture 1: Hello world, conditional expressions, loops, and lists

## Learning objectives:

* You will understand that Python will help you defy gravity.
* You will know how to execute Python statements from within Jupyter.
* Understand what a variable is and how to express a mathematical expression in code.
* Print program outputs.
* Access mathematical functions from a Python module.
* Be able to write your own *function*.
* Know how to form a *condition* using a *boolean expression*.
* You will be able to use a conditional expression in combination with a *while-loop* to perform repetitive tasks.
* You will learn how to store data elements within a Python *list*.
* You will learn to use a *for-loop* to iterate, and perform some task over a *list* of elements.

```python
import antigravity
```
![import antigravity](https://imgs.xkcd.com/comics/python.png)

## Programming a mathematical formula

Here is a formula for the position of a ball $y(t)$ in vertical motion, starting at ground level (i.e. at $y=0$) at time $t=0$:

$$ y(t) = v_0t- \frac{1}{2}gt^2, $$

where:

* $y(t)$ is the height (position) as a function of time $t$,
* $v_0$ is the initial velocity (at $t=0$), and
* $g$ is the acceleration due to gravity.

The computational task we want to solve is: given the values of $v_0$, $g$ and $t$, compute the height $y$. 

**How do we program this task?** A program is a sequence of instructions given to the computer. However, while a programming language is much **simpler** than a natural language, it is more **pedantic**. Programs must have correct syntax, i.e. correct use of the computer language grammar rules, and no misprints.

So let us execute a Python statement based on this example to evaluate $y(t) = v_0t- \frac{1}{2}gt^2$ for $v_0 = 5 \,\text{ms}^{-1}$, $g = 9.81 \,\text{ms}^{-2}$ and $t = 0.6 \,\text{s}$. If you were doing this on paper you would probably write something like this: $$y = 5\cdot 0.6 - \frac{1}{2}\cdot 9.81 \cdot 0.6^2.$$ Happily, writing this in Python is very similar:


```python
# Comment: This is a 'code' cell within Jupyter notebook.
# Press Shift-Enter to execute the code within this kind of
# cell, or click 'Run' on the Jupyter toolbar above.

print(5*0.6 - 0.5*9.81*0.6**2)
```

    1.2342


You probably noticed that, in the code cell we just wrote, the first few lines start with the hash (`#`) character. In Python, we use `#` to tell Python interpreter to ignore everything in the line that comes after `#`. We call those lines **comments**, and we write them to help us (humans) understand the code. Besides, we used `print` and enclosed our caluclation within parentheses to display the output. We will explain *comments* and *print function* in more details later.

## Exercise 1.1: Open a code cell and write some code.
1. Navigate the [Jupyter](http://jupyter.org/) toolbar to "Insert"->"Insert Cell Below". Note from the toolbar that you can select a cell to be 'Code' (this is the default), 'Markdown' (the cell you are reading right now is written in [Markdown](https://en.wikipedia.org/wiki/Markdown) - double click this cell to investigate further), and 'Raw' (its content is not evaluated by the notebook).
2. Copy&paste the code from the previous code cell into your newly created code cell below. Make sure it runs!
3. To see how important it is to use the correct [syntax](https://en.wikipedia.org/wiki/Syntax), replace `**` with `^` in your code and try running the cell again. You should see something like the following:

```python
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-6e110a567f02> in <module>
      3 # cell, or click on the 'Run' widget on the Jupyter toolbar above.
      4 
----> 5 print(5*0.6 - 0.5*9.81*0.6^2)

TypeError: unsupported operand type(s) for ^: 'float' and 'int'
```
4. Undo that change so your code is working again; now change `print` to `write` and see what happens when you run the cell. You should see something like:

```python
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-5-a3da902ceb19> in <module>
      3 # cell, or click on the 'Run' widget on the Jupyter toolbar above.
      4 
----> 5 write(5*0.6 - 0.5*9.81*0.6**2)

NameError: name 'write' is not defined
```

While a human might still understand these statements, they do not mean anything to the Python interpreter. Rather than throwing your hands up in the air whenever you get an error message like the above (you are going to see many during the course of these lectures!!!), train yourself to read error messages carefully to get an idea what it is complaining about, and re-read your code from the perspective of the Python interpreter.

Error messages can look bewildering and even frustrating at first, but **it gets much easier with practise**.

## Storing numbers in variables

From mathematics, you are already familiar with variables (e.g. $v_0 = 5$, $g = 9.81$, $t = 0.6$, $y = v_0t - \frac{1}{2}gt^2$), and you already know how important they are for working out complicated problems. Similarly, you can use variables in a program to make it easier to read and understand.


```python
v0 = 5
g = 9.81
t = 0.6
y = v0*t - 0.5*g*t**2
print(y)
```

    1.2342


This program performs the same calculations as the previous one and gives the same output. However, this program spans several lines and uses variables. 

We usually use one letter for a variable in mathematics, resorting to using the Greek alphabet and other characters for more clarity. The main reason for this is to avoid becoming exhausted from writing when working out long expressions or derivations. However, when programming, you should use more descriptive names for variables. This might not seem like an important consideration for the trivial example here. Still, it becomes increasingly important as the program gets more complicated and if someone else has to read your code.

### Good variable names make a program easier to understand!

Permitted variable names include:

* one-letter symbols,
* words or abbreviation of words, and
* variable names can contain lowercase `a-z`, uppercase `A-Z`, underscore (`_`), and digits `0-9`, **but** the name cannot start with a digit or contain a whitespace.

Variable names are case-sensitive (i.e. `a` is different from `A`). Let us rewrite the previous example using more descriptive variable names:


```python
initial_velocity = 5
acceleration_of_gravity = 9.81
TIME = 0.6
VerticalPositionOfBall = initial_velocity*TIME - 0.5*acceleration_of_gravity*TIME**2
print(VerticalPositionOfBall)
```

    1.2342


Certain words have a **special meaning** in Python and **cannot be used as variable names**. We refer to them as **keywords**, and they are:

`and`, `as`, `assert`, `async`, `await`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `nonlocal`, `not`, `or`, `pass`, `raise`, `return`, `try`, `while`, `with`, and `yield`. 

Similarly, `True`, `False`, and `None` are keywords we use for the values of variables, and we cannot use them for variable names. Keywords are very important in programming and, in these lectures, we will learn how to use them.

## Adding comments to code

Not everything written in a computer program is intended for execution. In Python, anything on a line after the `#` character is ignored and is known as a **comment**. You can write whatever you want in a comment. Comments are intended to be used to explain what a snippet of code is intended for. It might, for example, explain the objective or provide a reference to the data or algorithm used. This is useful for you when you have to understand your code at some later stage, and indeed for whoever has to read and understand your code later.


```python
# Program for computing the height of a ball in vertical motion.
v0 = 5    # Set initial velocity in m/s.
g = 9.81  # Set acceleration due to gravity in m/s^2.
t = 0.6   # Time at which we want to know the height of the ball in seconds.
y = v0*t - 0.5*g*t**2  # Calculate the vertical position.
print(y)
```

    1.2342


## Exercise 1.2: Convert from meters to British length units

Here in the UK, we are famous for our love of performing mental arithmetic. That is why we still use both imperial and metric measurement systems - hours of fun entertainment for the family switching back and forth between the two.

Make a program where you set a length given in meters and then compute and write out the corresponding length measured in:
* inches (one inch is 2.54 cm)
* feet (one foot is 12 inches)
* yards (one foot is 12 inches, one yard is 3 feet)
* miles (one British mile is 1760 yards)

**Note**: In this course, we are using [okpy](https://okpy.org/) and [pybryt](https://microsoft.github.io/pybryt/html/index.html) for automated assessment scoring. Therefore, while it is generally important to always carefully follow the instructions of a question, it is particularly important here so that *okpy* and *pybryt* can recognise the validity of your answer.

*Uncomment* and modify the relevant lines in the following code cell. The conversion to inches is done for you to illustrate what is required.


```python
meters = 640

# 1 inch = 2.54 cm. Remember to convert from 2.54 cm to 0.0254 m here.
inches = meters/0.0254

# Uncomment and complete the following code. Do not change variable ames for testing.
feet = inches/12

yards = feet/3

miles = yards/1760

```


```python
with pybryt.check(pybryt_reference(1, 2)):
    feet, yards, miles
```

    REFERENCE: exercise-1_2
    SATISFIED: True
    MESSAGES:
      - SUCCESS: Your conversion to feet is correct. Well done!
      - SUCCESS: Your calculation of yards is correct. Amazing!
      - SUCCESS: Wow! Your conversion to miles is correct.



```python
grade = ok.grade('exercise-1_2')
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Running tests
    
    ---------------------------------------------------------------------
    Test summary
        Passed: 3
        Failed: 0
    [ooooooooook] 100.0% passed



## Formatted printing style

Often we want to print out results using a combination of text and numbers, e.g. "At t=0.6 s, y is 1.23 m". Particularly when printing out floating-point numbers, we should **never** quote numbers to a higher accuracy than they were measured. Python provides a *printf formatting* syntax exactly for this purpose. We can see in the following example where the *slot* `%g` expresses the floating-point number with the minimum number of significant figures, and the *slot* `%.2f` specifies that only two digits are printed out after the decimal point.


```python
print("At t=%g s, y is %.2f m." % (t, y))
```

    At t=0.6 s, y is 1.23 m.


Notice in this example how the values in the tuple `(t, y)` are inserted into the *slots* (`%g` and `%.2f`).

Sometimes we want a multi-line output. This is achieved using a triple quotation, i.e. `"""`:


```python
print("""At t=%f s, a ball with
initial velocity v0=%.3E m/s
is located at the height y=%.2f m.
""" % (t, v0, y))
```

    At t=0.600000 s, a ball with
    initial velocity v0=5.000E+00 m/s
    is located at the height y=1.23 m.



Notice in this example we used `%f`, `%.3E`, and `%.2f` to define slots, into which we inserted the values of `t`, `v0`, and `y` respectively. You can find more details about the format specification mini-language in the Python [documentation](https://docs.python.org/3/library/string.html#format-specification-mini-language).

Instead of using the `%` operator for formatted printing, Python offers another two syntax alternatives: string's `format` method and f-strings. Let us have a look at how we can print "At t=0.6 s, y is 1.23 m" using these two alternative solutions.


```python
print("At t={:g} s, y is {:.2f} m.".format(t, y))  # string's format method
```

    At t=0.6 s, y is 1.23 m.



```python
print(f"At t={t:g} s, y is {y:.2f} m.")  # f-string method - string literal begins with an f
```

    At t=0.6 s, y is 1.23 m.


Notice that we defined slots in a string using curly braces `{}` where we also specified the formatting style in the same way we did before, but this time using `:` instead of `%`. We inserted the values into the slots by passing them to the `format()` method or by writing them in curly braces.

## Exercise 1.3: Compute the air resistance on a football

The drag force, due to air resistance, on an object can be expressed as
$$F_d = \frac{1}{2}C_D\rho Av^2$$
where:
* $\rho$ is the density of the air,
* $v$ is the velocity of the object,
* $A$ is the cross-sectional area (perpendicular to the velocity direction),
* and $C_D$ is the drag coefficient, which depends on the shape of the object and the roughness of the surface.

Complete **and correct** the following code that computes the drag force.


```python
# Import pi (3.14159...) from Python's math library
from math import pi

density = 1.2       # units of kg/m**3
ball_radius = 0.11  # units of m
A = pi*(ball_radius**2)  # Cross sectional area of a spherew
C_D = 0.2           # Drag coefficient

v = 50.8            # m/s (fastest recorded speed of football)

# Uncomment and complete the following line.
F_d = (C_D * density * A * (v**2))/2

# Challenge yourself to use the formatted print statement
# shown above to write out the force with one decimal in
# units of Newton (1 N = 1 kgm/s^2).
```


```python
with pybryt.check(pybryt_reference(1, 3)):
    A, F_d
```

    REFERENCE: exercise-1_3
    SATISFIED: True
    MESSAGES:
      - SUCCESS: Computed cross-sectional area is correct. Great!
      - SUCCESS: Your calculation of the drag force is correct.



```python
grade = ok.grade('exercise-1_3')
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Running tests
    
    ---------------------------------------------------------------------
    Test summary
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed



## How are arithmetic expressions evaluated?
Consider the random mathematical expression, ${5\over9} + 2a^4/2$, implemented in Python as `5.0/9 + 2*a**4/2`. The rules for evaluating the expression are the same as in mathematics: proceed term by term (additions/subtractions) from the left, compute powers first, then multiplication and division. Therefore in this example the order of evaluation will be:

1. `r1 = 5.0/9`
2. `r2 = a**4`
3. `r3 = 2*r2`
4. `r4 = r3/2`
5. `r5 = r1 + r4`

We use parenthesis to override these default rules. Indeed, many programmers use parenthesis for greater clarity.

## Exercise 1.4: Compute the growth of money in a bank

Let $p$ be a bank's annual interest rate in per cent. After $n$ years, an initial amount $A_0$ has then grown to

$$A_n = A_0\left(1+\frac{p}{100}\right)^n.$$

Write a program for computing how much money 1000 euros have grown to after three years with a 5% annual interest rate.


```python
# Uncomment and complete the code below (don't change variable names!)

p = 5
A_0 = 1000
n = 3

A_n = A_0*((1+ p/100)**n)

print("The amount of money in the account after %d years is: %.2f euros" % (n, A_n))
```

    The amount of money in the account after 3 years is: 1157.63 euros



```python
with pybryt.check(pybryt_reference(1, 4)):
    p, A_0, n, A_n
```

    REFERENCE: exercise-1_4
    SATISFIED: True
    MESSAGES:
      - SUCCESS: You set the value of the annual interest rate (p) correctly.
      - SUCCESS: You set the value of the initial amount (A_0) correctly.
      - SUCCESS: You set the number of years (n) correctly.
      - SUCCESS: Amazing! Your final solution (A_n) is correct.



```python
grade = ok.grade('exercise-1_4')
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Running tests
    
    ---------------------------------------------------------------------
    Test summary
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed



## Standard mathematical functions

What if we need to compute $\sin x$, $\cos x$, $\ln x$, $e^x$ etc., in a program? Such functions are available in Python's `math` module. In fact, there is a vast universe of functionality for Python available in modules. We just *import* in whatever we need for the task at hand.

In this example, we compute $\sqrt{2}$ using the `sqrt` function from the `math` module:


```python
import math

# Since we imported library (import math),
# we access the sqrt function using math.sqrt.
r = math.sqrt(2)
print(r)
```

    1.4142135623730951


or:


```python
from math import sqrt

# This time, we did not import the entire library -
# we imported only sqrt function.
# Therefore, we can use it directly.
r = sqrt(2)
print(r)
```

    1.4142135623730951


Let us now have a look at a more complicated expression, such as $\sin x \cos x + 4\ln x$:


```python
from math import sin, cos, log

x = 1.2
print(sin(x)*cos(x) + 4*log(x))   # log is ln (base e)
```

    1.0670178174513938


## Exercise 1.5: Evaluate a Gaussian function

The bell-shaped Gaussian function,

$$f(x)=\frac{1}{\sqrt{2\pi}s}\exp\left(-\frac{1}{2} \left(\frac{x-m}{s}\right)^2\right)$$

is one of the most widely used functions in science and engineering. The parameters $m$ and $s$ are real numbers, and $s$ must be greater than zero. Write a program for evaluating the Gaussian function when $m = 0$, $s = 2$, and $x = 1$.


```python
# Uncomment and complete the code below (don't change variable names!)

from math import pi,sqrt,exp

m = 0
s = 2
x = 1

f_x = (1/(sqrt(2*pi)*s))* exp((-1/2)*(((x-m)/s)**2))
```


```python
with pybryt.check(pybryt_reference(1, 5)):
    f_x
```

    REFERENCE: exercise-1_5
    SATISFIED: True
    MESSAGES:
      - SUCCESS: Great! You computed the value of the Gaussian function correctly.



```python
grade = ok.grade('exercise-1_5')
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Running tests
    
    ---------------------------------------------------------------------
    Test summary
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed



## Exercise 1.6: Find and fix errors in the coding of a formula

Roots of a quadratic equation $ax^2 + bx + c = 0$ are:

$$x_1 = \frac{−b + \sqrt{b^2 −4ac}}{2a},$$
and
$$x_2 = \frac{−b − \sqrt{b^2 −4ac}}{2a}.$$

Uncomment and fix the errors in the following code.


```python
from math import sqrt
#
a = 2
b = 1
c = -2
#
q = sqrt(b*b - 4*a*c)
x1 = (-b + q)/(2*a)
x2 = (-b - q)/(2*a)
```


```python
with pybryt.check(pybryt_reference(1, 6)):
    q, x1, x2
```

    REFERENCE: exercise-1_6
    SATISFIED: True
    MESSAGES:
      - SUCCESS: You compute the square root of the discriminant (q) correctly.
      - SUCCESS: Root x1 of a quadratic equation is correct.
      - SUCCESS: Root x2 of a quadratic equation is correct.



```python
grade = ok.grade('exercise-1_6')
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Running tests
    
    ---------------------------------------------------------------------
    Test summary
        Passed: 3
        Failed: 0
    [ooooooooook] 100.0% passed



## Functions

We have already used Python functions above, e.g. `sqrt` from the `math` module. In general, a function is a collection of statements we can execute wherever and whenever we want. For example, consider any of the formulae we implemented above. 

Functions can take any number of inputs (called *arguments*) to produce outputs. Functions help to organise programs, make them more understandable, shorter, and easier to extend. Wouldn't it be nice to implement it just once and then be able to use it again any time you need it, rather than having to write out the whole formula again?

For our first example, we will reuse the formula for the position of a ball in a vertical motion, which we have seen earlier.


```python
def ball_height(v0, t, g=9.81):
    """Function to calculate and return height of the ball in vertical motion.

    Parameters
    ----------
    v0 : float
         Initial velocity (units, m/s).
    t : float
        Time at which we want to know the height of the ball (units, seconds).
    g : float, optional
        Acceleration due to gravity (units, m/s^2). By default 9.81 m/s^2.

    Returns
    -------
    float
        Height of ball in meters.

    """
    height = v0*t - 0.5*g*t**2

    return height
```

Let us break this example down:
* Function *header*:
    * Functions start with `def` followed by the name we want to give the function (`ball_height` in this case).
    * Following the name, we have parentheses followed by a colon `(...):` containing some number of function *arguments*.
    * In this case, `v0` and `t` are *positional arguments*, while `g` is known as a *keyword argument* (more about this later).
* Function *body*:
    * The first thing to notice is that the body of the function is indented one level. All code that is indented with respect to `def`-line belongs to a function.
    * Best practice is to include a [docstring](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html) to explain to others (or remind our future self) how to use the function.
    * The function output is passed back via the `return` statement.

Notice that this just defines the function. Nothing is executed until we actually *call* the function:


```python
# We pass 5 and 0.6 to v0 and t, respectively.
# The value function returns (height) is put in variable h.
h = ball_height(5, 0.6)

print("Ball height: %g meters." % h)
```

    Ball height: 1.2342 meters.


No return value implies that `None` is returned. `None` is a special Python object that represents an ”empty” or undefined value. It is surprisingly useful, and we will use it a lot later.

Functions can also return multiple values. Let us extend the previous example to calculate the ball's velocity as well as its height:


```python
def ball_height_velocity(v0, t, g=9.81):
    """Function to calculate ball's height and its velocity.

    Parameters
    ----------
    v0 : float
         Initial velocity (units, m/s).
    t : float
        Time at which we want to know the height of the ball (units, seconds).
    g : float, optional
        Acceleration due to gravity (units, m/s^2). By default 9.81 m/s^2.

    Returns
    -------
    float
        Height of ball in meters.
    float
        Velocity of ball in m/s.

    """
    height = v0*t - 0.5*g*t**2
    velocity = v0 - g*t

    return height, velocity


# We pass 5 and 0.6 to v0 and t, respectively.
# The first value function returns (height) is put into variable h,
# whereas the second one (velocity) is placed in v.
h, v = ball_height_velocity(5, 0.6)

print("Ball height: %g meters." % h)
print("Ball velocity: %g m/s." % v)
```

    Ball height: 1.2342 meters.
    Ball velocity: -0.886 m/s.


## Scope: Local and global variables

Variables defined within a function are said to have *local scope*. That is to say that we can only reference them within that function. Consider the example function defined above where we used the *local* variable *height*. You can see that if you try to print the variable height outside the function, you will get an error.

```python
print(height)

---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-50-aa6406a13920> in <module>
----> 1 print(height)

NameError: name 'height' is not defined
```

## Keyword arguments and default input values

Besides *positional arguments*, functions can have arguments of the form `argument_name=value` and they are called *keyword arguments*:


```python
def somefunc(arg1, arg2, kwarg1=True, kwarg2=0):
    print(f'arg1: {arg1}, arg2: {arg2}, kwarg1: {kwarg1}, kwarg2: {kwarg2}')


# Note that we have not specified inputs for kwarg1 and kwarg2.
somefunc("Hello", [1, 2])
```

    arg1: Hello, arg2: [1, 2], kwarg1: True, kwarg2: 0



```python
# Note that we replace the default value for kwarg1.
somefunc("Hello", [1, 2], kwarg1="Hi")
```

    arg1: Hello, arg2: [1, 2], kwarg1: Hi, kwarg2: 0



```python
# Note that we replace the default value for kwarg2.
somefunc("Hello", [1, 2], kwarg2="Hi")
```

    arg1: Hello, arg2: [1, 2], kwarg1: True, kwarg2: Hi



```python
# Here, we replace both default values for keyword arguments kwarg1 and kwarg2.
somefunc("Hello", [1, 2], kwarg2="Hi", kwarg1=6)
```

    arg1: Hello, arg2: [1, 2], kwarg1: 6, kwarg2: Hi


If we use `argument_name=value` for all arguments, their sequence in the function call can be in any order.


```python
somefunc(kwarg2="Hello", arg1="Hi", kwarg1=6, arg2=[2])
```

    arg1: Hi, arg2: [2], kwarg1: 6, kwarg2: Hello


## Exercise 1.7: Implement a Gaussian function

Write a Python function to compute the Gaussian function:

$$f(x)=\frac{1}{s\sqrt{2\pi}}\exp\left(-\frac{1}{2} \left(\frac{x-m}{s}\right)^2\right)$$


```python
# Uncomment and complete this code - keep the names the same for testing purposes.

def gaussian(x, m=0, s=1):
    f_x = (1/(sqrt(2*pi)*s))* exp((-1/2)*(((x-m)/s)**2))
```


```python
with pybryt.check(pybryt_reference(1, 7)):
    gaussian(0.5)
```

    REFERENCE: exercise-1_7
    SATISFIED: True
    MESSAGES:
      - SUCCESS: Your implementation of Gaussian functon is correct. Well done!



```python
ok.grade('exercise-1_7')
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Running tests
    
    ---------------------------------------------------------------------
    question 1.7 > Suite 3 > Case 1
    
    import numpy as np
    >>> np.allclose(gaussian(0.5), 0.3520653267642995)
    Traceback (most recent call last):
      File "<__array_function__ internals>", line 5, in allclose
      File "/opt/jupyter/lib/python3.8/site-packages/numpy/core/numeric.py", line 2249, in allclose
        res = all(isclose(a, b, rtol=rtol, atol=atol, equal_nan=equal_nan))
      File "<__array_function__ internals>", line 5, in isclose
      File "/opt/jupyter/lib/python3.8/site-packages/numpy/core/numeric.py", line 2355, in isclose
        xfin = isfinite(x)
    TypeError: ufunc 'isfinite' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
    
    # Error: expected
    #     True
    # but got
    #     Traceback (most recent call last):
    #       ...
    #     TypeError: ufunc 'isfinite' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
    
    Run only this test case with "python3 ok -q exercise-1_7 --suite 3 --case 1"
    ---------------------------------------------------------------------
    Test summary
        Passed: 8
        Failed: 1
    [ooooooook..] 88.9% passed






    {'passed': 8, 'failed': 1, 'locked': 0}



## Exercise 1.8: How to cook the perfect egg

You just started University and moved away from home. You're trying to impress your new flatmates by cooking brunch. Write a Python script to help you cook the perfect egg! 

You know from A-levels that, when the temperature exceeds a critical point, the proteins in the egg first denature and then coagulate. The process becomes faster as the temperature increases. In the egg white, the proteins start to coagulate for temperatures above 63$^\circ$C, while in the yolk the proteins start to coagulate for temperatures above 70$^\circ$C. 

The time $t$ (in seconds) it takes for the centre of the yolk to reach the temperature $T_y$ (in degrees Celsius) can be expressed as: 

$$t = \frac{M^{2/3}c \rho^{1/3}}{K \pi^2 (4 \pi /3)^{2/3} } ln \left[0.76 \frac{T_0-T_w}{T_y-T_w}\right]$$

where:
* $M$ is the mass of the egg;
* $\rho$ is the density;
* $c$ is the specific heat capacity;
* $K$ is thermal conductivity;
* $T_w$ temperature of the boiling water (in $^\circ$C);
* $T_0$ is the initial temeprature of the egg (in $^\circ$C), before being put in the water.

Write a function that returns the time $t$ needed for the egg to cook, knowing that $T_w = 100^\circ\text{C}$, $M = 50\,\text{g}$, $\rho = 1.038\,\text{gcm}^{−3}$, $c = 3.7\,\text{Jg}^{−1}\text{K}^{−1}$, and $K = 5.4 \cdot 10^{−3}\,\text{Wcm}^{−1}\text{K}^{−1}$. Find $t$ for an egg taken from the fridge ($T_0 = 4^\circ\text{C}$) and for one at room temperature ($T_0 = 20^\circ\text{C}$). $T_y = 70^\circ\text{C}$ for a perfect soft-boiled egg.

**Hint**: You do not need to do any unit conversion. 


```python
# Uncomment and complete this code - keep the names the same for testing purposes.

from math import pi, log

def perfect_egg(T0, M=50, rho=1.038, Tw=100, c=3.7, K=5.4e-3, Ty=70):
    t = ((M**(2/3))*c*(rho**(1/3)) / (K*(pi**2)*((4*pi/3)**(2/3))))* log(0.76*((T0-Tw)/(Ty-Tw)))
    return t
```


```python
with pybryt.check(pybryt_reference(1, 8)):
    perfect_egg(T0=4, M=50, rho=1.038, Tw=100, c=3.7, K=5.4e-3, Ty=70)
    perfect_egg(T0=20, M=50, rho=1.038, Tw=100, c=3.7, K=5.4e-3, Ty=70)
```

    REFERENCE: exercise-1_8
    SATISFIED: True
    MESSAGES:
      - SUCCESS: Your function computes correct time for an egg at the fridge temperature to be perfectly cooked. Well done!
      - SUCCESS: The time for an egg at the room temperature to be perfectly cooked is correct. Well done!



```python
ok.grade('exercise-1_8')
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Running tests
    
    ---------------------------------------------------------------------
    Test summary
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed






    {'passed': 1, 'failed': 0, 'locked': 0}



## Exercise 1.9: Kepler's third law

You were selected to be the next astronaut to go to Mars. Congratulations! 

Kepler's third law expresses the relationship between the distance of planets from the Sun, $a$, and their orbital periods, $P$:

$$ P^2 = \frac{4\pi^2}{G(M + m)}a^3  $$

where
* $P$ is the period (in seconds);
* $G$ is the gravitational constant ($G = 6.67 \cdot 10^{-11} \,\text{m}^3\text{kg}^{-1}\text{s}^{-2}$);
* $M$ is the mass of the Sun ($M = 2 \cdot 10^{30} \text{kg}$);
* $m$ is the mass of the planet (in kg);
* $a$ is the distance between the planet and the Sun (in m).

How many Earth birthdays will you celebrate during your 10-years Mars mission? Write a Python function `period` that calculates the period of a planet. Using `period` function, calculate the period of the Earth, `P_earth`, and the period of Mars, `P_mars`. Finally, calculate `birthdays` which is how many Earth years are equivalent to 10 years on Mars.

We know that:
* The average distance between the Earth and the Sun is $a = 1.5 \cdot 10^{11} \,\text{m}$;
* The average distance between Mars and the Sun is 0.5 larger than the Earth-Sun distance;
* The mass of the Earth is $m_1 = 6 \cdot 10^{24} \,\text{kg}$;
* Mars's mass is about 10% of the Earth's mass.

**Hint**: You do not need to do any unit conversion. 


```python
# Uncomment and complete this code - keep the names the same for testing purposes.

from math import pi, sqrt

def period(a, m_planet, m_sun=2e30, G=6.67e-11):
    p = ((4* (pi**2)) / (G*(m_sun+m_planet))) * (a**3)
    return sqrt(p)

P_mars = period(2.25e11, 0.6e24, 2e30, 6.67e-11)

P_earth = period(1.5e11,6e24, 2e30, 6.67e-11)

birthdays = 10*P_mars/ P_earth
```


```python
with pybryt.check(pybryt_reference(1, 9)):
    period(a=1e11, m_planet=1e24), P_mars, P_earth, birthdays
```

    REFERENCE: exercise-1_9
    SATISFIED: True
    MESSAGES:
      - SUCCESS: Your function computes the period correctly.
      - SUCCESS: You computed the Earth's period correctly.
      - SUCCESS: You computed Mars's period correctly.
      - SUCCESS: Wow! Your computed birthdays value is correct!



```python
ok.grade('exercise-1_9')
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Running tests
    
    ---------------------------------------------------------------------
    Test summary
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed






    {'passed': 1, 'failed': 0, 'locked': 0}



## Boolean expressions

An expression with value `True` or `False` is called a boolean expression. Example expressions for what you would write mathematically as
$C = 40$, $C \ne 40$, $C \ge 40$, $C \gt 40$ and $C \lt 40$ are:

```python
C == 40  # Note: the double == checks for equality!
C != 40  # This could also be written as 'not C == 4'
C >= 40
C > 40
C < 40
```

Let us now test some boolean expressions:


```python
C = 41

print("C != 40: ", C != 40)
print("C < 40: ", C < 40)
print("C == 41: ", C == 41)
```

    C != 40:  True
    C < 40:  False
    C == 41:  True


Several conditions can be combined with keywords `and` and `or` into a single boolean expression:

* **Rule 1**: (`C1 and C2`) is `True` only if both `C1` and `C2` are `True`.
* **Rule 2**: (`C1 or C2`) is `True` if either `C1` or `C2` are `True`.

Examples:


```python
x = 0
y = 1.2

print('x >= 0 and y < 1:', x >= 0 and y < 1)
print('x >= 0 or y < 1:', x >= 0 or y < 1)
```

    x >= 0 and y < 1: False
    x >= 0 or y < 1: True


## Exercise 1.10: Values of boolean expressions
Add a comment to the code below to explain the outcome of each of the boolean expressions:


```python
C = 41

print("Case 1: ", C == 40)  # False because C is not equal to 40
print("Case 2: ", C != 40 and C < 41)  # ...
print("Case 3: ", C != 40 or C < 41)  # ...
print("Case 4: ", not C == 40)
print("Case 5: ", not C > 40)
print("Case 6: ", C <= 41)
print("Case 7: ", not False)
print("Case 8: ", True and False)
print("Case 9: ", False or True)
print("Case 10: ", False or False or False)
print("Case 11: ", True and True and False)
print("Case 12: ", (True and True) or 1 == 2)
```

    Case 1:  False
    Case 2:  False
    Case 3:  True
    Case 4:  True
    Case 5:  False
    Case 6:  True
    Case 7:  True
    Case 8:  False
    Case 9:  True
    Case 10:  False
    Case 11:  False
    Case 12:  True


## Loops
Suppose we want to make the following table of Celsius and Fahrenheit degrees:
```
 -20  -4.0
 -15   5.0
 -10  14.0
  -5  23.0
   0  32.0
   5  41.0
  10  50.0
  15  59.0
  20  68.0
  25  77.0
  30  86.0
  35  95.0
  40 104.0
```

How do we write a program that prints out such a table? We know that $F = \frac{9}{5}C + 32$, and a single line in this table is:


```python
C = -20
F = 9/5*C + 32

print(C, F)
```

    -20 -4.0


Now, we can just repeat these statements:


```python
C = -20; F = 9/5*C + 32; print(C, F)
C = -15; F = 9/5*C + 32; print(C, F)
C = -10; F = 9/5*C + 32; print(C, F)
C = -5; F = 9/5*C + 32; print(C, F)
C = 0; F = 9/5*C + 32; print(C, F)
C = 5; F = 9/5*C + 32; print(C, F)
C = 10; F = 9/5*C + 32; print(C, F)
C = 15; F = 9/5*C + 32; print(C, F)
C = 20; F = 9/5*C + 32; print(C, F)
C = 25; F = 9/5*C + 32; print(C, F)
C = 30; F = 9/5*C + 32; print(C, F)
C = 35; F = 9/5*C + 32; print(C, F)
C = 40; F = 9/5*C + 32; print(C, F)
```

    -20 -4.0
    -15 5.0
    -10 14.0
    -5 23.0
    0 32.0
    5 41.0
    10 50.0
    15 59.0
    20 68.0
    25 77.0
    30 86.0
    35 95.0
    40 104.0


We can see that works but it is **very boring** to write and very easy to introduce a misprint.

**You really should not be doing boring repetitive tasks like this.** Spend your time instead looking for a smarter solution. When programming becomes boring, there is usually a construct that automates the writing. Computers are very good at performing repetitive tasks. For this purpose we use **loops**.

## The while loop (and the significance of indentation)

A `while` loop executes repeatedly a set of statements as long as a **boolean condition** is `True`

```python
while condition:
    <statement 1>
    <statement 2>
    ...

<first statement after the loop>
```

Note that all statements to be executed within the loop must be indented by the same amount! The loop ends when an unindented statement is encountered.

In Python, indentations are very important. For instance, when writing a `while` loop:


```python
counter = 0
while counter <= 10:
    counter = counter + 1

print(counter)
```

    11


Let us take a look at what happens when we forget to indent correctly:

```python
counter = 0
while counter <= 10:
counter = counter + 1
print(counter)


  File "<ipython-input-86-d8461f52562c>", line 3
    counter = counter + 1
    ^
IndentationError: expected an indented block
```

Let us now use the `while` loop to create the table above:


```python
C = -20                 # Initialise C
dC = 5                  # Increment for C within the loop
while C <= 40:          # Loop heading with condition (C <= 40)
    F = (9/5)*C + 32  # 1st statement inside loop
    print(C, F)         # 2nd statement inside loop
    C = C + dC          # Increment C for the next iteration of the loop.
```

    -20 -4.0
    -15 5.0
    -10 14.0
    -5 23.0
    0 32.0
    5 41.0
    10 50.0
    15 59.0
    20 68.0
    25 77.0
    30 86.0
    35 95.0
    40 104.0


## Exercise 1.11: Compute the number of digits in a positive integer $a$

Write a Python function `num_digits(a)` that uses a `while` loop to compute how many decimal digits we need to write a positive integer $a$. For instance, we need 2 digits to write 73, whereas we need 5 digits to write 12345.


```python
# Uncomment and complete the code below. Do not change the names of variables!

def num_digits(a):
    count = 0
    while a != 0:
        a //= 10
        count += 1
    return count

```


```python
with pybryt.check(pybryt_reference(1, 11)):
     num_digits(55)
```

    REFERENCE: exercise-1_11
    SATISFIED: False
    MESSAGES:
      - ERROR: Hmmm... Think about dividing the number by 10 in each iteration.
      - ERROR: You should increment the number of digits in each iteration.
      - ERROR: Your function does not compute the number of digits correctly.



```python
ok.grade('exercise-1_11')
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Running tests
    
    ---------------------------------------------------------------------
    Test summary
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed






    {'passed': 1, 'failed': 0, 'locked': 0}



## Exercise 1.12: Write an approximate Fahrenheit-Celsius conversion table

Instead of using an exact formula for converting Fahrenheit ($F$) to Celsius ($C$) degrees:

$$C = \frac{5}{9}(F - 32),$$

many people use an approximate formula for quicker conversion:

$$C \approx \hat{C} = \frac{F − 30}{2}.$$

Write a Python function `conversion_table` using a `while` loop that prints the conversion table consisting of three columns: $F$, $C$, and the approximate value $\hat{C}$, for $F = 0, 10, 20, \ldots, 100$. Besides, using the same while loop, count the number of rows printed and return the count. Ensure that all numbers in the conversion table are printed with two decimal places.


```python
# Uncomment and complete the code below. Do not change the names of variables.

def conversion_table():
    F = 0
    rows = 0
    while F<=100:
        C = (5*(F-32))/9
        approximate_C = (F-30)/2
        print(f'{F:.2f}',f'{C:.2f}',f'{approximate_C:.2f}')
        F += 10
        rows +=1
    return rows
```


```python
with pybryt.check(pybryt_reference(1, 12)):
    conversion_table()
```

    0.00 -17.78 -15.00
    10.00 -12.22 -10.00
    20.00 -6.67 -5.00
    30.00 -1.11 0.00
    40.00 4.44 5.00
    50.00 10.00 10.00
    60.00 15.56 15.00
    70.00 21.11 20.00
    80.00 26.67 25.00
    90.00 32.22 30.00
    100.00 37.78 35.00
    REFERENCE: exercise-1_12
    SATISFIED: False
    MESSAGES:
      - ERROR: Hmmm... Think about increasing F by 10 in each iteration.
      - SUCCESS: Your computation of C is correct. Well done!
      - SUCCESS: Your computation of approximate C is correct.
      - SUCCESS: You are incrementing the number of rows in each iteration. Great!
      - SUCCESS: Wow! Your function returns the correct number of rows.



```python
ok.grade('exercise-1_12')
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Running tests
    
    ---------------------------------------------------------------------
    Test summary
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed






    {'passed': 1, 'failed': 0, 'locked': 0}



## Lists
So far, one variable has referred to one number (or string). Sometimes, however, we naturally have a collection of numbers, e.g. degrees −20, −15, −10, −5, 0, ..., 40. One way to store these values in a computer program would be to have one variable per value:


```python
C1 = -20
C2 = -15
C3 = -10
# ...
C13 = 40
```

This is clearly a terrible solution, particularly if we have lots of values. A better way of doing this is to collect values together in a list:


```python
C = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
```

Now, there is just one variable, `C`, holding all the values. We access elements in a list via an index. List indices are always *zero-indexed*, i.e. they are numbered as 0, 1, 2, and so forth up to the number of elements minus one:


```python
mylist = [4, 6, -3.5]
print('First element:', mylist[0])
print('Second element:', mylist[1])
print('Third element:', mylist[2])
```

    First element: 4
    Second element: 6
    Third element: -3.5


Here are a few examples of operations that you can perform on lists:


```python
C = [-10, -5, 0, 5, 10, 15, 20, 25, 30]
C.append(35)  # add new element 35 at the end
print(C)
```

    [-10, -5, 0, 5, 10, 15, 20, 25, 30, 35]



```python
C = C + [40, 45]  # And another list to the end of C
print(C)
```

    [-10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45]



```python
C.insert(0, -15)  # Insert -15 as index 0
print(C)
```

    [-15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45]



```python
del C[2]  # delete 3rd element
print(C)
```

    [-15, -10, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45]



```python
del C[2]  # delete what is now 3rd element
print(C)
```

    [-15, -10, 5, 10, 15, 20, 25, 30, 35, 40, 45]



```python
print(len(C))  # length of list
```

    11



```python
print(C.index(10))  # Find the index of the element with the value 10
```

    3



```python
print(10 in C)  # True only if the value 10 is stored in the list
```

    True



```python
print(C[-1])  # The last value in the list
```

    45



```python
print(C[-2])  # The second last value in the list
```

    40


We can also extract sublists using `:`:


```python
print(C[5:])  # From index 5 to the end of the list
```

    [20, 25, 30, 35, 40, 45]



```python
print(C[5:7])  # From index 5 up to, but NOT including index 7
```

    [20, 25]



```python
print(C[7:-1])  # From index 7 up to the second last element
```

    [30, 35, 40]



```python
print(C[:])  # [:] specifies the whole list.
```

    [-15, -10, 5, 10, 15, 20, 25, 30, 35, 40, 45]


We can also *unpack* the elements of a list into separate variables:


```python
somelist = ['Curly', 'Larry', 'Moe']
stooge1, stooge2, stooge3 = somelist
print(f'stooge1: {stooge1}, stooge2: {stooge2}, stooge3: {stooge3}')
```

    stooge1: Curly, stooge2: Larry, stooge3: Moe


## Exercise 1.13: Store odd numbers in a list

Write a Python function `odd_numbers(n)` that uses a `while` loop, and generates and returns a list of all odd numbers from $1$ to $n$. (Make sure that if $n$ is an even number, the largest generated odd number is $n-1$.)


```python
# Uncomment and complete code. Do not change the variable names.

def odd_numbers(n):
    res = []
    i = 1
    while i < n:
        res.append(i)
        i+=2
    return res

```


```python
with pybryt.check(pybryt_reference(1, 13)):
    print(odd_numbers(50))
```

    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
    REFERENCE: exercise-1_13
    SATISFIED: False
    MESSAGES:
      - ERROR: Hmmm... you are not appending an odd number to the list in each iteration.
      - ERROR: It looks like you are not increasing the number by 2 in each iteration.
      - SUCCESS: Before the loop, you begin with an empty list. Well done!
      - SUCCESS: Before the loop, you start with 1.
      - SUCCESS: Your function returns the correct solution.



```python
ok.grade('exercise-1_13')
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Running tests
    
    ---------------------------------------------------------------------
    Test summary
        Passed: 2
        Failed: 0
    [ooooooooook] 100.0% passed






    {'passed': 2, 'failed': 0, 'locked': 0}



## For loops
We can visit each element in a list and process it with some statements using a `for` loop, for example:


```python
degrees = [0, 10, 20, 40, 100]
for C in degrees:
    print('list element:', C)
print(f'The list has {len(degrees)} elements.')
```

    list element: 0
    list element: 10
    list element: 20
    list element: 40
    list element: 100
    The list has 5 elements.


Notice again how the statements to be executed within the loop must be indented! Let us now revisit the conversion table example using the `for` loop:


```python
Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
for C in Cdegrees:
    F = (9/5)*C + 32
    print(C, F)
```

    -20 -4.0
    -15 5.0
    -10 14.0
    -5 23.0
    0 32.0
    5 41.0
    10 50.0
    15 59.0
    20 68.0
    25 77.0
    30 86.0
    35 95.0
    40 104.0


We can easily beautify the table using the *printf syntax* we encountered previously:


```python
for C in Cdegrees:
    F = (9.0/5)*C + 32
    print('%5d %5.1f' % (C, F))
```

      -20  -4.0
      -15   5.0
      -10  14.0
       -5  23.0
        0  32.0
        5  41.0
       10  50.0
       15  59.0
       20  68.0
       25  77.0
       30  86.0
       35  95.0
       40 104.0


It is also possible to rewrite the `for` loop as a `while` loop, i.e.

```python
for element in somelist:
    # process element
```

can always be transformed to a `while` loop
```python
index = 0
while index < len(somelist):
    element = somelist[index]
    # process element
    index += 1
```

Let us see how a previous example would look like if we used `while` instead of `for` loop:


```python
Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
index = 0
while index < len(Cdegrees):
    C = Cdegrees[index]
    F = (9.0/5)*C + 32
    print('%5d %5.1f' % (C, F))
    index += 1
```

      -20  -4.0
      -15   5.0
      -10  14.0
       -5  23.0
        0  32.0
        5  41.0
       10  50.0
       15  59.0
       20  68.0
       25  77.0
       30  86.0
       35  95.0
       40 104.0


Rather than just printing out the Fahrenheit values, let us also store these computed values in a list of their own:


```python
Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
Fdegrees = []  # start with empty list
for C in Cdegrees:
    F = (9/5)*C + 32
    Fdegrees.append(F)  # add new element to Fdegrees
print(Fdegrees)
```

    [-4.0, 5.0, 14.0, 23.0, 32.0, 41.0, 50.0, 59.0, 68.0, 77.0, 86.0, 95.0, 104.0]


In Python, `for` loops usually loop over list values (elements), i.e.

```python
for element in somelist:
    # process variable element
```

However, we can also loop over list indices:

```python
for i in range(0, len(somelist), 1):
    element = somelist[i]
    # process element or somelist[i] directly
```

The statement `range(start, stop, increment)` generates a list of integers *start*, *start+increment*, *start+2\*increment*, and so on up to, but not including, *stop*. We can also write `range(stop)` as an abbreviation for `range(0, stop, 1)`:


```python
for i in range(3):  # same as range(0, 3, 1)
    print(i)
```

    0
    1
    2



```python
for i in range(2, 8, 3):
    print(i)
```

    2
    5


## List comprehensions
Consider this example where we compute two lists in a `for` loop:


```python
n = 16

# empty lists
Cdegrees = []
Fdegrees = []

for i in range(n):
    Cdegrees.append(-5 + i*0.5)
    Fdegrees.append((9/5)*Cdegrees[i] + 32)

print("Cdegrees = ", Cdegrees)
print("Fdegrees = ", Fdegrees)
```

    Cdegrees =  [-5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5]
    Fdegrees =  [23.0, 23.9, 24.8, 25.7, 26.6, 27.5, 28.4, 29.3, 30.2, 31.1, 32.0, 32.9, 33.8, 34.7, 35.6, 36.5]


As constructing lists is a very common task, the above way of doing it can become very tedious both to write and read. Therefore, Python has a compact construct, called *list comprehension* for generating lists from a `for` loop:


```python
n = 16
Cdegrees = [-5 + i*0.5 for i in range(n)]
Fdegrees = [(9/5)*C + 32 for C in Cdegrees]
print("Cdegrees = ", Cdegrees)
print("Fdegrees = ", Fdegrees)
```

    Cdegrees =  [-5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5]
    Fdegrees =  [23.0, 23.9, 24.8, 25.7, 26.6, 27.5, 28.4, 29.3, 30.2, 31.1, 32.0, 32.9, 33.8, 34.7, 35.6, 36.5]


The general form of a list comprehension is:
```python
somelist = [expression for element in somelist]
```

## Exercise 1.14: Create a list of even numbers ranging from 0 to $n$ using a `for` loop.

Write a function `even_numbers(n)` using a `for` loop, which generates and returns a list of all even numbers from 0 to $n$. For instance, `even_numbers(10)` should return list `[0, 2, 4, 6, 8]`. In this exercise, do not use list comprehensions.


```python
# Uncomment and complete code. Do not change the variable names.

def even_numbers(n):
    res = []
    for i in range(0,n+1):
        if i % 2 == 0:
            res.append(i)
    return res
```


```python
with pybryt.check(pybryt_reference(1, 14)):
    even_numbers(11)
```

    REFERENCE: exercise-1_14
    SATISFIED: False
    MESSAGES:
      - ERROR: Hmmm... you are not appending an even number to the list in each iteration.
      - SUCCESS: You are iterating over the correct list.
      - SUCCESS: Before the loop, you begin with an empty list. Well done!
      - SUCCESS: Your function returns the correct solution.



```python
ok.grade('exercise-1_14')
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Running tests
    
    ---------------------------------------------------------------------
    Test summary
        Passed: 2
        Failed: 0
    [ooooooooook] 100.0% passed






    {'passed': 2, 'failed': 0, 'locked': 0}



## Exercise 1.15: Implement the sum function

The built-in Python function [sum](https://docs.python.org/3/library/functions.html#sum) takes a list as an argument and computes the sum of the elements in the list:
```python
>> sum([1,3,5,-5])
4
```
Implement your own version of the sum function and name it `my_sum`.


```python
# Uncomment and complete this code - keep the names the same for testing purposes.
# from functools import reduce

# def my_sum(x):
#     res = reduce(lambda x,y: x+y, x)
#     return 

def my_sum(x):
    sum = 0
    for item in x:
        sum+= item
    return sum
```


```python
with pybryt.check(pybryt_reference(1, 15)):
    my_sum([2.1, 98, -451, 273, 1111, 23.98])
```

    REFERENCE: exercise-1_15
    SATISFIED: True
    MESSAGES:
      - SUCCESS: Great! In each iteration, you are adding a list element to the sum variable.
      - SUCCESS: You are iterating over the list elements instead over indices.
      - SUCCESS: Before the loop, you set the sum to be zero. Well done!
      - SUCCESS: Your function returns the correct solution.



```python
ok.grade('exercise-1_15')
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Running tests
    
    ---------------------------------------------------------------------
    Test summary
        Passed: 3
        Failed: 0
    [ooooooooook] 100.0% passed






    {'passed': 3, 'failed': 0, 'locked': 0}



## Exercise 1.16: Position of the ball in a vertical motion.

Write a function `distance` that returns a `list` of $y$ values calculated using the formula:

$$y(t) = v_0t − {1\over2} gt^2,$$

for `n` number of values $t$ ranging from `t_start` to `t_end`. Specify the keyword arguments `v0=6.0` and `g=9.81`.


```python
# Uncomment and complete this code - keep the names the same for testing purposes.

import numpy as np
def distance(t_start, t_end, n, v0=6.0, g=9.81):
    res = []
    step = (t_start+t_end)/(n+1)
    t_range = [num for num in np.arange(t_start,t_end+t_start,step)]
    for i in t_range:
        res.append(v0*i - (1/2)*g*(i**2))
    return res
```


```python
with pybryt.check(pybryt_reference(1, 16)):
    distance(0.1,0.6,6)
```

    REFERENCE: exercise-1_16
    SATISFIED: False
    MESSAGES:
      - ERROR: Hmmm... You are not iterating over the correct values of t.
      - ERROR: You are not appending the positions to a list.
      - SUCCESS: Before the loop, you start with an empty list. Amazing!
      - ERROR: Your time step value is wrong.
      - ERROR: Your function returns a wrong solution.



```python
ok.grade('exercise-1_16')
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Running tests
    
    ---------------------------------------------------------------------
    question 1.16 > Suite 2 > Case 2
    
    import numpy as np
    >>> np.allclose(distance(1, 6, 5, 3), [-1.9050000000000002, -18.0815625, -49.58625, -96.41906250000001, -158.58])
    Traceback (most recent call last):
      File "<__array_function__ internals>", line 5, in allclose
      File "/opt/jupyter/lib/python3.8/site-packages/numpy/core/numeric.py", line 2249, in allclose
        res = all(isclose(a, b, rtol=rtol, atol=atol, equal_nan=equal_nan))
      File "<__array_function__ internals>", line 5, in isclose
      File "/opt/jupyter/lib/python3.8/site-packages/numpy/core/numeric.py", line 2358, in isclose
        return within_tol(x, y, atol, rtol)
      File "/opt/jupyter/lib/python3.8/site-packages/numpy/core/numeric.py", line 2339, in within_tol
        return less_equal(abs(x-y), atol + rtol * abs(y))
    ValueError: operands could not be broadcast together with shapes (6,) (5,) 
    
    # Error: expected
    #     True
    # but got
    #     Traceback (most recent call last):
    #       ...
    #     ValueError: operands could not be broadcast together with shapes (6,) (5,) 
    
    Run only this test case with "python3 ok -q exercise-1_16 --suite 2 --case 2"
    ---------------------------------------------------------------------
    Test summary
        Passed: 2
        Failed: 1
    [ooooook....] 66.7% passed






    {'passed': 2, 'failed': 1, 'locked': 0}



## Exercise 1.17: Cumulative sum

Write a function that returns the cumulative sum of the numbers in a list. The function should return a list, whose `i`-th element is the sum of the input list up to and including the `i`-th element.

For example, for the list `[1, 4, 2, 5, 3]` should return `[1, 5, 7, 12, 15]`.


```python
# Uncomment and complete this code - keep the names the same for testing purposes.

def my_cumsum(x):
    res= []
    res.append(x[0])
    for i in range(1,len(x)):
        res.append(x [i]+ res[i-1])
    return res
    
```


```python
with pybryt.check(pybryt_reference(1, 17)):
    print(my_cumsum([55, 111, -33, 65]))
```

    [55, 166, 133, 198]
    REFERENCE: exercise-1_17
    SATISFIED: True
    MESSAGES:
      - SUCCESS: You are appending the correct cumulative sum to a list. Well done!
      - SUCCESS: Before the loop, you start with an empty list. Amazing!
      - SUCCESS: Wow! Your function returns the correct solution.



```python
ok.grade('exercise-1_17')
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Running tests
    
    ---------------------------------------------------------------------
    Test summary
        Passed: 2
        Failed: 0
    [ooooooooook] 100.0% passed






    {'passed': 2, 'failed': 0, 'locked': 0}



## Exercise 1.18: Bouncing ball

A rubber ball is dropped from a height `h_0`. After each bounce, the height it rebounds to decreases by 10%, i.e. after one bounce, it reaches `0.9*h_0`, after two bounces it reaches `0.9*0.9*h_0`, etc. Write a Python function `compute_heights` that returns a list of the maximum heights of the ball after each bounce (including after 0 bounces, i.e. its initial height), until either the ball has bounced `n` times *or* its maximum height falls below `h1`. The function should take `h_0`, `h_1` and `n` as keyword arguments, with default values of `1.0`, `0.3` and `10`, respectively.

**HINT:** If `n` bounces of the ball are not reached, the last value of height in the list should be the first height at which the ball fell below `h1`. More precisely, the last value is less than `h1`.


```python
# Uncomment and complete this code - keep the names the same for testing purposes.

def compute_heights(h_0=1.0, h_1=0.3, n=10):
    res = []
    res.append(h_0)
    times = 0
    while times < n and h_0 >= h_1:
        h_0 *= 0.9
        res.append(h_0)
        times += 1
    return res
    
```


```python
with pybryt.check(pybryt_reference(1, 18)):
    compute_heights(h_0=1.0, h_1=0.3, n=10)
```

    REFERENCE: exercise-1_18
    SATISFIED: False
    MESSAGES:
      - SUCCESS: You are appending the correct height to a list. Well done!
      - ERROR: You are not counting the bounces correctly.
      - SUCCESS: Before the loop, you start with an empty list. Amazing!
      - SUCCESS: Before the loop, you set the ounter to zero. Great!
      - SUCCESS: Wow! Your function returns the correct solution.



```python
ok.grade('exercise-1_18')
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Running tests
    
    ---------------------------------------------------------------------
    Test summary
        Passed: 4
        Failed: 0
    [ooooooooook] 100.0% passed






    {'passed': 4, 'failed': 0, 'locked': 0}



## Exercise 1.19: Calculate $\pi$

A formula for $\pi$ is given by the *Gregory-Leibniz series*:

$$\pi = 4 \left(\frac{1}{1} - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} + ...  \right)$$

Note that the denominators of the terms in this series are the positive odd numbers. Write a Python function `calculate_pi(n)` following the guidelines below; each of the first three steps can be completed using a single list comprehension.

**Step 1**:

Produce a list of the first `n` odd numbers, for `n=100`.

**Step 2**:

Make a list of the signs of each term, i.e. `[1, -1, 1, -1, ...]`. Hint: think about the value of $(-1)^i$ for integer $i$.

**Step 3**:

Using the results of steps 1 and 2, make a list of the first `n` terms in the above series.

**Step 4**:

Use your `my_sum` function to sum this series, multiply by 4, and return the result.


```python
# Uncomment and complete this code - keep the names the same for testing purposes.

def calculate_pi(n):
    odd_list = [2*num+1 for num in range(0,n)]
    sign_list = [((-1)**i) for i in range(0,n)]
    sum = 0
    for i in range(0,len(odd_list)):
        sum += sign_list[i]*(1/odd_list[i])
    return 4 * sum
    
```


```python
with pybryt.check(pybryt_reference(1, 19)):
    calculate_pi(100)
```

    REFERENCE: exercise-1_19
    SATISFIED: True
    MESSAGES:
      - SUCCESS: You generated odd integers correctly. Amazing!
      - SUCCESS: You generated the signs list correctly. Well done!
      - SUCCESS: Great! You computed series terms correctly.
      - SUCCESS: Wow! Your function returns the correct solution.



```python
ok.grade('exercise-1_19')
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Running tests
    
    ---------------------------------------------------------------------
    Test summary
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed






    {'passed': 1, 'failed': 0, 'locked': 0}




```python
ok.score()
```

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Scoring tests
    
    ---------------------------------------------------------------------
    question 1.2
        Passed: 3
        Failed: 0
    [ooooooooook] 100.0% passed
    
    ---------------------------------------------------------------------
    question 1.3
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed
    
    ---------------------------------------------------------------------
    question 1.4
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed
    
    ---------------------------------------------------------------------
    question 1.5
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed
    
    ---------------------------------------------------------------------
    question 1.5
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed
    
    ---------------------------------------------------------------------
    question 1.7 > Suite 3 > Case 1
    
    import numpy as np
    >>> np.allclose(gaussian(0.5), 0.3520653267642995)
    Traceback (most recent call last):
      File "<__array_function__ internals>", line 5, in allclose
      File "/opt/jupyter/lib/python3.8/site-packages/numpy/core/numeric.py", line 2249, in allclose
        res = all(isclose(a, b, rtol=rtol, atol=atol, equal_nan=equal_nan))
      File "<__array_function__ internals>", line 5, in isclose
      File "/opt/jupyter/lib/python3.8/site-packages/numpy/core/numeric.py", line 2355, in isclose
        xfin = isfinite(x)
    TypeError: ufunc 'isfinite' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
    
    # Error: expected
    #     True
    # but got
    #     Traceback (most recent call last):
    #       ...
    #     TypeError: ufunc 'isfinite' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
    
    Run only this test case with "python3 ok -q exercise-1_7 --suite 3 --case 1"
    ---------------------------------------------------------------------
    question 1.7
        Passed: 1
        Failed: 1
    [oooook.....] 50.0% passed
    
    ---------------------------------------------------------------------
    question 1.8
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed
    
    ---------------------------------------------------------------------
    question 1.9
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed
    
    ---------------------------------------------------------------------
    question 1.11
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed
    
    ---------------------------------------------------------------------
    question 1.12
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed
    
    ---------------------------------------------------------------------
    question 1.13
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed
    
    ---------------------------------------------------------------------
    question 1.14
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed
    
    ---------------------------------------------------------------------
    question 1.15
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed
    
    ---------------------------------------------------------------------
    question 1.16 > Suite 2 > Case 2
    
    import numpy as np
    >>> np.allclose(distance(1, 6, 5, 3), [-1.9050000000000002, -18.0815625, -49.58625, -96.41906250000001, -158.58])
    Traceback (most recent call last):
      File "<__array_function__ internals>", line 5, in allclose
      File "/opt/jupyter/lib/python3.8/site-packages/numpy/core/numeric.py", line 2249, in allclose
        res = all(isclose(a, b, rtol=rtol, atol=atol, equal_nan=equal_nan))
      File "<__array_function__ internals>", line 5, in isclose
      File "/opt/jupyter/lib/python3.8/site-packages/numpy/core/numeric.py", line 2358, in isclose
        return within_tol(x, y, atol, rtol)
      File "/opt/jupyter/lib/python3.8/site-packages/numpy/core/numeric.py", line 2339, in within_tol
        return less_equal(abs(x-y), atol + rtol * abs(y))
    ValueError: operands could not be broadcast together with shapes (6,) (5,) 
    
    # Error: expected
    #     True
    # but got
    #     Traceback (most recent call last):
    #       ...
    #     ValueError: operands could not be broadcast together with shapes (6,) (5,) 
    
    Run only this test case with "python3 ok -q exercise-1_16 --suite 2 --case 2"
    ---------------------------------------------------------------------
    question 1.16
        Passed: 1
        Failed: 1
    [oooook.....] 50.0% passed
    
    ---------------------------------------------------------------------
    question 1.17
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed
    
    ---------------------------------------------------------------------
    question 1.18
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed
    
    ---------------------------------------------------------------------
    question 1.19
        Passed: 1
        Failed: 0
    [ooooooooook] 100.0% passed
    
    ---------------------------------------------------------------------
    Point breakdown
        question 1.2: 1.0/1
        question 1.3: 1.0/1
        question 1.4: 1.0/1
        question 1.5: 1.0/1
        question 1.7: 0.5/1
        question 1.8: 1.0/1
        question 1.9: 1.0/1
        question 1.11: 1.0/1
        question 1.12: 1.0/1
        question 1.13: 1.0/1
        question 1.14: 1.0/1
        question 1.15: 1.0/1
        question 1.16: 0.5/1
        question 1.17: 1.0/1
        question 1.18: 1.0/1
        question 1.19: 1.0/1
    
    Score:
        Total: 15.0






    {'Total': 15.0}




```python

```
