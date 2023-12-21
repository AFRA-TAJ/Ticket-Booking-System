#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mysql-connector-python


# In[4]:


import mysql.connector as sql
conn=sql.connect(host='localhost',database='Ticket_booking',user='root',password='Af#ra_02!')#connecting with database
if conn.is_connected:
    print("Database is connected ")
    
stmt=conn.cursor()
create_str='''
create table if not exists customer
(
name varchar(50),
email varchar(50),
phone varchar(50)
)
'''
stmt.execute(create_str)

stamt=conn.cursor()
creat_str='''
create table if not exists venue
(
venue_name varchar(50),
address varchar(50)
)
'''
stamt.execute(creat_str)

statmt=conn.cursor()
crete_str='''
create table if not exists event
(
event_name varchar(50),
event_date date,
event_time time,
venue_name varchar(50),
total_seats int,
ticket_price int,
event_type varchar(50)
)
'''
statmt.execute(crete_str)

create_insert='''
insert into customer values("Deepa","deepa@gmail.com",1234567876)
'''
stmt=conn.cursor()
stmt.execute(create_insert)
conn.commit()
print('Inserted Successfully')

create_insert='''
insert into venue values("Arabian hall","123 mainst city")
'''
stmt=conn.cursor()
stmt.execute(create_insert)
conn.commit()
print('Inserted Successfully')

create_insert='''
insert into event values("Dance",'2023-12-10','02:00',"Pacific hall",150,100,"Concert")
'''
stmt=conn.cursor()
stmt.execute(create_insert)
conn.commit()
print('Inserted Successfully')


# In[ ]:




