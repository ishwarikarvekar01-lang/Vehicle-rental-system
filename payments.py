from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

payments = [
    {
        "id": 1,
        "BookingID": 1,
        "PaymentMethod": "Credit Card",
        "Amount": 5000,
        "PaymentStatus": "Paid"
    },
    {
        "id": 2,
        "BookingID": 2,
        "PaymentMethod": "UPI",
        "Amount": 3500,
        "PaymentStatus": "Pending"
    },
    {
        "id": 3,
        "BookingID": 3,
        "PaymentMethod": "Cash",
        "Amount": 4200,
        "PaymentStatus": "Paid"
    }
]

# GET ALL
@router.get("/")
def get_payments():
    return payments

# GET BY ID
@router.get("/{payment_id}")
def get_payment(payment_id: int):
    for payment in payments:
        if payment["id"] == payment_id:
            return payment
    raise HTTPException(status_code=404, detail="Payment not found")

# POST
@router.post("/")
def add_payment(payment: dict):
    payments.append(payment)
    return {
        "message": "Payment added successfully",
        "payment": payment
    }

# PUT
@router.put("/{payment_id}")
def update_payment(payment_id: int, payment: dict):
    for i in range(len(payments)):
        if payments[i]["id"] == payment_id:
            payments[i] = payment
            return {
                "message": "Payment updated successfully",
                "payment": payment
            }
    raise HTTPException(status_code=404, detail="Payment updated successfully")

# PATCH
@router.patch("/{payment_id}")
def patch_payment(payment_id: int, update_data: dict):
    for payment in payments:
        if payment["id"] == payment_id:
            payment.update(update_data)
            return {
                "message": "Payment partially updated",
                "payment": payment
            }
    raise HTTPException(status_code=404, detail="Payment updated partially")

# DELETE
@router.delete("/{payment_id}")
def delete_payment(payment_id: int):
    for i in range(len(payments)):
        if payments[i]["id"] == payment_id:
            deleted = payments.pop(i)
            return {
                "message": "Payment deleted successfully",
                "payment": deleted
            }
    raise HTTPException(status_code=404, detail="Payment deleted successfully")