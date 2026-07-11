from fastapi import APIRouter
from database import get_connection

router=APIRouter(prefix="/rentallocations",tags=["Rental Locations"])

@router.get("/")
def get_locations():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM rentallocations")
    data=cursor.fetchall()
    conn.close()
    return data

@router.post("/")
def add_location(location:dict):
    conn=get_connection()
    cursor=conn.cursor()
    sql="INSERT INTO rentallocations(LocationName,City,State,Pincode) VALUES(%s,%s,%s,%s)"
    cursor.execute(sql,tuple(location.values()))
    conn.commit()
    conn.close()
    return {"message":"Location added"}

@router.put("/{id}")
def update_location(id:int,location:dict):
    conn=get_connection()
    cursor=conn.cursor()
    sql="UPDATE rentallocations SET LocationName=%s,City=%s,State=%s,Pincode=%s WHERE LocationID=%s"
    cursor.execute(sql,(*location.values(),id))
    conn.commit()
    conn.close()
    return {"message":"Location updated"}

@router.delete("/{id}")
def delete_location(id:int):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM rentallocations WHERE LocationID=%s",(id,))
    conn.commit()
    conn.close()
    return {"message":"Location deleted"}
