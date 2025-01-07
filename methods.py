
a = "pineapple"
b = "PINEAPPLE"


print(a.upper())  

print(b.lower())  

c = "  hello brother  "
print(c.strip())  


d = "pavan !!!"
print(d.rstrip(" !"))  

print(a.replace("pineapple", "pavan")) 

e = "hello, bro how are you"
print(e.split())  

print(e.capitalize())  

print(a.center(50))              


print(a.count("a"))  


print(a.find("a"))  


f = "iam fine"
print(f.index("fine"))  

print(f.title())  


student = {
    1 : {"name": "google","age":14},
    2 : {"name": "deloite","age":20},
    3 : {"name": "pavan","age":20},
    4 : {"name": "super","age:18"},

}

for student_id,details in students.items()
print(f"Student ID:  {student_id},Name: {details{'name'}},Age:{details['age']}")
