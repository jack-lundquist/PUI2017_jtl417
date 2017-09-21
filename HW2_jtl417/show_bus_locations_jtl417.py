from __future__ import print_function
import sys
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python  show_bus_locations_jtl417.py <MTA_KEY> <BUS_LINE>")


key = sys.argv[1]
line = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + \
    "&VehicleMonitoringDetailLevel=calls&LineRef=" + line
print(url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

vehicleActivity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
bus_count = len(vehicleActivity)
line_name = vehicleActivity[0]['MonitoredVehicleJourney']['PublishedLineName']
print("Bus Line: " + line_name)
print("Number of active buses: " + str(bus_count))
for i in range(bus_count):
    lat = vehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    long = vehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print("Bus " + str(i) + " is at latitude " + str(lat) + " and longitude " + str(long))