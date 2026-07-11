from fastapi import APIRouter
from database import get_connection

router=APIRouter(prefix="/bookings",tags=["Bookings"])

@router.get("/")
def get_bookings():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM bookings")
    data=cursor.fetchall()
    conn.close()
    return data

@router.post("/")
def add_booking(booking:dict):
    conn=get_connection()
    cursor=conn.cursor()
    sql="""INSERT INTO bookings(UserID,VehicleID,PickupDate,ReturnDate,TotalAmount,BookingStatus)
    VALUES(%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql,tuple(booking.values()))
    conn.commit()
    conn.close()
    return {"message":"Booking added"}

@router.put("/{id}")
def update_booking(id:int,booking:dict):
    conn=get_connection()
    cursor=conn.cursor()
    sql="""UPDATE bookings SET UserID=%s,VehicleID=%s,PickupDate=%s,
    ReturnDate=%s,TotalAmount=%s,BookingStatus=%s WHERE BookingID=%s"""
    cursor.execute(sql,(*booking.values(),id))
    conn.commit()
    conn.close()
    return {"message":"Booking updated"}

@router.delete("/{id}")
def delete_booking(id:int):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM bookings WHERE BookingID=%s",(id,))
    conn.commit()
    conn.close()
    return {"message":"Booking deleted"}
