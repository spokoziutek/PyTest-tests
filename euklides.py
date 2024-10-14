# Algorytm Euklidesa
# Stworzyć funkcję zwracającą największy wspólny dzielnik dwóch liczb naturalnych,
# obliczoną algorytmem Euklidesa. Należy przygotować testy sprawdzające poprawność rezultatu zwracanego przez funkcję.


def euklides(a, b):
    
    if not isinstance(a, (int)):
        raise ValueError("Use only numbers")
    
    if not isinstance(b, (int)):
        raise ValueError("Use only numbers")
    
    while b:
        a, b = b, a % b
    return a

def test():
    assert euklides(12, 6) == 6
    assert euklides(100, 10) == 10
    
def testOneZero():
    assert euklides(0, 5) == 5
    assert euklides(5, 0) == 5
    
def testTwoZeros():
    assert euklides(0, 0) == 0
    
def testIncorrectTypeA():
    try:
        euklides("ala", 8)
    except ValueError as e:
        assert str(e) == "Use only numbers"
    else:
        assert False
        
def testIncorrectTypeB():
    try:
        euklides(8, "kot")
    except ValueError as e:
        assert str(e) == "Use only numbers"
    else:
        assert False
        
    

test()
testOneZero()
testTwoZeros()
testIncorrectTypeA()
testIncorrectTypeB()
