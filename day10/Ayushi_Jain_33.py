# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:19:06 2018

@author: Ayushi
"""
#import MongoClient
from pymongo import MongoClient      

#set up Connection
client = MongoClient('localhost', 27017)

#provide database name
mydb = client.db_University

#insert the data into Collections
def add_client(Student_Name, Student_Age, Student_Roll_no, Student_Branch):
    unique_client = mydb.University_clients.find_one({"Student Roll_no":Student_Roll_no}, {"_id":0})
    if unique_client:
        return "Client already exists"
    else:
        mydb.University_clients.insert(
                {
                "Student Name" : Student_Name,
                "Student Age" : Student_Age,
                "Student Roll_no" : Student_Roll_no,
                "Student Branch" : Student_Branch
                
                })
        return "Client added successfully"

#Read data
for i in range(0,10):
    

    Student_Name = input("Enter Student Name: ")
    Student_Age = input("Enter Student Age: ")
    Student_Roll_no = input("Enter Student roll no: ")
    Student_Branch = input("Enter Student Branch: ")
    
    print(add_client(Student_Name, Student_Age, Student_Roll_no, Student_Branch))


