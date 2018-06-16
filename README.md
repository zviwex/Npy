# Npy
Normalize Python block and indentation technique 


[![PyPI](https://img.shields.io/badge/pypi-v3.12.0-green.svg?style=flat)](https://pypi.python.org/pypi/npy/)
[![Twitter](https://img.shields.io/badge/twitter-ZviWex-4099FF.svg?style=flat)](https://twitter.com/ZviWex)
[![GNU License](https://img.shields.io/badge/license-GNU-blue.svg?style=flat)](https://www.gnu.org/licenses/gpl-3.0.en.html)
[![WebSite](https://img.shields.io/website-down-red/http/shields.io.svg?label=website)](https://ZviWex.com)
# Usage
## As runner
You can write your program in .npy file with the right way to indexnt and to crate blocks, and then run the normalyze.py parser on the file/repo

```sh
python normalyze.py file_path
python normalyze.py -d dir_path
python normalyze.py -h
```
The  normalyze.py file will be at <Python dir>\Scripts

This options is to convert the .npy file (normal indentation file) to a .py file (readable to python interpreter)

## As module
You can write your code this way and run it directly from python interptreter

```python
import npy; exec(npy.run("""

# Your code goes here
"-"-"
Lined raw string will look like this 
"-"-"

"""),globals())
```
Note - this supports modules too.

# Installation

```sh
python -m pip install --upgrade pip
python -m pip install --upgrade npy
```

# Contact
If you have any questions feel free to ping me
at [here](https://ZviWex.com/) to connect.
There is also a [mail address](mailto:zvikizviki@gmail.com) for higher latency discussion.
