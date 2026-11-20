import pandas as pd;
details = pd.read_csv('stock_info.csv');
def edit_data():
    print("")
    print("")
    print("")
    rows, columns = details.shape
    option = int(input()) #enter 1 to delete row / product, 2 to add row / product, 3 to delete week column
    
    if(option == 1):
        product = str(input()).strip().casefold() #lowercase input, don't need .str as this is only needed for Pandas dataframe values so that they can access the string library
        triggered = False;
        for i in range(rows):
            if details['Product'].iloc[i].casefold().strip() == product: #don't need .str as individual value is type string
                details.drop(i,inplace=True)#.drop() deletes a row or column within the DataFrame, not saved to CSV until final writing back to CSV
                print(product + " has been deleted.")
                triggered = True;
                break;
        if(triggered == False):
            print("Row not found")
    details.to_csv('stock_info.csv',index = False); #this position ensures no index gap errors
edit_data()

#.str.strip() - 'strips away' any leading / ending space characters while keeping spaces inbetween words - user input errors
#.str.casefold() - converts all characters to lowercase