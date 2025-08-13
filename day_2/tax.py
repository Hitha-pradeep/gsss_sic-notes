Name=input("Enter your name: ")
EmpID=input("Enter your Employee ID: ")
Basic_Monthly_Salary=float(input("Enter your Basic Salary: "))
Special_Allowances = float(input("Enter your Special Allowances: "))
Annual_Bonus = Basic_Monthly_Salary * 0.12
print("Annual Bonus is:", Annual_Bonus)
Gross_monthly_Salary = Basic_Monthly_Salary + Special_Allowances 
print("Gross Monthly Salary is:", Gross_monthly_Salary)
Gross_Annual_Salary = (Basic_Monthly_Salary + Special_Allowances) * 12 + Annual_Bonus
print("Gross Annual Salary is:", Gross_Annual_Salary)