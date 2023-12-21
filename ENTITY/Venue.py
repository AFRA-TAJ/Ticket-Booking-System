#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class venue:
    def __init__(self,venue_name,address):
        self.venue_name=venue_name
        self.address=address
        
    def get_venue_name(self):
        return self.venue_name
    def get_address(self):
        return self.address
    
    def set_venue_name(self):
        self.venue_name=venue_name
    def set_address(self):
        self.address=address
        
    def display_info(self):
        print(f"Venue Name={self.venue_name}")
        print(f"Address={self.address}")
venue_instance=venue("Arabian hall","123 mainst city")
venue_instance.display_info()

