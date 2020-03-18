
# j)Write a function that converts a dictionary into a list,
# where each element represents a key-value pair.

'''def dictToList(dictionary):
    temp=[]
    dictList=[]

    for key,value in dictionary.items():
        temp=[key,value]
        dictList.append(temp)
    return dictList

newList=dictToList({"name":"Sekina","age":"34"})
print(newList)'''

def profit(inventoryDict):
    inventory=inventoryDict["inventory"]
    costPrice=inventoryDict["cost_price"]
    sellPrice=inventoryDict[  "sell_price"]

    bp=inventory*costPrice
    sp=inventory*sellPrice

    actualProfit=sp-bp

    return actualProfit


actualProfit=profit({"cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200})
print(actualProfit)


