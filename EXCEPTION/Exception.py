#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class EventNotFoundException(Exception):
    def __init__(self, message="Invalid Event"):
        self.message = message
        super().__init__(self.message)
        
class InvalidBookingIdException(Exception):
    def __init__(self, message="Invalid Booking ID"):
        self.message = message
        super().__init__(self.message)

class NullPointerException(Exception):
    def __init__(self, message="Invalid"):
        self.message = message
        super().__init__(self.message)

