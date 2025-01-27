def div(a,b):
  return a/b
print(div(2,4))
     


     def dev_dec(func):
    def inner(a, b):
        if a * b > 20:
            return a / b
        else:
            return func(a, b)
    return inner
@dev_dec
def mul(a, b):
    return a * b
print(mul(2, 4))
print(mul(4, 2))
print(mul(4, 20))



from google.colab import files
import pandas as pd
uploaded = files.upload()
filename = list(uploaded.keys())[0]
df = pd.read_csv(filename)
df
     
df.describe()
     
df.info()

df.iloc[::,:3]