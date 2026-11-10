import pandas as pd #note, pandas sees the first row of the csv file as the headers by default, therefore excludes them
import math #math.ceil() represents ceiling rounding - rounding up to the next highest whole number regardless of the size of the decimal value

details = pd.read_csv('stock_info.csv')
#print(details.to_string())
products = []
target_quantities = []
suggestions = []

print(len(details['Product']))
for i in range(len(details['Product'])): #initalises the products list from the values in the CSV
  products.append(details.iloc[i,0]) 
print(products)

for i in range(len(details['Target Quantity'])):
  if(float(details.iloc[i,1]).isna() == False): #Skips values where the target_quantities entry is empty. .isna() returns true if a number is in the value
     target_quantities.append(float(details.iloc[i,1]))
print(target_quantities)


print("************")
print("Please enter the current quantities for the following products:")
for i in range(len(products)):
    print(products[i])
    current = float(input())
    if(current <= target_quantities[i]):
       suggestions.append(math.ceil((target_quantities[i] - current)))
    else:
       suggestions.append(0)
    print("Suggested Quantity: ", suggestions[i])
    print("************")
print("Shopping Suggestions")
for i in range(len(products)):
   if(suggestions[i] != 0):
      print(products[i], " : ", suggestions[i])
    
   
