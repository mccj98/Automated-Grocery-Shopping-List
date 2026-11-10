#Use's live, inputted data to generate a more accurate list
#Adapts to past data over time, by identifying if set target quantity < average, if so average is used, possible option for target quantity to be modified in settings menu??? Idea
import pandas as pd
import math
details = pd.read_csv('stock_info.csv', header = 1) #due to dates being in row 1, the default header
def live_list():
    products = []
    averages = []
    suggestions = []
    rows,columns = details.shape #returns num of rows, num of cols
    for i in range(len(details['Product'])): #Populates Array with product names
        products.append(details.iloc[i,0]) 

    for i in range(rows):                                           
           count = 0                                                
           average = 0                                              
           for j in range(3, columns): #start at 3 due to CSV layout
               count+= 1                                            
               average += float(details.iloc[i,j])                  
           if(count != 0 or average != 0): #0/0 not defined 
                if((average/count) <= details['Target Quantity'][i]):
                    averages.append(math.ceil(details['Target Quantity'][i])) #set average to user defined Target Quantity if calculated average is less than this value
                else:            
                    averages.append(average/count) #drops decimal value natively
           else:
               averages.append(-1) #to easily identify error                       

    #for i in range(len(details['Target Quantity'])):
     #if(float(details.iloc[i,1]).isna() == False): #Skips values where the target_quantities entry is empty. .isna() returns true if a number is in the value
      #   target_quantities.append(float(details.iloc[i,1]))    
    print("Please enter the current quantities for the following products:")
    for i in range(len(products)):
        print(products[i])
        current = float(input())
        #if(current <= target_quantities[i]):
        #    suggestions.append(math.ceil((target_quantities[i] - current)))
        #else:
        #    suggestions.append(0)
        suggest = averages[i]-current

        if(suggest <= 0): #deal's with negative suggestions
            suggestions.append(0)
        else:
            suggestions.append(math.ceil(suggest))
        print("Suggested Quantity: ", suggestions[i])
        #REVISIT IDEA OF ADDING A CONDITION WHERE USER IS WARNED IF SUGGESTED VALUE FALLS BELOW THE USER SET TARGET QUANTITY

    print("************")
    print("Shopping List - Based On Current Quantities")
    print("-------------------------------------------")
    for i in range(len(products)):
        if(suggestions[i] != 0):
            print(products[i], " : ", suggestions[i])
    print("***************************")

live_list()
    
   

