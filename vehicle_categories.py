from fastapi import APIRouter
from database import get_connection

router=APIRouter(prefix="/vehiclecategories",tags=["Vehicle Categories"])

@router.get("/")
def get_categories():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehiclecategories")
    data=cursor.fetchall()
    conn.close()
    return data

@router.post("/")
def add_category(category:dict):
    conn=get_connection()
    cursor=conn.cursor()
    sql="INSERT INTO vehiclecategories(CategoryName,SeatingCapacity,Description) VALUES(%s,%s,%s)"
    cursor.execute(sql,tuple(category.values()))
    conn.commit()
    conn.close()
    return {"message":"Category added"}

@router.put("/{id}")
def update_category(id:int,category:dict):
    conn=get_connection()
    cursor=conn.cursor()
    sql="UPDATE vehiclecategories SET CategoryName=%s,SeatingCapacity=%s,Description=%s WHERE CategoryID=%s"
    cursor.execute(sql,(*category.values(),id))
    conn.commit()
    conn.close()
    return {"message":"Category updated"}

@router.delete("/{id}")
def delete_category(id:int):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM vehiclecategories WHERE CategoryID=%s",(id,))
    conn.commit()
    conn.close()
    return {"message":"Category deleted"}
