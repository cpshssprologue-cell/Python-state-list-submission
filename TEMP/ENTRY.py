Data = {}
for x in range(20):
    print(x+1)
    IMG = input("Enter BG Image File Path: ").lower()
    FONT = input("Enter font name: ").lower()
    NAME = input("Enter Place Heading: ").upper()
    WIKI = input("Enter Wiki Address: ").lower()
    STATE = input("Enter State: ").upper()
    LOCATION = input("Enter location: ").upper()
    YEARLSTED = int(input("Enter Year Listed: "))
    SINCE = int(input("Since: "))
    AIRPORT = input("Label nearest Airport: ").upper()
    AIRPORT_INFO = input("Enter Airport Website: ").lower()
    RAILWAY = input("Label nearest Railway: ").upper()
    RAILWAY_INFO = input("Enter Railway Website: ").lower()
    VISITHRS = input("Enter Visiting Hours: ").upper()
    HOTEL = input("Enter close hotels: ").upper()
    HOTEL_INFO = input("Enter Hotel Info links: ").lower()
    FEES = int(input("Enter travelling fees: "))
    DESC = input("Write a description: ")
    PREC = input("Label Precautions, and dangers: ")
    Conlist = [IMG, FONT, NAME, WIKI, STATE, LOCATION, YEARLSTED, SINCE, AIRPORT, AIRPORT_INFO, RAILWAY, RAILWAY_INFO, VISITHRS, HOTEL, HOTEL_INFO, FEES, DESC]
    Data[(x+1)] = Conlist
    print("\n\n\n")
