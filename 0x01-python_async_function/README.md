# 0x01. Python - Async

The project delved into asynchronous programming in Python, covering `async` and `await` syntax. It also explained how to execute an `async` program using `asyncio`, run concurrent coroutines, create `asyncio` tasks, and utilize the `random` module for various applications. 
In summary, the project provided a comprehensive understanding of asynchronous programming techniques and their practical implementation in Python.

## Resources:books:
***Read or watch:***
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Requirements:round_pushpin:

**General**
- A mandatory [README.md](./README.md) file, at the root of the folder of the project.
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files should end with a new line
- All files must be executable
- The length of the files should be tested using `wc`
- The first line of all files should be exactly `#!/usr/bin/env python3`
- The code should use the `pycodestyle` style (version 2.5.x)
- All functions and coroutines must be type-annotated.
- All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)


## Tasks:page_with_curl:
**0. The basics of async**
- [0-basic_async_syntax.py](./0-basic_async_syntax.py): An asynchronous coroutine that takes in an integer argument (`max_delay`, with a default value of `10`) named `wait_random` that waits for a random delay between `0` and `max_delay` (included and float value) seconds and eventually returns it.
  - It uses the `random` module.

**1. Let's execute multiple coroutines at the same time with async**
- [1-concurrent_coroutines.py](./1-concurrent_coroutines.py): An async routine called `wait_n` that imports `wait_random` from the `0-basic_async_syntax` and takes in 2 int arguments (in this order): `n` and `max_delay`, spawns `wait_random` `n` times with the specified `max_delay`.
  - `wait_n` returns the list of all the delays (float values) in ascending order without using `sort()` because of concurrency.

**2. Measure the runtime**
- [2-measure_runtime.py](./2-measure_runtime.py): `measure_time` function with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n`. 
  - It imports `wait_n` from `1-concurrent_coroutines` module
  - it returns a float.
  - it uses the `time` module to measure an approximate elapsed time.

**3. Tasks**
- [3-tasks.py](./3-tasks.py): `task_wait_random` function (not an async function, it uses the regular function syntax) that takes an integer `max_delay` and returns a `asyncio.Task`.
  - it imports `wait_random` from `0-basic_async_syntax` module

**4. Tasks**
- [4-tasks.py](./4-tasks.py): A modified [wait_n](./1-concurrent_coroutines.py) function `task_wait_n` that calls `task_wait_random`.
  - it nearly identical to `wait_n` except [task_wait_random](./3-tasks.py) is being called.

## Helper files:raise_hand:
- [tests](./tests): A directory that contain main files for testing purpose

:+1:
