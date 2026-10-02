import pandas as pd
import os

# Create data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 28],
    "City": ["Delhi", "Mumbai", "Bangalore"]
}

# Create DataFrame
df = pd.DataFrame(data)

new_row={"Name":"gf1","age":20,"city":"NYC"}
df.loc[len(df.index)]=new_row
# Save to CSV file

os.makedirs('data',exist_ok=True)
file_p=os.path.join('data',"sample_data.csv")

df.to_csv(file_p, index=False)

print("CSV file created successfully!")
print(df)