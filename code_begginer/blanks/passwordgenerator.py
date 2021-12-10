
import random

upper = "QWERTYUIOPLKJHGFDSAZXCVBNM"
lower = "qwertyuioplkjhgfdsazxcvbnm"
nums = "0123456789"
symbols = "!@#$%^&*()-_=+|?{}[]"
length = 15
all = lower + upper + nums + symbols
password = "".join(random.sample(all, length))

def password_generator():
    print(password)
    
