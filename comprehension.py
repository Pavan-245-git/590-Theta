#list comprehension

#list = [1,2,3,5]

res = [i+1 for i in range (1,20)]
print(res)


list = [1,2,3,4,5,6,7,8,9]
res = [i for i in list if i%2==0]
print("even number",res)
od=[i for i in list if i%2 !=0]
print("odd number:",od)

#lower and upper case letters
words = ["LOWER", "W", "PYTHON"]
lower= [i.upper() for i in words]



#creating dictionary comprehension from two list

keys = ["name", "age", "city"]
values = ["pavan", "20", "Hyderabad"]
list = [i for i in list]
dict ={k:v for k,v in zip(keys,values)}
print(dict)

#tuple

import math
num = [1,2,3,4,5]
sq=tuple(i for i in num)

print(sq)

#tuple comprehension

import math
num = [1,4,16,9,25]
sq=tuple(math.sqrt(i) for i in num)
print(sq)


#give me the product details with price less than 500 use of dictionary comprehension

product = [

    {"name":"laptop", "price":800},
    {"name":"Smartphone", "price":500},
    {"name":"tablet", "price":400},

]

affordable_products = {i["name"]:i["price"]for i in product if i["price"]<500}