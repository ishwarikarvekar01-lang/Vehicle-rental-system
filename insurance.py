from fastapi import APIRouter, HTTPException
from database import get_connection

router = APIRouter(prefix="/insurance", tags=["Insurance"])

@router.get("/")
def get_insurance():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM insurance")
    data = cursor.fetchall()
    conn.close()
    return data

@router.get("/{id}")
def get_insurance_by_id(id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM insurance WHERE InsuranceID=%s", (id,))
    data = cursor.fetchone()
    conn.close()

    if not data:
        raise HTTPException(status_code=404, detail="Insurance not found")

    return data

@router.post("/")
def add_insurance(insurance: dict):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO insurance
    (PolicyNumber, Provider, CoverageAmount, ExpiryDate)
    VALUES (%s,%s,%s,%s)
    """

    cursor.execute(sql, tuple(insurance.values()))
    conn.commit()
    conn.close()

    return {"message": "Insurance added successfully"}

@router.put("/{id}")
def update_insurance(id: int, insurance: dict):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE insurance
    SET PolicyNumber=%s,
        Provider=%s,
        CoverageAmount=%s,
        ExpiryDate=%s
    WHERE InsuranceID=%
