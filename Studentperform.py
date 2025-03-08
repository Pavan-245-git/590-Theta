import pandas as pd
data =[20,30,40,50,2,3,6,8,10,18,19,20,24,2,4,5,6]

No_of_studied = data[4:8]
print("No.Of hours_studied",No_of_studied)
Age = data[9:13]
print("Student_age",Age)
screen_time = data[12:18]
print("Screen_time",screen_time)
Data_Frame = pd.DataFrame(data)
print(Data_Frame)