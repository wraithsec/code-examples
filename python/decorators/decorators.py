#!/usr/bin/python3
from functools import wraps 

def upper(func):
    @wraps(func) 
    def wrapper(msg):
        return msg.upper() 
    return wrapper
        
@upper
def say_hi(msg):
    return msg 

print(say_hi("Hello"))
print(say_hi.__wrapped__("Hello"))
    #Important to note that @wraps allows us to have .__wrapped__ to access the original.     
