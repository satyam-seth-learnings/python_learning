# Example-23 Module
from User import request
request.user_request()

# pwd -> /e/OneDrive/Python/Geekyshows/SMS/Tech
# python Example-23.py
# ->
# ModuleNotFoundError: No module named 'User'

# pwd -> /e/OneDrive/Python/Geekyshows/SMS
# python Example-23.py
# ->
# (null): can't open file 'Example-23.py': [Errno 2] No such file or directory

# -m mod : run library module as a script (terminates option list)
# pwd -> /e/OneDrive/Python/Geekyshows/SMS
# python -m Tech.Example-23
# -> 
# User Package --> request Module
# user_request Function