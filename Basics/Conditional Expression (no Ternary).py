# Python has no ternary operator & instead uses "conditional expressions"

# Sales tax rate value depends on taxable status

taxable = True
sales_tax_rate = 0.065 if taxable else 0
print(sales_tax_rate)