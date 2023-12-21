#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Customer:
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone
        
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def get_phone(self):
        return self.phone
    
    def set_name(self):
        self.name=name
    def set_email(self):
        self.email=email
    def set_phone(self):
        self.phone=phone
        
    def display_info(self):
        print(f"Name={self.name}")
        print(f"Email={self.email}")
        print(f"Phone={self.phone}")
customer_instance=Customer("Deepa","deepa@gmail.com",1234567876)
customer_instance.display_info()


# In[ ]:




