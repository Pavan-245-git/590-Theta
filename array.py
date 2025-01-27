import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(arr[1, 1, 2])
#arr[0,2,2]
#arr[1,2,1]



import numpy as pd
arr = arr = np.array([[[1, 1, 2, 3], [4, 4, 5, 6]], [[7, 8, 9, 9], [10, 11, 12, 13]]])
print(arr)
a= int(input("Enter number of rows: "))
b= int(input("Enter the elements: "))
print(arr[a,b])



import numpy as pd

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])


import pandas as pd

Patient_information ={
    "patient_name":["Sunil","Pavan","Mani","Rajni"],
    "Age":[19,18,20,21],
    "Date_of_oppointment":['2024-8-21','2024-7-20','2024-6-12','2024-5-11'],
    "patient_id":[101,102,103,104]

}

drag_quantity ={
    "name":["snji","shins","sdaas","sasa"],
    "quantity":[100,90,80,70],
    "patient_id":[101,102,103,104]
}

patient_df = pd.DataFrame(Patient_information)
drag_df = pd.DataFrame(drag_quantity)
print(f"PATIENT DATA :\n{patient_df} ,\nDRAG DATA :\n{drag_df}")

filtered_df = patient_df[patient_df["Age"] < 6]