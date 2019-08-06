"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""
import platform
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
modulez = sys.argv[0]
print(modulez)

# Print out the OS platform you're using:
# YOUR CODE HERE

print(platform.platform())

# OS Architecture type
print(platform.architecture())

# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version_info[0])

#Exact version of python
print(platform.python_version())

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

print("Process ID:", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print("Current working dir", os.getcwd())


# Print out your machine's login name
# YOUR CODE HERE
print("Login name:", os.getlogin())
