**Professor**: paolo.felli@unibo.it
**Tutor**: federico.ruggeri6@unibo.it

---

> [!NOTE] *Python Machine*
> We call **machine** the agent performing the computation.
> 
> **Computation** is a combinatorial manipulation of symbols from a finite alphabet
> 
> The abstract machine of a **language** "L" is any agent able to execute computations described in L.

## How to "describe" the computation?
To specify a computation we must specify the **elementary operations** (applied on some data) and the sequence of those operations that should be applied.
The description must be done with a certain **language**.

Computations is executed left-to-right, but with the following order of decreasing precedence:
* parenthesis 
* \** 
+ \+ - (unary) 
* \* // % 
+ \+ - (binary)

# Python
It's a high-level and flexible language.
There is no direct connection between Python data and machine representation (it's known to be very "abstract").

 > Python is **interpretative**:
	A Python Machine provides an **interactive** interpreter for command evaluation and to show results.

 > Every value (not variable!) is bound to a specific **type**:
	The type-check happens at run-time, it is not static.
	A type is given by:
	 the **values** bound to it, 
	 how those are **presented**, 
	 the collection of **elementary operations** on them
	and the **name** of the type itself.

$$x \rightarrow obj \rightarrow (val, type, id)$$
"x" is a name bound to an object, which has a value, a type, and an ID. This relation is called "state" of an object.

>[!definition] [[#Objects|Object]]
>An object is a value enveloped in an identity.
>This identity is unique during a run of the Python machine.

In Python, any value is an object.
The Python machine controls completely the **identity** of the object.
### Methods
The envelope enclosing an object contains, besides its identity, also other information:
An important information of an object are its **methods**.

An object is an "**active value**": we may stimulate the object through the methods offered by its envelop.
The methods are often bound to the **type** of the object.

The object is the binding element between the value and its type.

>[!info] Some types can be "**Truthy**" and "**Falsy**":

Phyton allows Boolean operations to be consistently defined for any object, even if they are not Boolean values.

>[!success] For example, `0`, `None` and `""` are **Falsy**.

==Two names can be bound to the same object== (**aliases**), for example:
![[img/AdobeExpressPhotos_e69357aaf4cf44df8538ee32e6d7034b_CopyEdited.png|141]]
In this instance, x and y have the same ID.
Since we are now working with **immutable** objects (such as integers and strings), the machine reads 2 an object itself (but this is just an implementative choice, ideally the two variables would point to different elements):
```
x = 2
y = 2
```
For this reason, x and y have still the same ID.
We can't change the value of an object with an immutable type. Instead, we have to use another object with the desired value associated.

Another example:
```
T = (1,2,3)
T = T + (4,5)
```
These operations create new objects, while...
```
V = (100,200)
S = V
```
...`S` and `V` are two names for the same object.


> [!NOTE] Garbage Collector
> It keeps track of the execution and removes from the memory every element that is not referenced.

# Operations
For the correct computation, the agents need:
1. Elementary operations
2. Order of the operations
3. Description of the ordering (program)

> [!NOTE] An **assignment** is the statement which associates a **name** to a **value**
> 1. the interpreter evaluates the expression and determines a certain value
> 2. then it checks the name to see if it is already present (if not, it creates it)
> 3. finally, it binds the value to the name

### Internal State
The Python Machine maintains a list of associations (a set of **current** bindings) between names and values.
This list is called the internal state of the machine.

>[!info] The collection of binding  that defines the local space of the machine is called **namespace**.

An assignment operated on an existing name only changes the binding for said name, it doesn't create any new element.
If a name is entirely new, it's added at the end of the list.

>[!NOTE] An **expression** is one possible legal phrase of the language of which we are interested in its value.
>It is evaluated and it always carries a value.

>[!NOTE] A **command** is a phrase in the language which we use for its modification of the internal state.
>A command can also be **conditional**, in order to alter the sequential order of execution of a program.

### External State
The "environment" that interacts with the program.
* `print(...)`
	Is a **command** that transfers a value to the external state.
* `input()`
	Is an **expression** that transfers a value to the internal state, from the external state.
	It always gives values of type `str`.


>[!NOTES] A **block** is a sequence of lines at the same indentation, each with a single command.

## Lazy evaluation

When evaluating a Boolean condition block with multiple `AND` conditions, the Python machine stops when it encounters a `False` value, without checking the following conditions.
For example:
```
if A and B:
	...
```
if `A` is `False`, the machine never evaluates `B`.

Same thing happens with any composite guard of a conditional block.

```
x = 0
if False and 10 / x:
	print("a")
else:
	print("b")
```
The program will print `"b"` and will never encounter the error.

---
## Functions
A function is a named sequence of commands, which performs a computation.
They help with the subdivision of a main program in smaller, simpler, single-purpose "subprograms".

>[!tip] A function is an **object**.

Every time a function is called a **new frame** is generated to keep the related data separated from the rest of the *global frame*.
The frame is then destroyed once the function returns a final value.

When a name is called, the frame first checks for it inside of its **[[Accessing Scopes|scope]]**. If it doesn't find it locally, it searches for it in the external frame.
For example:
```
A = 10 

def foo(x): 
	return A+x 

def fie(y): 
	A=100 
	return A+y 
	
print(foo(10)) # prints 20 
print(fie(10)) # prints 210 
print(A) # prints 10
```

See the documentation of predefined functions: 
https://docs.python.org/3/library/functions.html
Catalogue of libraries:
https://docs.python.org/3/library/

When we `import` a library we bring into the global frame a set of **fully qualified names** bound to specific objects.

### Can functions modify global objects?
```
b=20 

def f(a): 
	a=10 
	b=100 
	return None 
	
f(b) 
print(b)
```
The result of the printing is `20`!
`a`,`b` are local names in the body of `f`.

```
b=20 

def f(a):
	global b     # <-- !!! 
	a=10 
	b=100 
	return None 
	
f(b) 
print(b)
```
This returns `100`.

Modifying global **mutable** objects can be done in multiple ways:
1. Through a mutable actual parameter
2. Through a global name, bound to a mutable object
In both cases we call the object with a **selection**, not with the name.

---
## Loops

```
for <name> in <sequence>:
	<block>
```

It's a **bounded iteration** that express a repetition.

1. `<sequence>` is computed and "**frozen**".
2. If `<name>` does not exists, it is created.
3. `<name>` is bound to the first element of the `<sequence>`
4. Evaluate `<block>` and, if it exists, repeat the process from point 3 with the next element in the `<sequence>`.

In point 1. the identity of object `<sequence>` itself is frozen.
Reassignments of the name of the `<sequence>` can happen, but the frozen iterabile object remains itself throughout the whole loop.

For example:
```
s = 'lodi' 
for c in s: 
	s = 'Michael' 
	print(c) 
print(s)
```
Prints: 
```
l
o
d
i
Michael
```

### Unbounded iterations
The program doesn't know beforehand how many extractions will be performed. There often is a condition that has to be satisfied for the iteration to be considered completed, however, this can result in infinite loops.

#### `while` command
The iteration continues as long as the expression in the *guard* is evaluated as `True`.

We can approximate some bounded iterations to unbounded iterations:
```
for i in range(len(s)):
	<body>
```

```
i = 0
while i < len(s):
	<body>
	i = i+1
```

The unbounded iteration does not "freeze" neither `s` nor its length.

>[!warning] Using `while` for reading input until a "sentinel"
>Example from LAB:
>```
>total = 0 
>count = 0 
>while True: 
>	r = int(input("R:")) 
>	if r == 99999: 
>		break 
>	if r >= 0: 
>		total += r 
>		count += 1 
>if count > 0: 
>	print(round(total / count, 2))
>```
### Tuples
It's an immutable sequence of objects, that groups different values, each of them of arbitrary type.
`for` can also be used to **scan** a tuple or a sequence index by index.

The function `tuple()` can be used to convert values into tuples:
```
tuple((1,2,3))  ->  (1,2,3)
```

>[!important] Reverse function
>```
>def rev(S):
>	newS = ''
>	for el in S:
>		newS = el + newS
>	return newS
>```

### Lists
It's a structured type that has as values a finite and **mutable** sequence of objects. 

>[!info] Mutable
>This means we can modify the **value** of an **object** preserving its identity.
>```
L=[10,20,30] 
L[1] = 200
>```
>The object bound to `L` did not change.
>Its value did.

Lists can be **concatenated**, **repeated**, **selected**, etc...

### **Aliasing** and side effects
```
L = [10,20,30]
V = L
L[0]=100
print(V)
```
The result prints:
```
	[100, 20, 30]
```

Since there is aliasing (`V` and `L` are **aliases for the same object**), `V` gets modified by ***side effect***.

### Deleting elements from a list
```
del L[i]
```
`L[i]` is eliminated from `L` and the elements following the element are "shifted to the left".

>[!important] `del` does NOT work with `for` cycles!
>Never use `for` on lists, if their length is modified in the for body.
>In general, don't use lists in presence of side effects!!
>
>The heading of the `for` command freezes the sequence object (its **identity**) **not its value**.

Many methods/selections of lists may be done with the **slicing** function.

>[!warning] Slicing function
>`sequence[ start : stop : step ]`

```
L=[1,2,3]

L[0:2]=[10,20]   # --> [10,20,3]
L[0:1]=[5,6]     # --> [5,6,20,3]
L[-1:]=[4]       # --> [5,6,30,4]
L[1:1]=[1,2]     # --> [5,1,2,6,20,4]
L[0:2]=[]        # --> [2,6,20,4]
L[0:0]=[1]       # --> [1,2,6,20,4]
L[len(L):]=[30]  # --> [1,2,6,20,4,30]
```

For example,
`del L[i:j]` is equivalent to `L[i:j] = []`

>[!warning] Careful:
>`L = L + [element]`
>creates a new object, while
>`L.append(element)`
>doesn't.

### Augmented assignment
`+=  -=  *=  /=  //=  %=  **=`

These operations are **done in place**, if possible.
LHS is evaluated first.

---
# Recursion
Functions may call functions in their body.
Hence a function may call itself in its body (the name of a function is in scope within the function).

Recursion is composed by:
- a **base** case
- a **recursive** case
Termination occurs when the recursive case ends on a **simpler** (closer to the base) case.

>[!warning] General theorem of the **theory of computation**
>Any computation that is expressible through iteration is also expressible through recursion. And vice versa.

---

## Dictionaries
A dictionary is a generalization, a mutable mapping between immutable objects (*keys*) and arbitrary objects (*values*).

These structures are NOT sequences, therefore they can't be sliced or concatenated.

Similarly to lists, dictionaries must not be used inside `for` cycles, if their length is modified in the body.
Additionally, a modification to a dictionary which is used to control a `for` raises a run time error!

>[!info] The method `get()`
>It can be used to perform the "*if key present, otherwise update*" check, using the `default` argument:
>```
>D.get(key, default)
>```
>Returns `D[key]` if it exists, otherwise returns the default option.

The methods
	`D.keys()` 
	`D.values()` 
	`D.items()`
return **view objects** on keys, values and items (pairs).
These dynamic lists can be *frozen* into lists:
	`list(D.items())`
	returns a list of tuples.

>[!warning] `list(D)` is equivalent to `list(D.keys())`

>[!info] The method `update()`
>It can be used as a substitute for **concatenation** in dictionaries, which do not support that type of operation:
>```
>D1.update(D2)
>```
>It extends `D1` with the items of `D2`, if there are equal keys in `D1` and `D2`, the ones in `D2` ("update") are chosen.

---
## Comprehension

>[!info] Comprehension principle
>It's the operation by which, given a condition expressible by a formula $\phi (x)$, we form the set of all those $x$ meeting that condition:
>$$\{x \mid \phi(x)\}$$

`doubles=[2*i for i in range(1,101)]`

Expressed in a compact way, it returns the doubles of the numbers from 0 to 100.

### Nested comprehension
For example:
	*The list of lists of numbers from 0 to i, for i less than 20*

`[ [k for k in range(i)] for i in range(21)]`

### List Comprehension

`[expression for name in sequence]`

`expression` is always evaluated in its local frame and **after** the `for name in sequence`.

>[!info] `[expression for name in sequence series of for/if]`
>is equivalent to
>```
>res=[] 
>for name in sequence : 
>	series of for/if 
>		res.append(expression) 
>return res
>```

### Comprehensions on dictionaries

`{key:val for name in sequence}`

For example:
```
{i:[k for k in range(i)] for i in range(10)}
```

>[!warning] There is no comprehension on tuples

However, expressions which seem "tuple comprehension" are legal Python code, and are called **generators**:

```
G = (i*2 for i in range(10))
```

>[!info] Generators
>A generator is a kind of "potential sequence/tuple" which is able to generate the elements of the sequence, through the predefined function `next(…)`.
>```
>next(G) # : evaluates to 0 
>next(G) # : evaluates to 2 
>next(G) # : evaluates to 4 
>next(G) # : the generator is exhausted an error is raised
>```
>
>It is a particular case of **iterator**.

>[!warning] Command `yield`
>```
>yield expression
>```
>The presence of `yield` make the `def` define a generator.

It returns the value of `expression` and suspends the evaluation of the function (the frame is not destroyed, all the values of the local names are preserved, the point where execution is paused is preserved).

- Calling the generator's name returns the generator's **object** (the body is **not** evaluated yet).
- Calls to the function `next(G)` cause the execution of the body of the generator, until `yield` is found.
- `yield` suspends the execution of the body and returns the value of the `expression` ad value of the call to `next(G)`.

---
# Objects
An **object** is a value encapsulated into an *identity*.

>[!warning] **Class**
>It's a collection of objects which share:
>- structure
>- operations
>- methods

For example:
```
class Point: 
	def __init__(self): 
		self.x=0 
		self.y=0 
	
	def whoareyou(self): 
		return self.x, self.y 
		
	def move(self, delta): 
		self.x+=delta 
		self.y+=delta
```

To create **instances** of a class we use the **name of the class as a function**.
```
p = Point()
```
The structure of the instance that is returned is defined by the method `__init__`.

>By convention, for the first parameter we use `self`.
>`self` must be used to access the attributes of the instance.

>[!info] **Magic methods**
>"Dunder":  `__`
>Methods in this form are "magic methods", by convention reserved for special purposes by the Python machine.
>
>- `__init__`.
>- `__add__`, `__sub__`, `__mul__` called by `+`, `-` and `*` respectively.
>- `__floordiv__` and `__truediv__` called by `//` and `/` respectively.
>- `__pow__` called by `**`.
>- `__str__` called by `print()`.
>- `__repr__` is used internally by the interpreter to represent the value.
>- `__eq__` called by `==`.
>- `__ne__` called by `!=`.
>- `__lt__` called by `<`.
>- `__gt__` called by `>`.
>- `__le__` called by `<=`.
>- `__ge__` called by `>=`.
>- $...$
>  
>  There are also magic methods for in-place operations.
>  All of these methods can be overridden.

Boolean operations (and, or, not) cannot be redefined through special dunder methods `__xxx__` (because of the lazy evaluation, so hardwired in the python machine).

### Class attributes $vs$ Instance attributes
All instances of a class share an attribute modifications to the attribute are immediately shared by all instances.

>[!info] Class attributes
>Are static attributes, accessed by **dot notation**, using the class name.
>They belong to the class itself.

>[!Instance attributes]
>Are variables that  are unique and belong to a specific object and are only accessible within the object.
>These attributes are **not** shared between instances.


>[!danger] Do not use mutable objects as default arguments

---

# Inheritance and sub-classes
We want to define a new class with the same data as a previous class `A`, but more operations.
$\implies$ we must **extend** `A`.

For example, we create a new class `NewPoint` such that *any instance of `NewPoint` is an instance of `Point`*.
We can say that `NewPoint` is a **subclass**.


---
# Exceptions

```
try: 
	<block>
except <exception>:
	<handlerblock>
<after>
```

>[!warning] Asking user for a valid input
>```
>while True:
> 	try:
> 		age = int(input("Please enter your age: "))
> 	except ValueError:
> 		print("Sorry, I didn't understand that.")
> 	#better try again... Return to the start of the loop
> 		continue
> 	else:
> 		#age was successfully parsed!
> 		#we're ready to exit the loop.
> 		break
> if age >= 18: 
> 	print("You are able to vote in the United States!")
>else:
>	print("You are not able to vote in the United States.")
>```
>
>Or we can simulate a "`do...while`" with `x = None` and then the `while` cycle.

```
try: 
	<block> 
except name1: 
	<block>
. . . 
else: 
	<block>
finally:
	<finalblock>
```

`<finalblock>` is executed in any case, as final code before leaving the **try**, either if exceptions are or are not raised, or are handled or non handled.

## Exceptions and the frame stack
Exceptions are **propagated** through the stack. 
Frames are **popped out** of the stack if their function does not handle the exception. The code remaining in those functions is not executed.
If an exception is never caught, the exception is passed to the standard exception handler of the main: 
	the program terminates and the exception is printed.

>[!idea] It's like a break in a series of nested cycles.

## Hierarchies of user defined exceptions
An *except* clause will catch all exceptions of the specified instance, **therefore all instances of its subclasses**.

We can define exceptions:
```
class MyExcp(Exception): pass 
class MySpec1(MyExcp): pass 
class MySpec2(MyExcp): pass
```
