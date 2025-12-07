# CSV Handling : 
import csv 
with open("students.csv", newline="") as file: 
    reader = csv.DictReader(file) 
    print("Students scoring above 80:") 
    for row in reader: 
        if int(row["Grade"]) > 80: 
            print(row["Name"]) 
            
            

# JSON Handling : 
import json 
data = { 
    "course": "Python", 
    "duration": "3 months", 
    "students": ["Ali", "Sara"] 
} 
with open("course.json", "w") as file: 
    json.dump(data, file, indent=4) 
with open("course.json") as file: 
    loaded = json.load(file) 
print("Students:", loaded["students"]) 



# Excel Handling : 
import pandas as pd 
df = pd.DataFrame({ 
    "ID": [1, 2, 3], 
    "Name": ["Ali", "Mona", "Omar"], 
    "Salary": [5000, 7000, 6500] 
}) 
df.to_excel("employees.xlsx", index=False) 
df = pd.read_excel("employees.xlsx") 
print(df[["Name", "Salary"]])



# Data Transformation : 
import csv 
import json 
def csv_to_json(csv_file, json_file): 
    people = [] 
    with open(csv_file, newline="") as file: 
        reader = csv.DictReader(file) 
        for row in reader: 
            people.append({ 
                "Name": row["Name"], 
                "Age": int(row["Age"]), 
                "City": row["City"] 
            }) 
    output = {"people": people} 
    with open(json_file, "w") as file: 
        json.dump(output, file, indent=4)  
csv_to_json("people.csv", "people.json")