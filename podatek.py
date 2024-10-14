# Obliczenie podatku dochodowego
# Stworzyć funkcję obliczającą kwotę podatku dochodowego dla dochodu przekazanego w parametrze income. 
# Podatek ma być obliczony według skali podatkowej. Należy przygotować testy sprawdzające poprawność rezultatów zwracanych przez funkcje. Przyjmujemy skalę podatkową:
#
#  - dochód <= 120 000 - 12%
#  - dochód > 120 000 - 32% od nadwyżki + obliczony podatek z I progu
#  Kwota wolna od podatku: 30 000

def calculateTax(income):
    
    if not isinstance(income, (int, float)):
        raise ValueError("Income must be a number")
    
    taxFreeIncome = 30000
    
    lowerTax = 120000
    
    taxable_income = max(0, income - taxFreeIncome)
    
    if taxable_income <= lowerTax - taxFreeIncome:
        tax = taxable_income * 0.12
    else:
        lower_tax = (lowerTax - taxFreeIncome) * 0.12
        upper_tax = (taxable_income - (lowerTax - taxFreeIncome)) * 0.32
        tax = lower_tax + upper_tax
        
    return tax


def testCalculateIncomeTax():
    assert calculateTax(20000) == 0
    assert calculateTax(30000) == 0
    assert calculateTax(0) == 0
    assert calculateTax(120000) == 10800
    assert calculateTax(-100000) == 0

def testIncorrecType():
    try:
        calculateTax("ala ma kota")
    except ValueError as e:
        assert str(e) == "Income must be a number"
    else:
        assert False
        

testCalculateIncomeTax()
testIncorrecType()