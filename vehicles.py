from fastapi import APIRouter, HTTPException
from database import get_connection

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

@router.get("/")
def get_vehicles():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehicles")
    data = cursor.fetchall()
    conn.close()
    return data

@router.get("/{id}")
def get_vehicle(id:int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehicles WHERE VehicleID=%s",(id,))
    data = cursor.fetchone()
    conn.close()
    if not data:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return data

@router.post("/")
def add_vehicle(vehicle:dict):
    conn=get_connection()
    cursor=conn.cursor()
    sql="""INSERT INTO vehicles(CategoryID,Brand,Model,RegistrationNumber,FuelType,RentPerDay,AvailabilityStatus)
    VALUES(%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql,tuple(vehicle.values()))
    conn.commit()
    conn.close()
    return {"message":"Vehicle added"}

@router.put("/{id}")
def update_vehicle(id:int,vehicle:dict):
    conn=get_connection()
    cursor=conn.cursor()
    sql="""UPDATE vehicles SET CategoryID=%s,Brand=%s,Model=%s,
    RegistrationNumber=%s,FuelType=%s,RentPerDay=%s,
    AvailabilityStatus=%s WHERE VehicleID=%s"""
    cursor.execute(sql,(*vehicle.values(),id))
    conn.commit()
    conn.close()
    return {"message":"Vehicle updated"}

@router.delete("/{id}")
def delete_vehicle(id:int):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM vehicles WHERE VehicleID=%s",(id,))
    conn.commit()
    conn.close()
    return {"message":"Vehicle deleted"}
