#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='transshipment_vessels_20180723.csv',mode='█')

#Read the entire contents into a list object
lineList = fileObj.█()

#Release the link to the file objects (now that we have all its contents)
fileObj.█() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = █

#Print the contents of the headerLine
print(█)

#%% Task 4.2

#Split the headerLineString into a list of header items
headerItems = █

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = █
name_idx = █
fleet_idx = █

#Print the values
print(mmsi_idx,name_idx,fleet_idx)

#%% Task 4.3
#Create an empty dictionary
vesselDict = █
#Iterate through all lines (except the header) in the data file:
for █:
#Split the data into values
█
#Extract the mmsi value from the list using the mmsi_idx value
mmsi = █
#Extract the fleet value
fleet = █
#Adds info to the vesselDict dictionary
█

