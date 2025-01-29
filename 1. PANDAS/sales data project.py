# import the library
import pandas as pd

# read the csv file
sales_data = pd.read_csv(r"C:\Users\lenovo\Desktop\Downloads\employee_data.csv")
print(sales_data)

print('Display 10 rows of first')
print(sales_data.head(10))

print('Display 10 rows of last')
print(sales_data.tail(10))

"""
PROBLEM :-
1- column ?, rows ?
2- what type of ?
3- missing data?
"""

#  info method --> metadata
# 1- number of rows and columns
# 2- column name
# 3- data type
# 4- non null counts
# 5- memory isage of the dataframe

print('Display the info of data set')
print(sales_data.info())


# describe 

print('Descriptive Statistics')
print(sales_data.describe())

"""
1- how big is your dataset
2- what are the  names of columns
"""

print(f'Shape {sales_data.shape}')
print(f'Columns Names:{sales_data.columns}')


# 1- select specific column -->  square brackets
# 2- filter rows --> boolan conditions
# 3- combine multipal coditions

# selecting columns
# 1- a series
# 2 - dataframe multipal columns of data

name = sales_data["first_name"]
print(f"Name(Single Column return Series)\n{name}")

# selecting multipal columns
column = sales_data[["first_name","salary"]]
print(column)

# based on a single comdition
high_salary = sales_data[sales_data['salary'] > 50000]
print(f'Salary greter then 90 Thousand \n {high_salary}')

# combine multipal conditions
filtered_rows = sales_data[(sales_data["salary"]>50000)& (sales_data["salary"]<80000)]
print(f"salry greter then 50 Thousand and less the 80 Thousand \n {filtered_rows} ")

# filtering rows salary > 50K & age > 30
filtered = sales_data[(sales_data["salary"]>50000) & (sales_data["age"]>30)]
print(f"Employee list Age > 30 + Salary > 50000 \n{filtered}")

# using OR condition
filtered_or= sales_data[(sales_data["age"]> 55) | (sales_data["salary"]> 80000)]
print(f"Employee older than 55 OR salary > 80000 \n {filtered_or}")