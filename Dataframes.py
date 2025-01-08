import pandas as pd
screen_time =[2,8,9]
sleep_hours = [3,8,10]
stu_name =["Pavan","Kalyan","Kartik"]
dict1 = {
    "screen_time":screen_time,
    "sleep_hours":sleep_hours,
    "stu_name":stu_name
}

print(dict1)
df = pd.DataFrame(dict1)
print(df)