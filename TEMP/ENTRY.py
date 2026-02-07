import os
Folder = "Assets"
File = os.path.join(Folder, "Data.py")
Data = {}
try:
    from Assets.Data import Data as olddata
    Data = olddata
except (ImportError, SyntaxError):
        Data = {}

Index = len(Data)
nEntry = int(input("Input number of new Entries: "))
for x in range(nEntry):
    entry_id = Index + x + 1
    print(f"Entry {entry_id}")
    IMG = input("Enter BG Image File Path: ").lower()
    FONT = input("Enter font name: ").lower()
    NAME = input("Enter Place Heading: ").upper()
    WIKI = input("Enter Wiki Address: ").lower()
    STATE = input("Enter State: ").upper()
    LOCATION = input("Enter location: ").upper()
    YEARLSTED = input("Enter Year Listed: ").upper()
    SINCE = int(input("Since: "))
    AIRPORT = input("Label nearest Airport: ").upper()
    AIRPORT_INFO = input("Enter Airport Website: ").lower()
    RAILWAY = input("Label nearest Railway: ").upper()
    RAILWAY_INFO = input("Enter Railway Website: ").lower()
    VISITHRS = input("Enter Visiting Hours: ").upper()
    HOTEL = input("Enter close hotels: ").upper()
    HOTEL_INFO = input("Enter Hotel Info links: ").lower()
    FEES = input("Enter travelling fees: ")
    DESC = input("Write a description: ")
    PREC = input("Label Precautions, and dangers: ")
    
    conlist = [IMG, FONT, NAME, WIKI, STATE, LOCATION, YEARLSTED, SINCE, AIRPORT, 
               AIRPORT_INFO, RAILWAY, RAILWAY_INFO, VISITHRS, HOTEL, HOTEL_INFO, 
               FEES, DESC, PREC]
    
    Data[entry_id] = conlist
    print("\n\n")
with open(File, "w") as f:
    f.write(f"Data = {repr(Data)}")
