import pandas as pd

# Create data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 28],
    "City": ["Delhi", "Mumbai", "Bangalore"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV file
df.to_csv("sample_data.csv", index=False)

print("CSV file created successfully!")
print(df)