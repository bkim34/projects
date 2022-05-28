#Broad DSP Engineering takehome
# created by Benjamin Kim on 5/26/22

import requests
#import numPy as np



#question 1

#For this problem I decided to rely on the server API to filter the subway only routes since it makes it simpler to filter 
#through the data, only giving us the data we already want

req = requests.get("https://api-v3.mbta.com/routes?filter[type]=0,1")
#req now stores all the data using requests
line_data = req.json()
#gives us the json response, the data that we want and can now filter out
num_of_longnames = len(line_data['data'])
#return the number of subway routes in the data set

for i in range (num_of_longnames): 
    name = line_data['data'][i]["attributes"]["long_name"]
    print(name)
	
#iterate through number of "long_names", access them and output them to terminal


#question 2

#at first I didnt rely on the server api to filter my results and I got all wrong answers printed out, (commented out below)
#as well as really bad run time, as I filtered through every stop on the site, as well as running an o^n program
#after finding out how to rely on the server api, I just added the id of each subway route to the filter and saved the length in an array



num_stops_arr=[0]*(num_of_longnames)
#set an array for every subway line

for i in range (num_of_longnames):
    route_name= line_data['data'][i]["id"]
    #fetch the subway lines id
    req2 = requests.get("https://api-v3.mbta.com/stops?filter%5Broute%5D="+ route_name)
    stops_data = req2.json()
    #get the data for the subway
    num_stops_arr[i]=len(stops_data['data'])
    #add the number of stops that subway line passes through into its corresponding spot in the array

print ("The subway route with the least stops is " + line_data['data'][num_stops_arr.index(min(num_stops_arr))]["attributes"]["long_name"] +" with " +str(min(num_stops_arr))+ " stops")
print ("The subway route with the most stops is " +line_data['data'][num_stops_arr.index(max(num_stops_arr))]["attributes"]["long_name"] +" with "+ str(max(num_stops_arr))+ " stops")
#print out the lines with the most and least stops



connecting_stops=[]

for i in range (num_of_longnames):
    for j in range (num_of_longnames):
        if (i !=j):# make sure we arent doing the same line
            route_name1= line_data['data'][i]["id"]
            req3 = requests.get("https://api-v3.mbta.com/stops?filter%5Broute%5D="+ route_name1)
            stops_data1 = req3.json()
            route_name2= line_data['data'][j]["id"]
            req4 = requests.get("https://api-v3.mbta.com/stops?filter%5Broute%5D="+ route_name2)
            stops_data2 = req4.json()
            
            for k in range (len(stops_data1['data'])):
                if (stops_data1['data'][k]["attributes"]["name"] in stops_data2):
                    print (stops_data1['data'][k]["attributes"]["name"])
                #create a 2d array with stop name, connectling line 1 and connecting line 2 in each row 


#question 3

#start off by getting destination and location from user
print("enter the station you are at")
location =input()
print("enter the station you would like to go to")
destination = input()

#find locations's line 
for i in range (num_of_longnames):
    route_name= line_data['data'][i]["id"]
    req4 = requests.get("https://api-v3.mbta.com/stops?filter%5Broute%5D="+ route_name)
    stops_data = req4.json()
    if (location in stops_data):
        if (destination in stops_data): #if destination is in the same line, it is complete
            prob3= True
            print(location + " -> " + destination + ", "+ line_data['data'][i]["sattributes"]["long_name"])
        else: #if not, save the line
            location_line = line_data['data'][i]["attributes"]["long_name"]
            break
            route_name_dest= line_data['data'][j]["id"]
            req5 = requests.get("https://api-v3.mbta.com/stops?filter%5Broute%5D="+ route_name)
            stops_data_dest = req5.json()
            if (destination in stops_data_dest['data']):
                print(" you should take " + line_data['data'][i]["attributes"]["long_name"]+ " and transfer to  " +line_data['data'][j]["attributes"]["long_name"] + " to go from " + location + ' to ' + destination)
if (not prob3):
    #find destination's line if problem 3 is not complete
    for i in range (num_of_longnames):
        route_name= line_data['data'][i]["id"]
        req4 = requests.get("https://api-v3.mbta.com/stops?filter%5Broute%5D="+ route_name)
        stops_data = req4.json()
        if (destination in stops_data):
            destination_line = line_data['data'][i]["attributes"]["long_name"]
            break
    
    
#now if we have desitnations line make sure we can use it with the data structure we created above to see if thes lines connect

#if they dont find a way that they connect in the structure above



                


# my approach to this question was to use two arrays, one with the stop name and one with the number of times it appeared in a description
#  
#name_arr=[]
#for i in range (num_of_longnames): 
#    if "Green Line" not in line_data['data'][i]["attributes"]["long_name"]:
#        name_arr.append(line_data['data'][i]["attributes"]["long_name"])
#insert each subway line in an array we will use        
#name_arr.remove("Blue Line")
#name_arr.append("Green Line - (B)")
#name_arr.append("Green Line - (C)")
#name_arr.append("Green Line - (D)")
#name_arr.append("Green Line - (E)")
#name_arr.append("Blue Line")
#unfortunately I have to hard code these since this is how they are displayed in the data set and I am unsure 
#how to put them in with a "- ( )"

#num_stops_arr=[0]*(num_of_longnames)
#set up an array with number of stops for each line

#connecting_stops_arr= []
#set up an array containing connecting stops

#req2 = requests.get("https://api-v3.mbta.com/stops")
#req now stores all the data using requests

#stops_data = req2.json()


#num_stops = len(stops_data['data']) #get the number of stops
#for j in range (num_stops):
#    vehicle_type = stops_data['data'][j]["attributes"]["vehicle_type"]
    #retrive vehicle type which we will then filter to subway only
#    if (vehicle_type==1 or vehicle_type==0): #check if it is a subway
 #       for i in range (num_of_longnames): 
  #          if name_arr[i] in (stops_data['data'][j]["attributes"]["description"]) : #check if the line is in any of the descriptions to add
   #             num_stops_arr[i]=num_stops_arr[i]+1
            #if the name of the stop is in the stop's description, increment it by one since it passes through
            
    #        for k in range ((num_of_longnames)):
     #           if (name_arr[i] not in name_arr[k]) and (name_arr[i] in (stops_data['data'][j]["attributes"]["description"])) and (name_arr[k] in (stops_data['data'][j]["attributes"]["description"])):
      #              connecting_stops_arr.append(['data'][j])

            

#print ("The subway route with the least stops is " + name_arr[num_stops_arr.index(min(num_stops_arr))] +" with " +str(min(num_stops_arr))+ " stops")
#print ("The subway route with the most stops is " +name_arr[num_stops_arr.index(max(num_stops_arr))] +" with "+ str(max(num_stops_arr))+ " stops")
#print ("the stops that connect two or more subway routes are ")
#print (connecting_stops_arr)


