# Transform and clean data: - 
products = [" LAPTOP", "phone", "Tablet", "CAMERA "] 
clean_products = list(map(lambda p: p.strip().title(), products)) 
print(clean_products)
# Output: ['Laptop', 'Phone', 'Tablet', 'Camera']


#  Convert Temperatures (Celsius → Fahrenheit):- 
celsius = [0, 10, 20, 30, 40] 
fahrenheit = list(map(lambda c: (9/5) * c + 32, celsius)) 
print(fahrenheit)
# Output: [32.0, 50.0, 68.0, 86.0, 104.0]


# Apply Multiple Transformations:- 
nums = [1, 2, 3, 4, 5] 
transformed_nums = list(map(lambda x: x**2 + 10, nums)) 
print(transformed_nums)
# Output: [11, 14, 19, 26, 35]


# Extract First and Last Characters:- 
words = ["python", "lambda", "programming", "map", "function"] 
char_tuples = list(map(lambda w: (w[0], w[-1]), words)) 
print(char_tuples)
# Output: [('p', 'n'), ('l', 'a'), ('p', 'g'), ('m', 'p'), ('f', 'n')]


#  Nested Map Transformation:- 
marks = [[45, 80, 70], [90, 60, 100], [88, 76, 92]] 
transformed_marks = list(map( 
lambda row: list(map(lambda x: round(x * 1.05), row)), 
marks 
)) 
print(transformed_marks)
# Output: [[47, 84, 74], [95, 63, 105], [92, 80, 97]]


# Create a program that normalizes a list of numbers between 0 and 1 
# using map() and lambda:- 
data = [10, 20, 30, 40, 50] 
min_val = min(data) 
max_val = max(data) 
range_val = max_val - min_val 
if range_val == 0: 
    normalized_data = [0.0] * len(data) 
else: 
    normalized_data = list(map(lambda x: (x - min_val) / range_val, data)) 
print(normalized_data)
# Output: [0.0, 0.25, 0.5, 0.75, 1.0]


# Given a list of sentences, extract the length of each word in every 
# sentence using nested map():- 
sentences = [ 
    "Python is fun", 
    "Nested map functions are useful", 
    "List comprehension is concise" 
] 
word_lengths = list(map( 
    lambda s: list(map(lambda w: len(w), s.split())), 
    sentences 
)) 
print(word_lengths)
# Output: [[6, 2, 3], [6, 3, 9, 3, 6], [4, 13, 2, 7]]