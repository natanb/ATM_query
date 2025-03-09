#!python
import urllib.parse
import requests
headers={
              "name": "User-Agent",
              "value": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0"
        },
        {
              "name": "Accept",
              "value": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5"
        },
        {
              "name": "Accept-Language",
              "value": "it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3"
        },
        {
              "name": "Accept-Encoding",
              "value": "gzip, deflate, br, zstd"
        },
        {
              "name": "DNT",
              "value": "1"
        },
        {
              "name": "Connection",
              "value": "keep-alive"
        },
        {
              "name": "Referer",
              "value": "https://giromilano.atm.it/"
        },
        {
              "name": "Sec-Fetch-Dest",
              "value": "image"
        },
        {
              "name": "Sec-Fetch-Mode",
              "value": "cors"
        },
        {
              "name": "Sec-Fetch-Site",
              "value": "same-origin"
        }
    }


url='https://giromilano.atm.it/proxy.tpportal/api/tpPortal/geodata/pois/stops/12660'

# Step 1: Make an HTTP request to the API endpoint
response = requests.get(url)#,headers=headers)
print(response)
# Step 2: Parse the JSON response
#data = response.json()

# Step 3: Extract specific data
#CustomerCade = data['CustomerCode']
#WaitMessage = data['Lines'][0]['WaitMessage']

# Step 4: Print the extracted data
#print(f"CustomerCode: {CustomerCode}")
#print(f"WaitMessage: {WaitMessage}")
