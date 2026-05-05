import pandas as pd
import matplotlib.pyplot as plt

# ==============================================
# 📘 DataFrame 1: Student Grades
# ==============================================
data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}
df1 = pd.DataFrame(data1)

print("\n===== 📘 DataFrame 1: Student Grades =====")

# Exercise 1: Average grade per student
df1["Average"] = df1[["Math", "English", "Science"]].mean(axis=1)
print("\n1️⃣ Average Grade per Student:\n", df1[["Student_ID", "Average"]])

# Exercise 2: Student with highest average
top_student = df1.loc[df1["Average"].idxmax()]
print("\n2️⃣ Student with Highest Average:\n", top_student)

# Exercise 3: Total marks column
df1["Total"] = df1[["Math", "English", "Science"]].sum(axis=1)
print("\n3️⃣ Added Total Marks Column:\n", df1[["Student_ID", "Total"]])

# Exercise 4: Bar chart of average grades per subject
avg_subjects = df1[["Math", "English", "Science"]].mean()
avg_subjects.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title("Average Grades per Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Grade")
plt.show()


# ==============================================
# 💰 DataFrame 2: Sales Data
# ==============================================
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}
df2 = pd.DataFrame(data2)

print("\n===== 💰 DataFrame 2: Sales Data =====")

# Exercise 1: Total sales per product
total_sales = df2[["Product_A", "Product_B", "Product_C"]].sum()
print("\n1️⃣ Total Sales per Product:\n", total_sales)

# Exercise 2: Date with highest total sales
df2["Total_Sales"] = df2[["Product_A", "Product_B", "Product_C"]].sum(axis=1)
max_sales_date = df2.loc[df2["Total_Sales"].idxmax(), "Date"]
print("\n2️⃣ Date with Highest Total Sales:", max_sales_date)

# Exercise 3: % change in sales from previous day
pct_change = df2[["Product_A", "Product_B", "Product_C"]].pct_change() * 100
print("\n3️⃣ Percentage Change in Sales from Previous Day:\n", pct_change)

# Exercise 4: Line chart for sales trends
df2.plot(x="Date", y=["Product_A", "Product_B", "Product_C"], marker='o')
plt.title("Sales Trends Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend(["Product A", "Product B", "Product C"])
plt.show()


# ==============================================
# 👩‍💼 DataFrame 3: Employee Information
# ==============================================
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}
df3 = pd.DataFrame(data3)

print("\n===== 👩‍💼 DataFrame 3: Employee Information =====")

# Exercise 1: Average salary per department
avg_salary_dept = df3.groupby("Department")["Salary"].mean().reset_index()
print("\n1️⃣ Average Salary per Department:\n", avg_salary_dept)

# Exercise 2: Most experienced employee
most_exp = df3.loc[df3["Experience (Years)"].idxmax()]
print("\n2️⃣ Employee with Most Experience:\n", most_exp)

# Exercise 3: Salary increase from minimum
min_salary = df3["Salary"].min()
df3["Salary Increase (%)"] = ((df3["Salary"] - min_salary) / min_salary) * 100
print("\n3️⃣ Salary Increase from Minimum Salary:\n", df3[["Name", "Salary Increase (%)"]])

# Exercise 4: Bar chart of employees per department
dept_count = df3["Department"].value_counts()
dept_count.plot(kind="bar", color="coral")
plt.title("Employee Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.show()


# ==============================================
# 🛒 DataFrame 4: Customer Orders
# ==============================================
data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}
df4 = pd.DataFrame(data4)

print("\n===== 🛒 DataFrame 4: Customer Orders =====")

# Exercise 1: Total revenue
total_revenue = df4["Total_Price"].sum()
print("\n1️⃣ Total Revenue:", total_revenue)

# Exercise 2: Most ordered product
most_ordered = df4["Product"].value_counts().idxmax()
print("\n2️⃣ Most Ordered Product:", most_ordered)

# Exercise 3: Average quantity ordered
avg_quantity = df4["Quantity"].mean()
print("\n3️⃣ Average Quantity Ordered:", round(avg_quantity, 2))

# Exercise 4: Pie chart of sales distribution by product
sales_by_product = df4.groupby("Product")["Total_Price"].sum()
sales_by_product.plot(kind="pie", autopct="%1.1f%%", startangle=90)
plt.title("Sales Distribution by Product")
plt.ylabel("")
plt.show()
