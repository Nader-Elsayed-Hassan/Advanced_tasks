# Problem1: Validate Email Addresses 
import re 
email_regex = r"^\w[\w.]*@\w+\.(com|org|edu)$" 
emails = ["user@example.com", "bad-email", "test@domain.org"] 
print(f"Testing regex: {email_regex}\n") 
for email in emails: 
    if re.fullmatch(email_regex, email): 
        validation_status = "Valid" 
    else: 
        validation_status = "Invalid" 
    print(f"'{email}': {validation_status}")


# problem 2 : Extract Hashtag 
import re 
text = "I love #Python and #AI" 
hashtag_regex = r"#\w+" 
hashtags = re.findall(hashtag_regex, text) 
print(hashtags)



# problem 3 : Validate phone number 
import re 
phone_regex = r"^(\+1-)?\d{3}-\d{3}-\d{4}$" 
phone_numbers = ["+1-555-1234", "123-456-7890", "5551234", "123-45-6789"] 
for number in phone_numbers: 
    if re.fullmatch(phone_regex, number): 
        validation_status = "Valid" 
    else: 
        validation_status = "Invalid" 
    print(f"'{number}': {validation_status}") 
    
    
    
# problem 4 : Word frequency (Regex Tokenizer)  
import re 
from collections import Counter 
text = "Python, Python! AI is great; Python AI." 
word_regex = r"[A-Za-z]+" 
words = re.findall(word_regex, text.lower()) 
word_counts = Counter(words) 
print(f"Text: '{text}'") 
print(f"Word Frequencies: {dict(word_counts)}")



# problem 8 : Extract Programming language 
import re 
text = "I know Python, Java, and C++ but not Ruby." 
language_regex = r"Python|Java|C\+\+|Ruby" 
languages = re.findall(language_regex, text) 
print(f"Text: '{text}'")  
print(f"Extracted Languages: {languages}")