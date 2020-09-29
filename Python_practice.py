# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# counties_dict = {'Denver':123, 'Arapahoe':456, 'Jefferson':789}

# for county, num in counties_dict.items():
#     print(county + ' county has '+ str(num) + ' regiestered voters.')

voting_data = [
               {"county" : "Arapahoe", "registered_voters" : 422829}, 
               {"county" : "Denver", "registered_voters" : 463353}, 
               {"county" : "Jefferson", "registered_voters" : 432438}
              ]
    
for countyDict in voting_data:
    #print(countyDict["county"] + "--" + str(countyDict["registered_voters"]))
    print(f'{countyDict["county"]} county has {countyDict["registered_voters"]:,} registered voters.')