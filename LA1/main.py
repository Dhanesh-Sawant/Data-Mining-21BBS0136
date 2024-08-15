import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('employee_data.csv')

# print("printing the shape of dataframe of dataset ", df.shape)
# print("printing the structure of dataframe of dataset ", df.info())
# print("printing all the attribute names of dataframe of dataset ", df.columns)
# print("printing all the attribute values of dataframe of dataset ")
# print(df.describe())

# print("Displaying the first 5 records")
# print(df.head())

# print("Displaying the last 5 records")
# print(df.tail())

# print("printing the name, designation and salary of top 10 employees")
# print(df[['Name', 'Designation', 'Salary']].head(10))

# print("printing the name of all the records")
# print(df['Name'])

# print("printing all the records")
# print(df)

# print("printing the mean of the dataframe")
# print(df[['Salary','Experience']].mean())
# print("printing the median of the dataframe")
# print(df[['Salary','Experience']].median())
# print("printing the mode of the dataframe")
# print(df[['Salary','Experience']].mode())

# print("\nMode of Vaccinated:")
# print(df['Vaccinated'].mode())

# # Variance of Salary and Experience
# print("Variance of Salary and Experience:")
# print(df[['Salary', 'Experience']].var())

# # Covariance between Salary and Experience
# print("\nCovariance between Salary and Experience:")
# print(df[['Salary', 'Experience']].cov())

# # Correlation between Salary and Experience
# print("Correlation between Salary and Experience:")
# print(df['Salary'].corr(df['Experience']))


# Pie chart of Designation
designation_counts = df['Designation'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(designation_counts, labels=designation_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart of Employee Designations')
plt.show()


# Histogram of Salary
plt.figure(figsize=(10, 6))
sns.histplot(df['Salary'], bins=10, kde=False)
plt.title('Histogram of Employee Salaries')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# Scatter plot of Salary to Experience
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Experience', y='Salary', data=df)
plt.title('Scatter Plot of Salary vs. Experience')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary')
plt.show()