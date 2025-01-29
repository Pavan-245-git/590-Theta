import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
data = {
    "Customer_id":[1,2,3,4],
    "Ranks":["First","Second","Third","Fourth"],
    "fruits":["apple","banana","orange","kiwi"],
    "Gender":["Male","Female","Male","Female"]
}

df = pd.DataFrame(data)
label_encoder = LabelEncoder()
df["encoder_ranks"] = label_encoder.fit_transform(df["Ranks"])
df["encoder_fruits"] = label_encoder.fit_transform(df["fruits"])
print(f"The LabelEncoder Data id:\n {df}")

one_hot_encoder = OneHotEncoder()
column_encode = ["Gender","Ranks","fruits"]

encoded_data = one_hot_encoder.fit_transform(df[column_encode])
encoded_column = one_hot_encoder.get_feature_names_out(column_encode)

encoded_df = pd.DataFrame(encoded_data_dense,columns=encoded_column)

print(f"The One Hot Encoder :\n {encoder_df}")