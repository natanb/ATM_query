import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
import requests  # For making API requests to fetch bus wait times
#import q_atm_param as q

class BusApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=5, spacing=5)
        
        # Title Label
        self.title_label = Label(text="Bus Wait Times", font_size=24, size_hint=(1, 0.1))
        self.layout.add_widget(self.title_label)
        
        # Grid Layout to display wait times
        self.grid_layout = GridLayout(cols=2, spacing=10, size_hint=(1, 0.6))
        self.layout.add_widget(self.grid_layout)
        
        # Update Button
        self.update_button = Button(text="Update Wait Times", size_hint=(1, 0.1))
        self.update_button.bind(on_press=self.update_wait_times)
        self.layout.add_widget(self.update_button)
        
        # Fetch initial wait times
        self.update_wait_times()
        
        return self.layout
    
    def update_wait_times(self, *args):
        # Fetch wait times from API
        wait_times = self.fetch_bus_wait_times()
        
        # Clear the grid layout before adding new data
        self.grid_layout.clear_widgets()
        
        lines=["45 FACCHINETTI","93 ARGONNE","93 GORINI","45 GOLGI","45 MURANI"] 
        # Add wait times to the grid layout
        for  i in range(len(wait_times)):
            bus_label = Label(text=f"{lines[i]}", font_size=26, halign="left", valign="middle")
            time_label = Label(text=f"{wait_times[i]}", font_size=26, halign="right", valign="middle")
            self.grid_layout.add_widget(bus_label)
            self.grid_layout.add_widget(time_label)
    
    def fetch_bus_wait_times(self):
        # Replace this with your actual API call or logic to fetch wait times
        # For now, we'll simulate 6 wait times

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
        wait_time=["0","0","0","0","0"]
        j=0
        lines=["18475","20072","12446","12465","12463"]
        for l in lines:
            linea=l
            response = requests.get(
            'https://giromilano.atm.it/proxy.tpportal/api/tpPortal/geodata/pois/stops/'+linea,
            cookies=cookies,
            headers=headers,
            )

            data = response.json()

# Step 3: Extract specific data
#            LineDescription = data['Lines'][0]['Line']['LineDescription']
#            CustomerCode = data['CustomerCode']
            WaitMessage = data['Lines'][0]['WaitMessage']
#            Address = data['Address']
#            LineCode = data['Lines'][0]['Line']['LineCode']
            wait_time[j]=WaitMessage
            j+=1

# Step 4: Print the extracted data
#            print(f"CustomerCode: {CustomerCode}")
#            print(f"Line: {LineCode}")
#            print(f"Address: {Address}")
#            print(f"WaitMessage: {WaitMessage}")
#            print(f"LineDescription: {LineDescription}")
        return wait_time


if __name__ == "__main__":
    BusApp().run()
