# Assigment 1 ,2nd question
tax_rate = 0.20
standard_reduction = 10000
dependent_reduction = 3000
gross_income = float(input("Enter your total income"))
number_of_dependent = int(input("Enter total number of dependant"))
taxeable_income = gross_income - standard_reduction - dependent_reduction*number_of_dependent
income_tax = taxeable_income*tax_rate
print("The income tax is $"+str(income_tax))
