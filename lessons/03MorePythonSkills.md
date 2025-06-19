
# Lesson 3 — More Python Skills

## Lesson Overview
**Learning objective:** In this lesson, students will learn and apply key advanced Python concepts including object-oriented programming, decorators, list comprehensions, and closures. They will learn how to write cleaner, more modular code using these features, and gain insight into how such patterns are used in real-world frameworks like Dash.

### Topics
1. Object-oriented programming (OOP)
2. Decorators
3. List comprehensions
4. Closures
---

## 10.1 Object-oriented programming in Python
Everything in Python is an object, and objects are instances of *classes*. That means when you create a variable like a string, list, or even a function — you’re actually creating an object. Before finishing Python 100, it's worth understanding what this actually means.  

Until now we have been following principles of *functional programming*: writing standalone functions that take in inputs, return outputs, and typically don't remember anything between calls. But sometimes we want to bundle together data and the functions -- called *methods* -- that operate on that data. This is the core idea of object-oriented programming (OOP). This bundling is called *encapsulation*, and helps keep related code organized in one place. If you are creating a new data type, OOP lets you define not only what that data type is, but what you can do with it. 

> If you want to go a little deeper, there is a nice overview of OOP at [Real Python](https://realpython.com/python3-object-oriented-programming/). 

### Basic class definition
Let’s look at a very simple example — a class that represents dogs:

```Python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call_dog(self):
        print(f"Come here, {self.name}!")

    def speak(self):
        print("bark bark bark")

dog1 = Dog("Spot", 2)
dog1.call_dog()
dog1.speak()
print(f"dog1's name is {dog1.name}.")

dog2 = Dog("Wally", 4)
dog2.call_dog()
dog2.age += 1
print(dog2.age)
```

In the above, we have:
- The declaration of a class named `Dog`.  Unlike functions, class names are capitalized in Python.
- An initialization method `__init__()` that runs automatically when you create a new dog. Here, the method is used to set the initial values of the object's attributes (`name` and `age`). 
- You can access an object's attributes using *dot notation*: this includes both instance variables and methods.
- The object's instance variables `self.name` and `self.age` store data for each instance of the class.
- The two methods, `call_dog()` and `speak()` are always passed the value  `self`, which gives them access to attributes like `name` or `age`. 
- Notice that we were able to modify `dog2`'s age -- there is nothing truly private about the data stored in an object's attributes. We will say more about this below. 

#### What is `self`?
Within a class definition, `self` refers to the current instance of the class — the specific object the method is being called on. It can be a little confusing because when *defining* a method it is always the first parameter, but you don’t actually pass it in as a parameter when invoking the method; Python does that automatically behind the scenes. For instance, above we have `dog1.call_dog()`, which doesn't include the `self` argument explicitly. 

### Expanding the class: class attributes and class methods
We can add more bells and whistles to our simple Dog class. For example, suppose we want to count how many dogs have been created. Instead of storing that information in each individual dog, we can store it once at the class level:

```Python
class Dog:
    _count = 0  

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog._count += 1 

    def call_dog(self):
        print(f"Come here, {self.name}!")

    def speak(self):
        print("bark bark bark")

    @classmethod
    def get_dog_count(cls):
        return cls._count

# Create a couple of dogs
dog1 = Dog("Spot", 2)
dog1.call_dog()
dog1.speak()
print(f"dog1's name is {dog1.name}.")

dog2 = Dog("Wally", 4)
dog2.call_dog()
dog2.age += 1
print(f"dog2's new age: {dog2.age}")

print(f"Total dogs created: {Dog.get_dog_count()}")  
```
There are quite a few new things going on here:
- The variable `_count` is a *class variable*. Unlike the instance variables like `name` and `age`, it belongs to the class itself — not any individual dog. This means it is shared across all `Dog` objects. You can tell it is a class variables because it is defined outside the `__init__()` method.
- The `_count` variable starts with a single underscore to signal that it’s intended for internal use. This is a common Python convention: it doesn’t make the variable truly private (it is still accessible), but it tells developers that it isn't meant to be directly accessed and modified. 
- The method `get_dog_count()` is a *class method*, declared using the `@classmethod` decorator (we will talk more about decorators below). This tells Python that the method operates on the `Dog` class rather than individual objects.
- Instead of taking `self` as the first parameter,  `get_dog_count()` takes in `cls` (short for *class*). `cls` allows us to access the class-level variable `_count`.

### Class inheritance
Suppose you want to create a class that’s similar to `Dog`, but with a few differences — maybe a bigger bark, or a new behavior like fetching. Instead of rewriting everything from scratch, Python (and OOP in general) lets you *inherit* from an existing class and customize only the parts you want. This is called *class inheritance*.

Here's an example where we create a class `BigDog` that explicitly inherits from `Dog`:

```Python
class BigDog(Dog): # inherits from Dog
    def __init__(self, name, age): 
        # Call the parent class's __init__ to set name/age
        super().__init__(name, age) 

    def fetch(self):
        print("Got it.")

    def speak(self):
        print("Woof Woof Woof") # overrides Dog.speak()

    def speak_verbose(self):
        # call Dog.speak(), then BigDog.speak()
        super().speak()
        self.speak()

dog3 = BigDog("Butch", 3)
dog3.call_dog()
dog3.speak()
dog3.speak_verbose()
```

Here, the `BigDog` class inherits from the `Dog` class, meaning it gets all of `Dog`’s methods and attributes unless explicitly changed:
- The `call_dog()` method is inherited from `Dog`, because we didn’t override it.
- The `speak()` method is overridden to make big dogs sound different.
- The `speak_verbose()` method shows how to call both the original `Dog.speak()` (using `super()`) and `BigDog.speak()`.

You might try creating a `ShyDog` class that overrides `speak()` to say nothing unless prompted by giving it a treat with a method `give_treat()`.

### A few other facts about classes
A useful attribute of every class and instance is `__dict__`.

```python
print(Dog.__dict__) # prints attributes and methods for the Dog class
print(dog1.__dict__) # prints the attributes of the instance and their values.
```

You can also create classes from system classes:

```Python
class Shout(str):
   def __new__(cls, content):
      return str.__new__(cls, content.upper())

x = Shout("hello there")
print(x) # prints HELLO THERE
```
In this case, the subclass overrides the `__new__` method of the `str` class, and not the `__init__` method, because strings are immutable. 

---

## 10.2: Introduction to Decorators
We’ve already seen some decorators like `@classmethod` in our class definitions. But what are these things? A decorator is syntactic sugar that says, “Take this function or class, and pass it through another function to modify it.” You will probably *use* decorators more than you write them in Python, so let's see them in action to see how useful they can be.   

#### Examples of decorators
Python provides lots of built-in decorators. We've already seen one:

```Python
@classmethod
def get_dog_count(cls):
```
This tells Python: “Don’t treat `get_dog_count()` like a normal method. Treat it as a method that applies to the class itself.” That’s all a decorator is doing: changing the behavior of a function or method, without you having to rewrite that function.

There are *many* useful built-in decorators. Sometimes, we want a method in a class to act like an attribute — it does a calculation, but we want to access it without parentheses:

```Python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

    @property
    def diameter(self):
        return 2 * self.radius
```

Now you can access those properties (area and diameter) as if they were attributes of the object, using dot notation: 

```Python
c = Circle(3)
print(c.area)    
print(c.diameter)  
```
Another nice feature is that while `area` and `diameter` are calculated using methods, if you change the `radius`, they will automatically repopulate with the correct values without you having to re-run those methods:

```Python
c.radios = 5
print(c.area)
```
You didn't have to re-assign anything: `area` (and `diamater`) are always recalculated based on the current radius. 

`@property` and `@classmethod` are built-in Python decorators -- Python itself provides this functionality. Below, we will discuss how to write your own decorators. 

So far we’ve seen decorators used with functions and methods, like `@property` and `@classmethod`. However, decorators can also be used with *classes*. One useful example is the built-in `@dataclass` decorator, which lets you quickly and conveniently define simple classes for storing structured data, without needing an `__init__` method.

```Python
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str

book1 = Book("Dune", "Frank Herbert")
book2 = Book("Dune", "Frank Herbert")
book3 = Book("Neuromancer", "William Gibson")

print(book1)
print(book2.title)          
print(book1 == book2) # True — same data, so considered equal
print(book1 == book3) # False — different data
```
There are a few things to notice about `dataclass` objects:
- You didn’t have to write an `__init__` method or any other methods for the class: Python did it for you behind the scenes. You just declare the attribute names and their data types.
- You can access the attributes of a book object using standard dot notation (`book2.title`). 
- You can check if two different books are the same with `book1 == book2` without having to define your own `__eq__()` operator.  

### Writing your own decorators
Python classifies functions as first-class objects, which means you can treat them just like any other variable or object. That is, you can pass them as arguments to other functions. For instance:

```Python
def say_hello():
    print("Hello!")

def repeat_me(func, num_repeats):
    for _ in range(num_repeats):
        func()

repeat_me(say_hello, 5)  # Will print "Hello!" 5x
```
This simple example demonstrates how you can pass around functions such as `say_hello()` and call them dynamically in your scripts. 

Decorators take advantage of this, and make such function application cleaner and easier to read. Let's look at a simple example, your first hand-made decorator: 

```python
def my_decorator(func):
    def wrapper():
        print ("Hello!")
        func()
        print ("World!")
    return wrapper

@my_decorator
def print_name():
    print("John")

print_name()
```

The output of `print_name()`, which is modified with the decorator, will be:
```
Hello!
John
World!
```
What's happening here?
- The decorator function `my_decorator()` takes a function (`func`) as input. 
- Inside this function, you define a new function called `wrapper()` that does three things: it prints "Hello!", calls the original function `func()` (which prints the name "John"), and then prints "World!". 
- The decorator returns the new `wrapper()` function that includes this extra behavior that is wrapped around `func()`. 
- When you add the `@my_decorator` above the `print_name()` function declaration, Python runs the following behind the scenes:

```Python
print_name = my_decorator(print_name)
```
Decorators let you add behavior to a function without modifying its original code. You didn’t have to touch `print_name()` -- you just wrapped it.

In this example the function is fairly trivial, however in the next section we can dig into some more useful examples. 

### Decorator that will work with any function

Here is an example of a decorator that allows us to benchmark different sections of code. We need to allow all functions to go into this decorator, and it will print out the time it took for a function to complete.
```python
import time

def timer(func):
    ## Output the time the inner function takes
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print (f"Finished in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def wait_half_second():
    time.sleep(0.5)
    return "Done"

wait_half_second()
```
This provides a useful way to wrap any function to see how long it takes to run (here we are wrapping a function that simply waits for a half second to demonstrate how the decorator works). 

In more detail:
- `@timer` decorates the function `wait_half_second`.
- Inside the wrapper, we:
  - Record the start time
  - Call the original function (`func(*args, **kwargs)`)
  - Record the end time and complute the elapsed time.
  - Print the elapsed time.
- Why did we use `*args` and `**kwargs`? Those let the decorator work with *any* function, no matter how many arguments it takes. `*args` captures positional arguments, while `**kwargs` captures keyword arguments. This flexibility makes the wrapper reusable for any function. Go ahead and try it for other functions.
  

### Decorator with arguments: decorator factories
Sometimes you want to pass *arguments* into a decorator — like how many times to repeat something, or what prefix to add to a message.  In this case, you need two levels of wrapping. This is because decorators are called with just one argument: the function being decorated. If you want to pass extra arguments, you need a *decorator factory* — a function that creates a customized decorator based on the parameters you provide. 

Let's look at an example where we allow users to specify how many times a message is repeated, and what prefix to add:

```Python
def repeat_with_prefix(prefix, num_repeats): # decorator factory
    def decorator(func):  # The decorator: takes the function
        def wrapper(*args, **kwargs):  # The wrapper: runs the function with extra behavior
            for _ in range(num_repeats):
                result = func(*args, **kwargs)  # Call the original function
                print(f"{prefix} {result}")
        return wrapper
    return decorator

@repeat_with_prefix(">>", 3)  
def greet(name):
    return f"Hello, {name}!"

greet("Amanda")
```
Breaking down the above. When you run `greet("Amanda")` you get:

```Python
>> Hello, Amanda!
>> Hello, Amanda!
>> Hello, Amanda!
```
Here's what happened behind the scenes:
- The decorator factory is called: `@repeat_with_prefix(">>", 3)` creates and returns a decorator function customized with the appropriate arguments.
- The decorator wraps the function: The `decorator` function (returned by the factory) is applied to `greet`.
- The wrapper runs the function: When you call `greet("Amanda")`,  the wrapper function uses the `prefix` and `num_repeats` provided by the factory to add the prefix to each output and print the result (`num_repeat` times)

Feel free to modify the code or the parameters (e.g., change ">>" to "**" or 3 to 5) to see how the decorator’s behavior changes. Parameterized decorators are a powerful but advanced concept, so take your time to experiment and build your intuition.

### Callback to Dash application
Decorators are often used in another way.  They register a function that is to be called by system code.  For example, in the lesson on Dash, you had the following lines:

```Python
@app.callback(
    Output("stock-price", "figure"),
    [Input("stock-dropdown", "value")]
)
def update_graph(symbol):
```
The `app.callback` method runs before `update_graph()` is ever called.  It records the fact that `update_graph()`, as wrappered by the `app.callback` wrapper function, is to be called whenever the stock dropdown changes.  You could do something like this, registering the functions to be wrapped, as follows:

```Python
callback_dict={}

def wrap_output(before, after,greeting_type):
    def decorator_wrap_output(func):
        callback_dict[greeting_type] = func
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return before + result + after
        callback_dict[greeting_type]=wrapper
        return wrapper
    return decorator_wrap_output

@wrap_output("begin:", ":end","for_hello")
def hello():
    return "Hello, World!"

@wrap_output("begin:", ":end","for_goodbye")
def goodbye():
    return "Goodbye, World!"

print(callback_dict["for_hello"]()) # Will print "begin:Hello, World!:end"

print(callback_dict["for_goodbye"]()) # Will print "begin:Goodbye, World!:end"
```

Here, the decorated functions, in their wrappered form, get registered for callbacks in `callback_dict`.  This is like what Dash is doing when you use the decorator `@app.callback`.

---

## **10.3 Python List Comprehensions**

### **Overview**  
A list comprehension is a fast and Pythonic way to generate a list.  For example, suppose you want a list of the integers from 0 to 19.  You could do

```Python
integer_list=[]
for x in range(20):
    integer_list.append(x)
```
but, with Python, you can use a list comprehension as a shorthand:
```Python
integer_list = [x for x in range(20)]
```
Or, to get just the odd ones:
```Python
odd_list = [x for x in range(20) if x%2 != 0]
```
Or, to get the squares of the odd ones:
```Python
odd_squares_list = [x**2 for x in range(20) if x%2 !=0]
# or
odd_squares_list = [x**2 for x in odd_list]
```

### **Generator Expressions**

A generator expression is just like a list comprehension, except that you use parentheses instead of square brackets.  A generator expression is an `iterable`, meaning you can use it in a `for` loop.  Like so:

```python
odd_squares_generator = (x**2 for x in range(20) if x%2 !=0)

for y in odd_squares_generator:
    print(y)

```

---

## **10.4 Python Closures**

A Python closure is a way of wrappering information by returning a function that has access to that information.  This provides some protection for the stuff you wrapper.  For example:

```Python
def make_secret(secret):
    def did_you_guess(guess):
        if guess == secret:
            print("You got it!")
        else:
            print("Nope")
    return did_you_guess

game1 = make_secret("swordfish")
game2 = make_secret("magic")

game1("magic") # Prints nope
game1("swordfish") # Prints you got it
game2("magic") # Prints you got it
```

Of course, the wrappered function could also store data, but you may need the `nonlocal` keyword.  This makes the variable still wrappered within the outer function, but accessible within the inner function:
```Python
def make_secret(secret):
    bad_guesses = 0
    def did_you_guess(guess):
        nonlocal bad_guesses
        if guess == secret:
            print("You got it!")
        else:
            bad_guesses+=1
            print(f"Nope, bad guesses: {bad_guesses}")
    return did_you_guess

game1 = make_secret("swordfish")
game1("magic") # Prints nope, bad guesses 1
game1("magic") # Prints nope, bad guesses 2
```

---


## **Summary**
In this lesson, you learned:
1. Declaring and Using Custom Python Classes
2. How to use Python Decorators
3. How to use Python List Comprehensions
4. Closures in Python

