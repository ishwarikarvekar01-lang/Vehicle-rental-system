from fastapi import APIRouter
from database import get_connection

router=APIRouter(prefix="/payments",tags=["Payments"])

@router.get("/")
def get_payments():
    conn=get_connection()
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM payments")
    data=cursor.fetchall()
    conn.close()
    return data

@router.post("/")
def add_payment(payment:dict):
    conn=get_connection()
    cursor=conn.cursor()
    sql="""INSERT INTO payments(BookingID,PaymentMethod,PaymentDate,Amount,PaymentStatus)
    VALUES(%s,%s,%s,%s,%s)"""
    cursor.execute(sql,tuple(payment.values()))
    conn.commit()
    conn.close()
    return {"message":"Payment added"}

@router.put("/{id}")
def update_payment(id:int,payment:dict):
    conn=get_connection()
    cursor=conn.cursor()
    sql="""UPDATE payments SET BookingID=%s,PaymentMethod=%s,
    PaymentDate=%s,Amount=%s,PaymentStatus=%s
    WHERE PaymentID=%s"""
    cursor.execute(sql,(*payment.values(),id))
    conn.commit()
    conn.close()
    return {"message":"Payment updated"}

@router.delete("/{id}")
def delete_payment(id:int):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM payments WHERE PaymentID=%s",(id,))
    conn.commit()
    conn.close()
    return {"message":"Payment deleted"}
