from fastapi import APIRouter
from database import get_connection

router=APIRouter(prefix="/vehiclemaintenance",tags=["Vehicle Maintenance"])

@router.get("/")
def get_maintenance():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehiclemaintenance")
    data=cursor.fetchall()
    conn.close()
    return data

@router.post("/")
def add_maintenance(maintenance:dict):
    conn=get_connection()
    cursor=conn.cursor()
    sql="""INSERT INTO vehiclemaintenance(VehicleID,ServiceDate,ServiceType,Cost,NextServiceDate)
    VALUES(%s,%s,%s,%s,%s)"""
    cursor.execute(sql,tuple(maintenance.values()))
    conn.commit()
    conn.close()
    return {"message":"Maintenance added"}

@router.put("/{id}")
def update_maintenance(id:int,maintenance:dict):
    conn=get_connection()
    cursor=conn.cursor()
    sql="""UPDATE vehiclemaintenance SET VehicleID=%s,ServiceDate=%s,
    ServiceType=%s,Cost=%s,NextServiceDate=%s
    WHERE MaintenanceID=%s"""
    cursor.execute(sql,(*maintenance.values(),id))
    conn.commit()
    conn.close()
    return {"message":"Maintenance updated"}

@router.delete("/{id}")
def delete_maintenance(id:int):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM vehiclemaintenance WHERE MaintenanceID=%s",(id,))
    conn.commit()
    conn.close()
    return {"message":"Maintenance deleted"}
