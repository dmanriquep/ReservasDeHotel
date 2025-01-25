import asyncio
from hotel_management.reservations import Reservation, ReservationSystem
from hotel_management.customers import Customer, CustomerManagement
from hotel_management.rooms import Room, RoomManagement
from hotel_management.payments import process_payment
from datetime import datetime

async def main():
    reservation_system = ReservationSystem()
    customer_mgmt = CustomerManagement()
    room_mgmt = RoomManagement()

    room_mgmt.add_room(Room(101, "Habitación Sencilla", 100))
    room_mgmt.add_room(Room(102, "Habitación Doble", 150))

    customer1 = Customer(1, "Ana", "ana@dominio.com")
    customer_mgmt.add_customer(customer1)

    customer2 = Customer(2, "Roberto", "roberto@dominio.com")
    customer_mgmt.add_customer(customer2)

    if room_mgmt.check_availability(101):
        reservation = Reservation(1, "Ana", 101, datetime.now(), datetime.now())
        reservation_system.add_reservation(reservation)

        await process_payment("Ana", 100)

    if room_mgmt.check_availability(102):
        reservation = Reservation(2, "Roberto", 102, datetime.now(), datetime.now())
        reservation_system.add_reservation(reservation)

        await process_payment("Roberto", 150)

if __name__ == "__main__":
    asyncio.run(main())

