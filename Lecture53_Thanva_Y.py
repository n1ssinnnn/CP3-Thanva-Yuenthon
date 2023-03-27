priceInput = int(input())

def vatCalculator(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result
print(vatCalculator(priceInput))