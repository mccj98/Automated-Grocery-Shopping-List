import pandas as pd
details = pd.read_csv("stock_info.csv", header = 1) #CSV read directly into DatFrame
def quick_list_pd(): #past data
    products = []
    suggestions = []
    rows, columns = details.shape  #returns tuple (num of rows, num of cols), excludes header (not considered data)
    for i in range(len(details['Product'])): #initalises the products list from the values in the CSV, row 0 = headers, rows 1 and below are considered data
      products.append(details.iloc[i,0])                                                             

    for i in range(rows):
           count = 0  
           average = 0
           for j in range(3, columns): #start at 3 due to CSV layout
               count+= 1
               average += float(details.iloc[i,j])
           if(count or average != 0): #0/0 not defined
            suggestions.append(average/count)
   
    print("Quick Shopping List - based on past data")                  
    for k in range(len(products)):                 
       if(suggestions[k] != 0):                         
         print(products[k], " : ", suggestions[i])    

quick_list_pd()   
                                                   
