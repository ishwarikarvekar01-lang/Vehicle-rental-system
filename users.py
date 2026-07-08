from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

users = [
    {
        "id": 1,
        "FullName": "Ishwari Karvekar",
        "Email": "ishwari@gmail.com",
        "Phone": "9876543210",
        "Address": "Goa",
        "Password": "12345",
        "DrivingLicenseNo": "GA12345678",
        "Role": "Customer"
    }
]

# GET ALL
@router.get("/")
def get_users():
    return users

# GET BY ID
@router.get("/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# POST
@router.post("/")
def add_user(user: dict):
    users.append(user)
    return {
        "message": "User added successfully",
        "user": user
    }

# PUT
@router.put("/{user_id}")
def update_user(user_id: int, user: dict):
    for i in range(len(users)):
        if users[i]["id"] == user_id:
            users[i] = user
            return {
                "message": "User updated successfully",
                "user": user
            }
    raise HTTPException(status_code=404, detail="User not found")

# PATCH
@router.patch("/{user_id}")
def patch_user(user_id: int, update_data: dict):
    for user in users:
        if user["id"] == user_id:
            user.update(update_data)
            return {
                "message": "User partially updated",
                "user": user
            }
    raise HTTPException(status_code=404, detail="User not found")

# DELETE
@router.delete("/{user_id}")
def delete_user(user_id: int):
    for i in range(len(users)):
        if users[i]["id"] == user_id:
            deleted = users.pop(i)
            return {
                "message": "User deleted successfully",
                "user": deleted
            }
    raise HTTPException(status_code=404, detail="Deleted")