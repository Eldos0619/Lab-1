import time
import math
def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)  

print(f"Square root of 25100 after 2123 milliseconds is {delayed_sqrt(25100, 2123)}")