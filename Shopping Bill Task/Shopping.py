
def calculateElectronicsGST(a, b):
    return (a + b) * 1.18

def calculateFashionGST(c, d):
    return (c + d) * 1.13

def calculateFoodGST(e):
    return e * 1.07

def totalBill(a, b, c, d, e):
    return (calculateElectronicsGST(a, b)
            + calculateFashionGST(c, d)
            + calculateFoodGST(e))

def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 0.20
    return total - discount


a = 100
b = 100
c = 100
d = 100
e = 100

total = totalBill(a, b, c, d, e)
discount = total * 0.20
final_amount = calculateDiscountedBill(a, b, c, d, e)

print(f"Total after GST = {total:.2f}")
print(f"Discount = {discount:.2f}")
print(f"Final payable amount = {final_amount:.2f}")
