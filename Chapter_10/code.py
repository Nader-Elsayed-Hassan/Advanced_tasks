# Context manager time measurement
import time
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        end = time.time()
        print(f"Execution took {end - self.start:.2f} seconds")
with Timer():
    for i in range(1_000_000):
        pass



# Generate
def even_numbers(n):
    i = 2
    while i <= n:
        yield i
        i += 2
for even in even_numbers(10):
    print(even)
    
    
    

# Coroutine
def filter_positive():
    while True:
        number = (yield)
        if number > 0:
            print(f"Positive number: {number}")
positive = filter_positive()
next(positive)
positive.send(10)
positive.send(-5)
positive.send(3)





# Factory pattern
class Circle: 
    def draw(self): 
        return "Drawing Circle" 
class Square: 
    def draw(self):
        return "Drawing Square" 
def shape_factory(shape_type): 
    if shape_type == "circle": 
        return Circle() 
    elif shape_type == "square": 
        return Square() 
    else: 
        return None
shape1 = shape_factory("circle") 
print(shape1.draw()) 
shape2 = shape_factory("square") 
print(shape2.draw())