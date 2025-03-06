from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
import requests  # For making API requests to fetch bus wait times

class BusApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
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
        
        # Add wait times to the grid layout
        for i, wait_time in enumerate(wait_times, start=1):
            bus_label = Label(text=f"Bus {i}", font_size=18, halign="left", valign="middle")
            time_label = Label(text=f"{wait_time} min", font_size=18, halign="right", valign="middle")
            self.grid_layout.add_widget(bus_label)
            self.grid_layout.add_widget(time_label)
    
    def fetch_bus_wait_times(self):
        # Replace this with your actual API call or logic to fetch wait times
        # For now, we'll simulate 6 wait times
         
        return ATM_query

if __name__ == "__main__":
    BusApp().run()
