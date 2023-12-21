#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import date, time, datetime
from enum import Enum
class EventType(Enum):
    Movie = 'Movie'
    Sports = 'Sports'
    Concert = 'Concert'
class Event:
    def __init__(self,event_name,event_date,event_time,venue_name,total_seats,ticket_price,event_type):
        self.event_name=event_name
        self.event_date=event_date
        self.event_time=event_time
        self.venue_name=venue_name
        self.total_seats=total_seats
        self.available_seats=total_seats
        self.ticket_price=ticket_price
        self.event_type=EventType(event_type)
        self.booked_tickets = 0
        
    def get_event_name(self):
        return self.event_name
    def get_event_date(self):
        return self.event_date
    def get_event_time(self):
        return self.event_time
    def get_venue_name(self):
        return self.venue_name
    def get_total_seats(self):
        return self.total_seats
    def get_available_seats(self):
        return self.available_seats
    def get_ticket_price(self):
        return self.ticket_price
    def get_event_type(self):
        return self.event_type
    
    def set_event_name(self):
        self.event_name=event_name
    def set_event_date(self):
        self.event_date=event_date
    def set_event_time(self):
        self.event_time=event_time
    def set_venue_name(self):
        self.venue_name=venue_name
    def set_total_seats(self):
        self.total_seats=total_seats
        self.available_seats=total_seats 
    def set_available_seats(self):
        self.available_seats=available_seats
    def set_ticket_price(self):
        self.ticket_price=ticket_price
    def set_event_type(self):
        self.event_type=EventType(event_type)
        
    def calculate_tot_revenue(self,tickets_sold):
        if tickets_sold<=self.available_seats:
            revenue=tickets_sold*self.ticket_price
            self.available_seats-=tickets_sold
            self.booked_tickets +=tickets_sold
            return revenue
        else:
            print("Error.")
            return 0
    def getBookedTickets(self):
        return self.booked_tickets
    
    def book_tickets(self,num_tickets):
        if num_tickets<=self.available_seats:
            self.available_seats-=num_tickets
            self.booked_tickets+=num_tickets
            print(f"{num_tickets} tickets booked successfully.")
        else:
            print("Not enough available seats")
            
    def cancel_booking(self,num_tickets):
        if num_tickets<=self.booked_tickets:
            self.available_seats+=num_tickets
            self.booked_tickets-=num_tickets
            print(f"{num_tickets} tickets canceled successfully.")
        
    def display_info(self):
        print(f"Event Name:{self.event_name}")
        print(f"Event Date:{self.event_date}")
        print(f"Event Time:{self.event_time}")
        print(f"Venue Name:{self.venue_name}")
        print(f"Total Seats:{self.total_seats}")
        print(f"Ticket Price:{self.ticket_price}")
        print(f"Event Type:{self.event_type.value}")
event_instance=Event("Dance",'2023-12-10','02:00',"Pacific hall",150,100,"Concert")
total_revenue = event_instance.calculate_tot_revenue(10)
event_instance.display_info()
event_instance.cancel_booking(2)
print(f"Total revenue={total_revenue }")
print(f"No Of Tickets Booked={event_instance.getBookedTickets()}")

