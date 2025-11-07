"""
- пользователь может пересмотреь список отелей,
- ользователь может забронировать отель,
- пользователь может получить подтверждение бронирования или билет(ticket),
  как бы вы не назвали это, после чего, как он забронировал отель
"""

## Hotel, User, ReservationTicket

# class User:
#    def view_hotels(self):
#         pass 

import pandas as pd


class Hotel:
    def __init__(self, hotel_id,):
        self.hotel_id = hotel_id




    def booking(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_obj):
        self.customer_name = customer_name
        self.hotel_obj = hotel_obj

    def generate(self):
        pass

df = pd.read_csv("hotel.csv")
print(df)

hotel_id = input("Enter the ID of the hotel")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.booking()
    customer_name = input("Enter you name: ")
    reservation_ticket = ReservationTicket(
        customer_name=customer_name, 
        hotel_obj=hotel,)
    reservation_ticket.generate()
else:
    print("Sorry, the hotel is not available for booking...")