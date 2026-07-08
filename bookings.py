from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)

bookings = [
    {
        "id": 1,
        "UserID": 101,
        "VehicleID": 201,
        "BookingDate": "2026-07-01",
        "StartDate": "2026-07-02",
        "EndDate": "2026-07-05",
        "Status": "Confirmed"
    },
    {
        "id": 2,
        "UserID": 102,
        "VehicleID": 202,
        "BookingDate": "2026-07-03",
        "StartDate": "2026-07-04",
        "EndDate": "2026-07-06",
        "Status": "Pending"
    },
    {
        "id": 3,
        "UserID": 103,
        "VehicleID": 203,
        "BookingDate": "2026-07-05",
        "StartDate": "2026-07-06",
        "EndDate": "2026-07-10",
        "Status": "Completed"
    }
]

# GET ALL
@router.get("/")
def get_bookings():
    return bookings

# GET BY ID
@router.get("/{booking_id}")
def get_booking(booking_id: int):
    for booking in bookings:
        if booking["id"] == booking_id:
            return booking
    raise HTTPException(status_code=404, detail="Booking not found")

# POST
@router.post("/")
def add_booking(booking: dict):
    bookings.append(booking)
    return {
        "message": "Booking added successfully",
        "booking": booking
    }

# PUT
@router.put("/{booking_id}")
def update_booking(booking_id: int, booking: dict):
    for i in range(len(bookings)):
        if bookings[i]["id"] == booking_id:
            bookings[i] = booking
            return {
                "message": "Booking updated successfully",
                "booking": booking
            }
    raise HTTPException(status_code=404, detail="Booking not found")

# PATCH
@router.patch("/{booking_id}")
def patch_booking(booking_id: int, update_data: dict):
    for booking in bookings:
        if booking["id"] == booking_id:
            booking.update(update_data)
            return {
                "message": "Booking partially updated",
                "booking": booking
            }
    raise HTTPException(status_code=404, detail="Booking partially added")

# DELETE
@router.delete("/{booking_id}")
def delete_booking(booking_id: int):
    for i in range(len(bookings)):
        if bookings[i]["id"] == booking_id:
            deleted = bookings.pop(i)
            return {
                "message": "Booking deleted successfully",
                "booking": deleted
            }
    raise HTTPException(status_code=404, detail="Booking deleted successfully")