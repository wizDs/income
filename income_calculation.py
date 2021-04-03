from tkinter import *

def entry_str_to_float(entry: Entry) -> int:
    return float(entry.get())

def income_post_tax(income: Entry, labor_market_tax_rate: Entry, municipality_tax_rate: Entry, tax_deduction: Entry):

    income = entry_str_to_float(income)
    labor_market_tax_rate = entry_str_to_float(labor_market_tax_rate) / 100
    municipality_tax_rate = entry_str_to_float(municipality_tax_rate) / 100
    tax_deduction = entry_str_to_float(tax_deduction)

    taxable_income = income - tax_deduction

    return taxable_income * (1-labor_market_tax_rate) * (1-municipality_tax_rate) + tax_deduction


window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

# indkomst
income_lbl = Label(window, text="Indkomst")
income_lbl.grid(column=1, row=0)
income = Entry(window,width=10)
income.grid(column=2, row=0)

# arbejdsmarkedsbidrag
labor_market_tax_rate_lbl = Label(window, text="%-vis arbejdsmarkedsbidrag")
labor_market_tax_rate_lbl.grid(column=1, row=1)
labor_market_tax_rate = Entry(window,width=10)
labor_market_tax_rate.grid(column=2, row=1)

# kommuneskat
municipality_tax_rate_lbl = Label(window, text="%-vis kommuneskat")
municipality_tax_rate_lbl.grid(column=1, row=2)
municipality_tax_rate = Entry(window,width=10)
municipality_tax_rate.grid(column=2, row=2)

# Fradrag
tax_deduction_lbl = Label(window, text="Fradrag i kr.")
tax_deduction_lbl.grid(column=1, row=3)
tax_deduction = Entry(window,width=10)
tax_deduction.grid(column=2, row=3)

space_blank = Label(window, text="")
space_blank.grid(column=1, row=4)

output_lbl = Label(window, text="Indkomst efter skat")
output_lbl.grid(column=1, row=5)
output = Label(window, text="")
output.grid(column=2, row=5)

def clicked():

    output.configure(text=income_post_tax(income, labor_market_tax_rate, municipality_tax_rate, tax_deduction))

btn = Button(window, text="Udregn", command=clicked)
btn.grid(column=3, row=5)

window.mainloop()

