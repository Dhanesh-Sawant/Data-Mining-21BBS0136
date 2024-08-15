import pandas as pd
import random
from mlxtend.frequent_patterns import fpgrowth, association_rules

# Step 1: Generate a synthetic dataset representing monthly sales
vehicles = ['Sedan', 'SUV', 'Truck', 'Convertible', 'Hatchback', 'Minivan']
months = ['January', 'February', 'March', 'April', 'May', 'June']

# Generate random sales transactions
data = []
for _ in range(100):  # 100 transactions
    month = random.choice(months)
    purchased_vehicles = random.sample(vehicles, k=random.randint(1, 3))  # purchase 1 to 3 vehicles
    data.append([month] + purchased_vehicles)

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Month', 'Vehicle1', 'Vehicle2', 'Vehicle3'])

# Step 2: One-hot encode the vehicle purchases for FP-Growth
df_one_hot = pd.get_dummies(df[['Vehicle1', 'Vehicle2', 'Vehicle3']], prefix='', prefix_sep='').groupby(level=0, axis=1).sum()
df_one_hot = df_one_hot.clip(upper=1)  # Ensure binary format

# Step 3: Apply FP-Growth algorithm to find frequent itemsets
frequent_itemsets = fpgrowth(df_one_hot, min_support=0.2, use_colnames=True)

# Step 4: Generate association rules from the frequent itemsets
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

# Display the results
print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nAssociation Rules:")
print(rules)

# Optionally, save the dataset and results to CSV files
df.to_csv('automobile_showroom_sales.csv', index=False)
frequent_itemsets.to_csv('frequent_itemsets.csv', index=False)
rules.to_csv('association_rules.csv', index=False)
