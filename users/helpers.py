from datetime import timedelta
import datetime
from shangkai import settings
from users.models import User_Cab_Booking, User_Hotel_Booking
from django.core.mail import send_mail

def check_rooms_availaible(cin,cout,hotel_inst,room_inst,rooms):
    hotel_booking = User_Hotel_Booking.objects.filter(
        hotel_id=hotel_inst,
        room_id=room_inst,
        check_in_date__gte=cin,
        check_in_date__lte=cout,
    )
    hotel_booking2 = User_Hotel_Booking.objects.filter(
        hotel_id=hotel_inst,
        room_id=room_inst,
        check_out_date__gte=cin,
        check_out_date__lte=cout,
    )
    hotel_booking3 = User_Hotel_Booking.objects.filter(
        hotel_id=hotel_inst,
        room_id=room_inst,
        check_in_date__lte=cin,
        check_out_date__gte=cout,
    )
    hotel_booking4 = User_Hotel_Booking.objects.filter(
        hotel_id=hotel_inst,
        room_id=room_inst,
        check_in_date__gte=cin,
        check_out_date__lte=cout,
    )
    hotel_booking = hotel_booking.union(hotel_booking2)
    hotel_booking = hotel_booking.union(hotel_booking3)
    hotel_booking = hotel_booking.union(hotel_booking4)            
    if len(hotel_booking) > 0:
        day_count = (cout - cin).days + 1
        for single_date in (cin + timedelta(n) for n in range(day_count)):
            count=0
            for i in range(0, len(hotel_booking)):
                if single_date >= hotel_booking[i].check_in_date and single_date <= hotel_booking[i].check_out_date:
                    count+=hotel_booking[i].rooms
            if int(room_inst.no_rooms) < int(count) + int(rooms):
                return (int(room_inst.no_rooms) - int(count),False)
    return (0,True)

def send_hotel_book_email(name,booking_id,hotel,room,check_in_date,check_out_date,rooms,amount,to):
    subject = "Hotel Booking Confirmation"
    message = f"Dear {name},\n\nYour Hotel Booking has been confirmed.\n\nBooking id: {booking_id}\nHotel Name: {hotel}\nRoom Type: {room}\nCheck In Date: {check_in_date}\nCheck Out Date: {check_out_date}\nRooms: {rooms}\nAmount: Rs {amount}\n\nThank You,\nTeam Shangkai"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [to]
    send_mail(subject, message, email_from, recipient_list)
    
def send_trek_book_email(name,booking_id,trek,start_date,seats,amount,to):
    subject = "Trek Booking Confirmation"
    message = f"Dear {name},\n\nYour Trek Booking has been confirmed.\n\nTrek Name: {trek}\nBooking id: {booking_id}\nStarting on: {start_date}\nSeats: {seats}.\nAmount: Rs {amount}\n\nThank You,\nTeam Shangkai"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [to]
    send_mail(subject, message, email_from, recipient_list)
    
def send_guide_book_email(name,booking_id,guide,package_name,booking_date,no_guests,amount,to):
    subject = "Guide Booking Confirmation"
    message = f"Dear {name},\n\nYour Guide Booking has been confirmed.\n\nGuide Name: {guide}\nPackage Name: {package_name}\nBooking id: {booking_id}\nBooked For: {booking_date}\nNumber of guest: {no_guests}.\nAmount: Rs {amount}\n\nThank You,\nTeam Shangkai"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [to]
    send_mail(subject, message, email_from, recipient_list)
    
def calculate_checkout_date(check_in_date, no_of_days=1):
    check_in_date = datetime.datetime.strptime(check_in_date, "%Y-%m-%d")
    check_out_date =  check_in_date + timedelta(days=no_of_days)
    return check_out_date.strftime("%Y-%m-%d")

def check_cab_avaliability(cin,tin,cout,tout,car_inst):
    qs = User_Cab_Booking.objects.filter(
        car_id = car_inst,
        check_in_date__gte=cin,
        check_out_date__lte=cout,
        check_in_time__gte=tin,
        check_out_time__lte=tout,
    )
    if qs.exists():
        return False
    return True