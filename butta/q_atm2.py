import requests

cookies = {
    '_ga': 'GA1.1.2037073293.1738697629',
    '_gid': 'GA1.1.1857438754.1738697629',
    '_ga': 'GA1.1.2037073293.1738697629',
    '_ga_RD7BG8RLV0': 'GS1.1.1738697628.1.0.1738697628.0.0.0',
    '_gat': '1',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '_ga=GA1.1.2037073293.1738697629; _gid=GA1.1.1857438754.1738697629; _ga=GA1.1.2037073293.1738697629; _ga_RD7BG8RLV0=GS1.1.1738697628.1.0.1738697628.0.0.0; _gat=1',
    'dnt': '1',
    'priority': 'u=1, i',
    'referer': 'https://giromilano.atm.it/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://giromilano.atm.it/proxy.tpportal/api/tpPortal/geodata/pois/stops/18475',
    cookies=cookies,
    headers=headers,
)
#print(response)



data = response.json()

# Step 3: Extract specific data
CustomerCode = data['CustomerCode']
WaitMessage = data['Lines'][0]['WaitMessage']
Address = data['Address']
LineDescription = data['Lines'][0]['Line']['LineDescription']
LineCode = data['Lines'][0]['Line']['LineCode']
# Step 4: Print the extracted data
print(f"CustomerCode: {CustomerCode}")
print(f"WaitMessage: {WaitMessage}")
print(f"Address: {Address}")
print(f"LineDescription: {LineDescription}")
print(f"Line: {LineCode}")
