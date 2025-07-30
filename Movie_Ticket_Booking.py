def seats_booked(booked,seat_num,total):
    if seat_num<1 or seat_num>total:
        print("Invalid seat number")
    elif seat_num in booked:
        print(f"{seat_num} already booked")
    else:
        booked.append(seat_num)
def seats_cancle(booked,seat_num):
    if seat_num in booked:
        booked.remove(seat_num)
    else:
        print(f"{seat_num} is not booked")
def available_seats(total,booked):
    return [seat for seat in range(1, total + 1) if seat not in booked]
total_seats = 10
booked_seats = [2, 5, 7]
book_seat = 3
cancel_seat = 5
seats_booked(booked_seats,book_seat,total_seats)
seats_cancle(booked_seats,cancel_seat)
print(f"Available seats:{available_seats(total_seats,booked_seats)}")
