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

#Save the contents of the first line
header_line_String = loit_line_list[0]


#Split the headerLineString into a list of header items
header_items = header_line_String.split(",")

#List the index of the mmsi, shipname, and fleet_name values
mmsiIdx = header_items.index('transshipment_mmsi')
starting_lat_idx = header_items.index('starting_latitude')
starting_long_idx = header_items.index('starting_longitude')
ending_lat_idx = header_items.index("ending_latitude")

#Create empty list for mmsis that match criteria 
matching_mmsi=[]

#Iterate through lines
for line in loit_line_list[1:]: #will iterate through lines, skipping first header line
    #split string into a list of data items
    loit_data = line.split(",")
    #assign variables
    mmsi =  loit_data[mmsiIdx]  
    starting_lat = loit_data[starting_lat_idx]  
    ending_lat = loit_data[ending_lat_idx]
    starting_long = loit_data[starting_long_idx]
    #If the vessel meets all the requirements, add MMSI to a list
    if starting_lat[0]=="-" and ending_lat[0]!= "-" and 165< float(starting_long) <170:
       matching_mmsi.append(mmsi)

#If no records found, tell user
if len(matching_mmsi) == 0:
    print ("No Records Found")
    
#Print vessels that match criteria
for key in matching_mmsi:
    vesselID = key
    vesselFleet = vesselDict[key] #uses matching key to pull vessel fleet number from task 4
    print(f"Vessel # {vesselID} flies the flag of {vesselFleet}")       



    

