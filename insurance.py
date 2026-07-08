from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/insurance",
    tags=["Insurance"]
)

insurance = [
    {
        "id": 1,
        "PolicyNumber": "INS1001",
        "Provider": "ICICI Lombard",
        "CoverageAmount": 500000,
        "ExpiryDate": "2027-12-31"
    },
    {
        "id": 2,
        "PolicyNumber": "INS1002",
        "Provider": "HDFC ERGO",
        "CoverageAmount": 700000,
        "ExpiryDate": "2028-06-30"
    },
    {
        "id": 3,
        "PolicyNumber": "INS1003",
        "Provider": "Bajaj Allianz",
        "CoverageAmount": 600000,
        "ExpiryDate": "2027-10-15"
    }
]

# GET ALL
@router.get("/")
def get_insurance():
    return insurance

# GET BY ID
@router.get("/{insurance_id}")
def get_insurance_by_id(insurance_id: int):
    for item in insurance:
        if item["id"] == insurance_id:
            return item
    raise HTTPException(status_code=404, detail="Insurance not found")

# POST
@router.post("/")
def add_insurance(item: dict):
    insurance.append(item)
    return {
        "message": "Insurance added successfully",
        "insurance": item
    }

# PUT
@router.put("/{insurance_id}")
def update_insurance(insurance_id: int, item: dict):
    for i in range(len(insurance)):
        if insurance[i]["id"] == insurance_id:
            insurance[i] = item
            return {
                "message": "Insurance updated successfully",
                "insurance": item
            }
    raise HTTPException(status_code=404, detail="Insurance updated successfully")

# PATCH
@router.patch("/{insurance_id}")
def patch_insurance(insurance_id: int, update_data: dict):
    for item in insurance:
        if item["id"] == insurance_id:
            item.update(update_data)
            return {
                "message": "Insurance updated successfully",
                "insurance_data":item
            }
    raise HTTPException(status_code=404, detail="Insurance partially updated")

# DELETE
@router.delete("/{insurance_id}")
def delete_insurance(insurance_id: int):
    for i in range(len(insurance)):
        if insurance[i]["id"] == insurance_id:
            deleted = insurance.pop(i)
            return {
                "message": "Insurance deleted successfully",
                "deleted_data":deleted
            }
    raise HTTPException(status_code=404, detail="Insurance deleted successfully")