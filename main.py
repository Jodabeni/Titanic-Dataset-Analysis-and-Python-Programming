
import pandas as pd


df = pd.read_csv('titanic.csv')

#a. ppl traveling to Minneapolis
Destinations = df["home.dest"]
minneapolis_empty = 0 # initialize 0
for Des_rows in Destinations.values:
    if Des_rows.__contains__("minneapolis, MN"):
       minneapolis_empty =  minneapolis_empty + 1

print('The total number of people traveling to  minneapolis', minneapolis_empty)
#b Which fare was bought the most?

fares = df["fare"] # set equal to fare column
mostshows = {} #dictionary , the keys are unique
for fare in fares:
    if fare in mostshows.keys():
        mostshows[fare] += 1
    else:
        mostshows[fare] = 1
#5.Whichever key appears the most, return it
print(" Which fare was bought the most?", max(mostshows, key=mostshows.get))

#c) What is the highest paid fare?
print("What is the highest paid fare?", max(mostshows))# max() shows which one appears the most in the dictionary

# d) List all the females that survived the crash.
female_survived = (df["sex"] == "female") & (df["survived"] == 1)
female_survived_count = female_survived.sum()
print(' The total number of female survivers are : ' , female_survived_count)


# e) List all the survivors that did not have cabin information.
survived = (df["survived"] == 1) & (df["cabin"]== "?")
survived_count = survived.sum()
print(' The total number of people without cabin information is  : ' , survived_count)


# f) Display the number of survivors and non-survivors for each passenger class.

classes = df["pclass"].unique() # Finds all classes from 0 to infinity
# Looping through each passenger class and count survivors and non-survivors
for pclass in classes:
    # Count survivors
    survivors = df[(df["pclass"] == pclass) & (df["survived"] == 1)].shape[0]
    # Count non-survivors
    non_survivors = df[(df["pclass"] == pclass) & (df["survived"] == 0)].shape[0]
    # Print the results for this class
    print(f"For passenger class {pclass}:")
    print(f"  Survivors: {survivors}")
    print(f"  Non-survivors: {non_survivors}")



















