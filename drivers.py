from fastapi import APIRouter
from database import get_connection

router=APIRouter(prefix="/drivers",tags=["Drivers"])

@router.get("/")
def get_drivers():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM drivers")
    data=cursor.fetchall()
    conn.close()
    return data

@router.post("/")
def add_driver(driver:dict):
    conn=get_connection()
    cursor=conn.cursor()
    sql="""INSERT INTO drivers(DriverName,Phone,LicenseNumber,Experience,AvailabilityStatus)
    VALUES(%s,%s,%s,%s,%s)"""
    cursor.execute(sql,tuple(driver.values()))
    conn.commit()
    conn.close()
    return {"message":"Driver added"}

@router.put("/{id}")
def update_driver(id:int,driver:dict):
    conn=get_connection()
    cursor=conn.cursor()
    sql="""UPDATE drivers SET DriverName=%s,Phone=%s,
    LicenseNumber=%s,Experience=%s,
    AvailabilityStatus=%s WHERE DriverID=%s"""
    cursor.execute(sql,(*driver.values(),id))
    conn.commit()
    conn.close()
    return {"message":"Driver updated"}

@router.delete("/{id}")
def delete_driver(id:int):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM drivers WHERE DriverID=%s",(id,))
    conn.commit()
    conn.close()
    return {"message":"Driver deleted"}
