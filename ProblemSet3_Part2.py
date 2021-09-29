#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='transshipment_vessels_20180723.csv',mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Print the contents of the headerLine
print(headerLineString)

#%% Task 4.2

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(",")

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = headerItems.index('mmsi')
name_idx = headerItems.index('shipname')
fleet_idx = headerItems.index('fleet_name')

#Print the values
print(mmsi_idx,name_idx,fleet_idx)

#%% Task 4.3
#Create an empty dictionary
vesselDict = {}

#Iterate through all lines (except the header) in the data file:
for line in lineList[1:]:
    #Split the data into values
    lineData = line.split(',')
    #Extract the mmsi value from the list using the mmsi_idx value
    mmsi = lineData[mmsi_idx]
    #Extract the fleet value
    fleet = lineData[fleet_idx]
    #Adds info to the vesselDict dictionary
    vesselDict[mmsi]=fleet

#%% Task 4.4
#Assign Vessel ID variable
vesselID = '258799000' 

#Look up vessel ID in vessel dictionary
vesselFleet = vesselDict[vesselID]

#print statement
print(f"Vessel # {vesselID} flies the flag of {vesselFleet}")

#%% Task 5

#Reads file into variable
loit_file_obj = open(file='loitering_events_20180723.csv',mode='r')

#Read the entire contents into a list object
loit_line_list = loit_file_obj.readlines()

#Release the link to the file objects 
loit_file_obj.close() 

#Empty dictionaries for latitudes and long
mmsi_lat = {}
mmsi_long = {}

#Iterate through lines
for line in loit_line_list[1]:
    #split string into a list of data items
    loit_data = line.split(",")
    #assign variables
    mmsi =  loit_data[0]  
    starting_lat = loit_data[1]  
    ending_lat = loit_data[3]
    starting_long = loit_data[2]
    #add to mmsi latitude dictionary 
    mmsi_lat[mmsi]= (starting_lat, ending_lat)
    #add to mmsi longitude dictionary
    mmsi_long[mmsi]= starting_long
 
#Create empty list for equator crossing keys
keys_equator_crossing = []
#Assess starting and ending latitude for equator crossing
for mmsi_item in mmsi_lat.items():
    #get the coordinates
    mmsi, coordinates = mmsi_item
    starting_lat, ending_lat = coordinates
    #see if crosses equator, if starting lat starts with a - and the ending lat doesn't, it should cross equator
    if starting_lat[0] == "-" and ending_lat[0] != "-":
        keys_equator_crossing.append(mmsi)

#Create empty list for keys matching longitude criteria
keys_long_criteria = []
#Assess starting and ending latitude for equator crossing
for mmsi_long_item in mmsi_long.items():
    #get the coordinates
    mmsi, starting_long = mmsi_long_item
    int_long = float(starting_long)
    #see if qualifies longitude criteria
    if 165< int_long <170:
        keys_long_criteria.append(mmsi)
        
#Convert criteria key lists into sets
equator_set = set(keys_equator_crossing)
long_set = set(keys_long_criteria)
#Create list from intersection
matching_keys = list(equator_set.intersection(long_set))

#If no records found, tell user
if len(matching_keys) == 0:
    print ("No Records Found")
    
#Pull from vessel dict using matching keys
for matching_key in matching_keys:
    vesselID = matching_key
    vesselFleet = vesselDict[matching_key]
    print(f"Vessel # {vesselID} flies the flag of {vesselFleet}")
    

