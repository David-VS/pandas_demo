import pandas as pd

##########
##Inputs##
##########
categories = []
amounts = []
is_inputing = True

while is_inputing:
    user_input = input("Add an item? (Y)es:")
    if user_input == "Y":
        category = input("Category:")
        amount = float(input("Amount:"))
        categories.append(category)
        amounts.append(amount)
    else:
        is_inputing = False

#############
##To Excell##
#############
data = {
    "category":categories,
    "amount":amounts
}

data_frame = pd.DataFrame(data)
data_frame.to_excel('data/costs.xlsx', sheet_name="overview", index=False)

#########
##Stats##
#########
print(data_frame["amount"].max())
print(data_frame["amount"].mean())
print(data_frame.groupby("category").mean())
print(data_frame.groupby("category").sum())