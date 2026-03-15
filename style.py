def calculateTotalPrice(itemprice,TaxRate):
 total=itemprice+itemprice*TaxRate
 if(total>100):print("Large order")
 return total
