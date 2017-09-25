#Importing packages
from __future__ import print_function
import sys
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

#Collecting console inputs
if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python  show_bus_locations_jtl417.py <MTA_KEY> <BUS_LINE>")


key = sys.argv[1]
line = sys.argv[2]

#Loading url into json data
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + \
    "&VehicleMonitoringDetailLevel=calls&LineRef=" + line
print(url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

#Creating variable storing location of vehicle activity data
vehicleActivity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

#Getting count of buses
bus_count = len(vehicleActivity)

#Finding name of the line
line_name = vehicleActivity[0]['MonitoredVehicleJourney']['PublishedLineName']

#Printing bus count and line name
print("Bus Line: " + line_name)
print("Number of active buses: " + str(bus_count))

#Finding and printing lat long for each bus
for i in range(bus_count):
    lat = vehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    long = vehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print("Bus " + str(i) + " is at latitude " + str(lat) + " and longitude " + str(long))
