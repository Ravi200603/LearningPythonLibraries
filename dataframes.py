import pandas as pd 

data = {"Name":["Spongbob", "Patrick", "Squidward"], "Age": [30, 35, 50]}

df = pd.DataFrame(data, index = ["Emp1", "Emp2", "Emp3"])

# add a new column 
df["job"] = ["Cook", "N/A", "Cashier"]



# add a new row 
new_row = pd.DataFrame([{"Name":"Sandy", "age" :28, "Job" : "Engineer"}], index = ["Emp4"])
df = pd.concat([df, new_row])
print(df)



