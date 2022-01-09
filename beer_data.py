# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np

beerConversion = {3:"Rolling Rock",
                   11:"Montucky Cold Snacks",
                   10:"Miller High Life",
                   6:"Raineer",
                   1:"Kokanee",
                   5:"PBR",
                   4:"Coors Banquet",
                   12:"Hamm's",
                   8:"Modelo",
                   2:"10 Barrel Pub Beer (craft control)",
                   7:"Tecate",
                   9:"Budweiser"}

Ryan =  [2,11,12,1,6,3,5,4,7,9,8,10]
Betsy = [3,10,11,1,5,4,6,8,2,7,12,9]
David = [3,10,11,8,7,12,5,6,2,4,1,9]
Shay =  [4,11,2,8,10,6,5,12,1,9,7,3]
Madie = [12,11,1,7,2,8,5,4,3,10,9,6]

# Create a data frame from the beer data
def sort_by_beer(ranker):
    rank = list(range(1,13))
    ranker, rank = zip(*sorted(zip(ranker, rank)))
    return rank
    
d = {"Beer number":list(range(1,13)),
        "Ryan's Rank":  sort_by_beer(Ryan),
        "Betsy's Rank": sort_by_beer(Betsy),
        "David's Rank": sort_by_beer(David),
        "Shay's Rank":  sort_by_beer(Shay),
        "Madie's Rank": sort_by_beer(Madie)}

data = pd.DataFrame(data=d)
data.index = range(1,len(data)+1) #reindex to correlate beer names

beerNames = pd.Series(beerConversion).sort_index()
data['Beer names'] = beerNames
data = data[['Beer names',"Ryan's Rank","Betsy's Rank","David's Rank","Madie's Rank","Shay's Rank"]].set_index(["Beer names"])
dataFlipped = data.transpose()
#dataFlipped = data.set_index(["Beer names"]).transpose()
mean = dataFlipped.mean()

print("\nAverage Score for each Beer")
print(dataFlipped.mean())
print("\nStandard Deviation for each Beer")
print(dataFlipped.std())

# determine each persons devation from each beer
dev = data.subtract(mean,axis='index').abs().mean()
print("\nDevation")
print(dev)
