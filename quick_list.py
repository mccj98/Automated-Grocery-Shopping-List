import pandas as pd
import math as math
details = pd.read_csv("stock_info.csv") #CSV read directly into DataFrame
def quick_list_pd(): #past data
    products = []
    suggestions = []
    set_targets = []
    rows, columns = details.shape  #returns tuple (num of rows, num of cols), excludes header (not considered data)
    for i in range(len(details['Product'])): #initalises the products list from the values in the CSV, row 0 = headers, rows 1 and below are considered data
      products.append(details.iloc[i,0])
    #for j in range(len(details['Target Quantity'])):    
       #set_targets.append(details.iloc[j])                                                         

    for i in range(rows):
           count = 0  
           average = 0
           for j in range(3, columns): #start at 3 due to CSV layout, calculates average value of row
               count+= 1
               average += float(details.iloc[i,j])
           if(count or average != 0): #0/0 not defined
            if(math.ceil(average/count) >= details['Target Quantity'].iloc[i]):
               suggestions.append(int(math.ceil(average/count)))
            else:
               suggestions.append(int(details['Target Quantity'].iloc[i]))
           else:
              suggestions.append(0)
   
    print("Quick Shopping List - based on past data")                  
    for k in range(len(products)):                 
       if(suggestions[k] != 0):                         
         print(products[k], " : ", suggestions[k])    

quick_list_pd()   
                                                   
