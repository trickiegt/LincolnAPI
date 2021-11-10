#Connect and gather vehicle information
import requests

headers = {
    "Host": "phev.myfordmobile.com",
    "Connection": "Keep-Alive",
    "User-Agent": "okhttp/4.9.0",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json; charset=UTF-8",
    }
sessionID = "REDACTED"
data = '{"PARAMS":{"apiLevel":"3","forceUpdate":"1","lastUpdatedTime":"0","sessionId":"%s"}}' % (sessionID)
url = "https://phev.myfordmobile.com/services/webGetAVD"

lincResp = requests.post(url, headers=headers, data=data)
results = lincResp.json()
#print("Full Response: ", results)
print("Name:", results['avdQueryResponse']['customerData']['firstName'])
print("Gas Tank Level:", results['avdQueryResponse']['customerData']['vehicleData']['vehicle']['fuelLevel'],"%")
print("Oil Life:", results['avdQueryResponse']['customerData']['vehicleData']['vehicle']['oilLife'],"%")
print("Odometer:", results['avdQueryResponse']['customerData']['vehicleData']['vehicle']['odometer'])
print("Battery Status:", results['avdQueryResponse']['customerData']['vehicleData']['vehicle']['batteryHealth'])
print("Tire Pressure:", results['avdQueryResponse']['customerData']['vehicleData']['vehicle']['tirePressure'])
print("Vehicle Location:", results['avdQueryResponse']['customerData']['vehicleData']['vehicle']['vehicleLatitude'],",",results['avdQueryResponse']['customerData']['vehicleData']['vehicle']['vehicleLongitude'])

