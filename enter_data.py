import pandas as pd;
details = pd.read_csv('stock_info.csv'); #csv data loaded into Dataframe. use .iloc to access data within Dataframe via integer position
def enter_data():
    rows, columns = details.shape; #returns tuple of details dimensions
    details['Week ' + str(columns - 3)] = 0   #See reasoning below
    print("Make sure that the CSV is closed, else pandas cannot write new entrys to csv")
    print("Enter the quantities of the items that you purchased")
    #columns = to the amount of columns currently present, increment to reach next empty column
    for i in range(rows):
        print(details['Product'].iloc[i]) #.iloc(row), since I have already defined the column as 'Product' column 
        details.iloc[i,columns] = int(input()) #appends chances to the Pandas Dataframe, must append these changes back to CSV at end

        #I was running into an error when i didn't have line 9 - creating a heading row - as python would not allow me to 
        #append values to a column outside the dataframes shape. To get around this, I simply created a new column named 
        #week _ to get around this 

    details.to_csv("stock_info.csv", index=False) #Overide CSV with dataframe values - which includes new column, exclude new index column
    print("Reciept has been appended to CSV successfully.")
enter_data()

    
    
       
