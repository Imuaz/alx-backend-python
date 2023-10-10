# 0x02. Python - Async Comprehension

The project covered various aspects of asynchronous programming in Python, including writing asynchronous generators, using async comprehensions, and type-annotating generators.
These topics are crucial for developing efficient and maintainable asynchronous code in Python.

## Resources:books:
***Read or watch:***
- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)
- [Type-hints for generators](https://stackoverflow.com/questions/42531143/how-to-type-hint-a-generator-in-python-3)

## Requirements:round_pushpin:

**General**
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A mandatory [README.md](./README.md) file, at the root of the folder of the project.
- The code should use the `pycodestyle` style (version 2.5.x)
- The length of files should be tested using `wc`
- All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All functions and coroutines must be type-annotated.

## Tasks:page_with_curl:
**0. Async Generator**
- [0-async_generator.py](./0-async_generator.py):  A coroutine that takes no arguments.
  - The coroutine loops 10 times, each time asynchronously wait 1 second, then yields a random number between 0 and 10.
  - it uses the `random` module.

**1. Async Comprehensions**
- [1-async_comprehension.py](./1-async_comprehension.py): A coroutine that imports `async_generator` and takes no arguments.
  - The coroutine collects 10 random numbers using an async comprehensing over `async_generator`, then returns the 10 random numbers.

**2. Run time for four parallel comprehensions**
- [2-measure_runtime.py](./2-measure_runtime.py): A coroutine that imports `async_comprehension` and executes it four times in parallel using `asyncio.gather`.
  - it measures the total runtime which is roughly 10 seconds and returns it.

##Helper files:raise_hand:
- [tests](./tests): A directort that contains all the given main files for testing purposes



