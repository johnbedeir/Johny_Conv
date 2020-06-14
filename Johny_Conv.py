# -*- coding: utf-8 -*-
"""
#Python
#title 		:Converter.py
#description 	:This is a convertor app
#author 	:JohnBedeir
#website	:johnydesigns.com
#date		:14June20
"""
print("""""choose one of the following:
    1. Minutes to Hours
    2. Seconds to Hours
    3. Miles to Km
    4. Km to Miles
    5. Kg to Lbs
    6. Lbs to Kg
    7. Metre to Cm
    8. Cm to Metre
    """"")
ans=input ("Enter your choice: ")

if ans == "1":
    minutes = input ("Enter numebr in minutes: ")
    minutes=float(minutes)  
    hours = minutes / 60
    print("Please type only numbers")
    print (minutes, "minutes are equal to", hours, "hours")

elif ans == "2":
    seconds = input ("Enter numebr in seconds: ")
    seconds=float(seconds)
    hours = seconds / 3600
    print (seconds, "second are equal to", hours, "hours")

elif ans == "3":
    miles = input ("Enter numebr of miles: ")
    miles=float(miles)
    km = miles / 1.6
    print (miles, "miles are equal to", km, "kilometers")

elif ans == "4":
    km = input ("Enter numebr of kilometers: ")
    km=float(km)
    miles = km * 1.6
    print (km, "kilometers are equal to", miles, "miles")

elif ans == "5":
    kg = input ("Enter amount in kilograms: ")
    kg=float(kg)
    lbs = kg * 2.20462
    print (kg, "kilograms are equal to", lbs, "lbs")
    
elif ans == "6":
    lbs = input ("Enter amount in lbs: ")
    lbs=float(lbs)
    kg = lbs / 2.20462
    print (lbs, "lbs are equal to", kg, "kg") 
    
elif ans == "7":
    metre = input ("Enter lenght in metre: ")
    metre=float(metre)
    cm = metre * 100
    print (metre, "metres are equal to", cm, "centimetre")    

elif ans == "8":
    cm = input ("Enter lenght in centimetre: ")
    cm=float(cm)
    metre = cm / 100
    print(cm, "centimetre are equal to", metre, "metres") 

else:
    print ("--- Wrong entry, please choose between 1 to 8 ---")    