from __future__ import print_function
import sys
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python  get_bus_info_jtl417.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")

key = sys.argv[1]
line = sys.argv[2]
file = sys.argv[3]

fout = open(file, "w")
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + key + \
    "&VehicleMonitoringDetailLevel=calls&LineRef=" + line
print(url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

vehicleActivity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
bus_count = len(vehicleActivity)

for i in range(bus_count):
    lat = str(vehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    long = str(vehicleActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    if not vehicleActivity[i]['MonitoredVehicleJourney']['OnwardCalls']:
        stop = 'N/A'
        status = 'N/A'
    else:
        stop = str(vehicleActivity[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
        status = str(vehicleActivity[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions'] \
                 ['Distances']['PresentableDistance'])
    output = (lat + "," + long + ',' + stop + ',' + status + "\n")
    fout.write(output)