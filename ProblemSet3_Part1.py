# %% PS3: Code Block 1

mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = 20322 

print (f"{mountain}, formerly\nknown as {nickname}\nis {str(elevation)} above sea level.")

# %% Task 2

#Assign variables
dataFolder = "W:\859_data\\tri_state"
dataList = ["roads.shp", "road_types.dbf", "naip_imagery.tif"]
userItem = "streams.shp"

#Add userItem to dataList
dataList.append(userItem)

#Iterate through dataList
for x in dataList:
    print(f"{dataFolder}\{x}")

# %% Task 3

#Make an empty list
userNumbers = []

#Iterate 
for x in range(3) :
    x = input("Enter an integer:")
    userNumbers.append(int(x))

#Sort ascending
userNumbers.sort()
#print highest value
print(f"The highest number is: {userNumbers[-1]}")

# %% Task 3 Challenge

#Make an empty list
userNumbers = []

#Iterate 
for x in range(3) :
    x = input("Enter an integer:")
    userNumbers.append(int(x))

#Sort descending
userNumbers.sort(reverse=True)
#print list
print(userNumbers)