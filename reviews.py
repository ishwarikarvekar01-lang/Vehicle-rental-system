from fastapi import APIRouter, HTTPException
from database import get_connection

router = APIRouter(prefix="/reviews", tags=["Reviews"])

@router.get("/")
def get_reviews():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM reviews")
    data = cursor.fetchall()
    conn.close()
    return data

@router.get("/{id}")
def get_review(id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM reviews WHERE ReviewID=%s", (id,))
    data = cursor.fetchone()
    conn.close()

    if not data:
        raise HTTPException(status_code=404, detail="Review not found")

    return data

@router.post("/")
def add_review(review: dict):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO reviews
    (UserID, VehicleID, Rating, Comment, ReviewDate)
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(sql, tuple(review.values()))
    conn.commit()
    conn.close()

    return {"message": "Review added successfully"}

@router.put("/{id}")
def update_review(id: int, review: dict):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE reviews
    SET UserID=%s,
        VehicleID=%s,
        Rating=%s,
        Comment=%s,
        ReviewDate=%s
    WHERE ReviewID=%s
    """

    cursor.execute(sql, (*review.values(), id))
    conn.commit()
    conn.close()

    return {"message": "Review updated successfully"}

@router.delete("/{id}")
def delete_review(id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM reviews WHERE ReviewID=%s", (id,))
    conn.commit()
    conn.close()

    return {"message": "Review deleted successfully"}
