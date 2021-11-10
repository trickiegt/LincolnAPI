#Send Command to Cancel Remote Start
import requests
import json
import time

vin = "REDACTED"
sessionID = "REDACTED"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Host": "phev.myfordmobile.com",
    "Connection": "Keep-Alive",
    "User-Agent": "okhttp/4.9.0",
    "Content-Type": "application/json; charset=UTF-8",
    }
data = {
    "PARAMS":{
        "apiLevel":"3",
        "LOOKUPCODE":"CANCEL_START_CMD",
        "VIN": vin,
        "SESSIONID": sessionID
        }
    }
body = json.dumps(data)
lincResp = requests.put("https://phev.myfordmobile.com/services/webAddCommandPS", headers=headers, data=body)
results = lincResp.json()
#print("Full Response -- ", results)
print("Cancel Remote Start Command ID is:", results['COMMANDID'])

commandID = results['COMMANDID']
data = {
    "PARAMS":{
        "COMMANDID": commandID,
        "SESSIONID": sessionID
        }
    }
body = json.dumps(data)
complete = False
while complete == False:
    time.sleep(5)
    lincResp = requests.put("https://phev.myfordmobile.com/services/webGetRemoteCommandStatusPS", headers=headers, data=body)
    results = lincResp.json()
    #print("Full Response -- ", results)
    print("Command Status:", results['Entries']['Entry']['status'])
    if results['Entries']['Entry']['status'] != "QUEUED":
        if results['Entries']['Entry']['status'] == "COMPLETED":
            print("Cancel Start Command Executed Successfully")    
            complete = True
        else:
            print("Cancel Start Command Failed -", results['Entries']['Entry']['status'])    
            complete = True