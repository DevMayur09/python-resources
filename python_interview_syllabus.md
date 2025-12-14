# Python Interview Syllabus --- Fundamental to Advanced

## 1. Python Fundamentals

-   What is Python, features, advantages
-   Installation, interpreter, bytecode, .pyc
-   Syntax, indentation rules
-   Variables & assignment
-   Keywords
-   Data types overview
-   Comments & docstrings
-   Input/output functions
-   Operators: arithmetic, comparison, logical, identity, membership

## 2. Python Data Types (Deep Concepts)

-   Numbers
-   Strings: immutability, slicing, interning, encoding
-   Lists: dynamic array internals, shallow vs deep copy
-   Tuples: immutability, packing/unpacking, hashability
-   Dictionaries: hash tables, collision resolution, ordered behavior
-   Sets & Frozensets
-   Boolean
-   Range
-   Bytes & Bytearray

## 3. Variables & Memory Model

-   Memory allocation
-   Stack vs heap
-   Reference counting
-   Garbage collector
-   sys.getrefcount
-   Python object model
-   Mutable vs immutable
-   Interning
-   Shallow vs deep copy
-   id(), type(), dir()

## 4. Functions

-   Defining functions
-   Return types
-   Arguments: positional, keyword, default (pitfalls)
-   \*args, \*\*kwargs
-   Lambda functions
-   First-class functions
-   Higher-order functions
-   Closures
-   Decorators
-   Partial functions (functools)

## 5. Object-Oriented Programming

-   Classes & objects
-   **init**
-   Self
-   Instance vs class variables
-   Instance, class, static methods
-   Inheritance (all types)
-   Method overriding
-   MRO
-   super()
-   Polymorphism
-   Encapsulation
-   Abstract classes (abc)
-   Composition vs inheritance
-   Data classes
-   Magic methods

## 6. Modules & Packages

-   Imports
-   **name** == "**main**"
-   Creating modules
-   Virtual environments
-   pip & PyPI
-   Python path

## 7. Error Handling

-   Exception hierarchy
-   Try/except/finally
-   Custom exceptions
-   Raising exceptions
-   Context managers

## 8. File Handling

-   File reading/writing
-   JSON
-   CSV
-   Pickle & serialization

## 9. Iterables, Iterators & Generators

-   Iterable vs Iterator
-   iter(), next()
-   Generator functions
-   yield, yield from
-   Generator expressions

## 10. Collections Module

-   namedtuple
-   deque
-   Counter
-   OrderedDict
-   defaultdict
-   ChainMap
-   heapq
-   bisect

## 11. Concurrency & Parallelism

### Multithreading

-   Threading
-   ThreadPoolExecutor
-   Race conditions
-   Locks

### Multiprocessing

-   Processes
-   Queues, pipes
-   Pool

### AsyncIO

-   Event loop
-   async/await
-   Tasks
-   When to use async vs threads vs processes

## 12. Memory, Performance & Optimization

-   Big-O
-   Profiling (cProfile, timeit)
-   Caching (lru_cache)
-   Optimizing loops
-   String builder pattern
-   Sets for fast lookup

## 13. Python Internals

-   CPython architecture
-   Bytecode
-   dis module
-   Dict/list internals
-   Ref counting
-   GIL
-   Green threads

## 14. Design Patterns

-   Singleton
-   Factory
-   Strategy
-   Observer
-   Adapter
-   Facade
-   DI
-   Builder

## 15. Testing in Python

-   unittest
-   pytest
-   Fixtures
-   Mocking
-   Patching
-   Coverage

## 16. Backend Development

### FastAPI / Django / Flask

-   Routing
-   Middleware
-   ORMs
-   Auth/JWT
-   Caching
-   Logging
-   Pagination

### Databases

-   PostgreSQL basics
-   Indexing
-   Transactions
-   Connection pooling

## 17. Deployment

-   Docker
-   CI/CD
-   Environment variables
-   Gunicorn/Uvicorn
-   Nginx
-   Scaling

## 18. DevOps & Cloud

-   AWS services
-   Serverless Python

## 19. Data Science (Optional)

-   NumPy
-   Pandas
-   Matplotlib
-   sklearn
