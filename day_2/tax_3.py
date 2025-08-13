import tax,tax_2
Section_87A_rebate=True
if tax.Gross_Annual_Salary>0 and  tax.Gross_Annual_Salary>300000:
    print("Taxable Income is:", tax_2.Taxable_income)
elif tax.Gross_Annual_Salary>600000:
    print("Taxable Income is:", tax_2.Taxable_income * 0.05)
elif tax.Gross_Annual_Salary>900000:
    print("Taxable Income is:", tax_2.Taxable_income * 0.10)
elif tax.Gross_Annual_Salary>1200000:
    print("Taxable Income is:", tax_2.Taxable_income * 0.15)
elif  tax.Gross_Annual_Salary>1500000:
    print("Taxable Income is:", tax_2.Taxable_income * 0.20)
else:
    print("Taxable Income is:", tax_2.Taxable_income * 0.30)

cess_amount = tax_2.Taxable_income * 0.04
print("Cess Amount is:", cess_amount)
if Section_87A_rebate and tax_2.Taxable_income <= 700000:
    print("Section 87A Rebate is applicable, no tax payable.")
else:
    total_tax = tax_2.Taxable_income + cess_amount
    print("Total Tax Payable is:", total_tax)

