
# Lesson 12 — More Python Skills

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
    _species = "Canis lupus familiaris" #single underscore
    __count = 0  # double underscore: name mangling

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog._Dog__count += 1 

    def call_dog(self):
        print(f"Come here, {self.name}!")

    def speak(self):
        print("bark bark bark")

    @classmethod
    def get_dog_count(cls):
        return cls._Dog__count

dog1 = Dog("Spot", 2)
dog1.call_dog()
dog1.speak()
print(f"dog1's name is {dog1.name}.")
print(f"Species: {dog1._species}")

dog2 = Dog("Wally", 4)
dog2.call_dog()
dog2.age += 1
print(dog2.age)

print(f"Total dogs created: {Dog.get_dog_count()}")     
```
There are quite a few new things going on here:
- This `Dog` class includes two *class variables*: `_species` and `__count`. Unlike the instance variables like `name` and `age`, these belong to the class itself — not to each individual dog. This means they are shared across all Dog objects, not unique to one. You can tell they are class variables because they are not inside the `__init__()` method.
- What about the strange naming conventions on those class variables? As mentioned earlier, Python doesn't support truly private data within a class — everything is technically accessible. However, in Python there are conventions to signal that something is meant to be internal:
    -  The *single underscore* in front of a variable (like `_species`) is a soft warning to developers. It indicates that the variables is for internal use: please don't modify it directly, and access it through a method if possible. 
    -  The *double* underscore (like `__count`) sends an even stronger signal. Python will automatically *name mangle* these variables to help prevent accidental access or modifications. For example, `__count ` becomes `_Dog__count`. This is useful for values like the dog counter, as we don't want users to reset it by accident.
- The method `get_dog_count()` is a *class method*, meaning it's called on the class itself rather than an individual dog object. Such methods are declared using the `@classmethod` decorator (we will talk more about decorators below).
- Instead of taking `self` as the first parameter,  `get_dog_count()` uses `cls` -- short for "class". That's because it is a method applied to the class, rather than a specific object. `cls` allows us to access the shared class attribute `__count` (and since it is name-mangled, we must refer to it as `cls._Dog__count`). 

### Class inheritance
Suppose you want to create a class that’s almost like Dog, but with a few differences — maybe a bigger bark, or a new behavior like fetching. Instead of rewriting everything from scratch, Python (and OOP in general) lets you *inherit* from your existing class and just customize the parts you want. This is called *class inheritance*.

Here's an example where we create a class `BigDog` that explicitly inherits the attributes of `Dog`:

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
- The `call_dog()` method is inherited from `Dog`, since we didn’t override it.
- The `speak()` method is overridden to make big dogs sound different.
- The `speak_verbose()` method shows how to call both the original `Dog.speak()` (using `super()`) and the new `BigDog.speak()`.

### A few other facts about classes
A useful attribute of every class and instance is `__dict__`.

```python
print(Dog.__dict__) # prints stuff for the Dog class, including its methods
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

## **10.2 Python Decorators**

### **Overview**
Python classifies functions as first class citizens, which means that you are able to apply one function to another function. Decorators allow this to be clearer and easier to read.

### **Key techniques**
Decorators are functions that can be called in a unique way, and accept a function as an input.

```python

def decorator(func):
    def wrapper():
        print ("Hello!")
        func()
        print ("World")
@decorator
def name():
    print("John")
```

Note in this example the output:
```
Hello!
John
World!
```

Why did we get this result? The answer is because @decorator called the function using the decorator function. It is effectively equivalent to calling
```python
decorator(name())
```
but is much clearer and easier to understand.

In this example the function is fairly trivial, however in the next section we can dig into a more useful way to use this.

### **Example code**

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
        print ("Finished in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def time_consuming_function(...):
    ...
```

Sometimes you need to have a decorator that itself has arguments.  In this case, you need two levels of wrapping:

```Python
def wrap_output(before, after):
    def decorator_wrap_output(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return before + result + after
        return wrapper
    return decorator_wrap_output

@wrap_output("begin:", ":end")
def hello():
    return "Hello, World!"

print(hello()) # Will print "begin:Hello, World!:end"
```

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

## **10.2 Python List Comprehensions**

### **Overview**  
A list comprehension is a fast way to generate a list.  For example, suppose you want a list of the integers from 0 to 19.  You could do

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

## **10.3 Python Closures**

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
1. How to use Python Decorators
2. How to use Python List Comprehensions
3. Closures in Python
4. Declaring and Using Custom Python Classes
