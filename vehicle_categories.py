from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/vehicle_categories",
    tags=["Vehicle Categories"]
)

vehicle_categories = [
    {
        "id": 1,
        "CategoryName": "Car",
        "SeatingCapacity": 5,
        "Description": "Comfortable family car"
    },
    {
        "id": 2,
        "CategoryName": "Bike",
        "SeatingCapacity": 2,
        "Description": "Two wheeler for city travel"
    },
    {
        "id": 3,
        "CategoryName": "SUV",
        "SeatingCapacity": 7,
        "Description": "Spacious sports utility vehicle"
    }
]

# GET ALL
@router.get("/")
def get_vehicle_categories():
    return vehicle_categories

# GET BY ID
@router.get("/{category_id}")
def get_vehicle_category(category_id: int):
    for category in vehicle_categories:
        if category["id"] == category_id:
            return category
    raise HTTPException(status_code=404, detail="Vehicle Category not found")

# POST
@router.post("/")
def add_vehicle_category(category: dict):
    vehicle_categories.append(category)
    return {
        "message": "Vehicle Category added successfully",
        "vehicle_category": category
    }

# PUT
@router.put("/{category_id}")
def update_vehicle_category(category_id: int, category: dict):
    for i in range(len(vehicle_categories)):
        if vehicle_categories[i]["id"] == category_id:
            vehicle_categories[i] = category
            return {
                "message": "Vehicle Category updated successfully",
                "vehicle_category": category
            }
    raise HTTPException(status_code=404, detail="Vehicle Category not found")

# PATCH
@router.patch("/{category_id}")
def patch_vehicle_category(category_id: int, update_data: dict):
    for category in vehicle_categories:
        if category["id"] == category_id:
            category.update(update_data)
            return {
                "message": "Vehicle Category partially updated",
                "vehicle_category": category
            }
    raise HTTPException(status_code=404, detail="Updated Partially")

# DELETE
@router.delete("/{category_id}")
def delete_vehicle_category(category_id: int):
    for i in range(len(vehicle_categories)):
        if vehicle_categories[i]["id"] == category_id:
            deleted = vehicle_categories.pop(i)
            return {
                "message": "Vehicle Category deleted successfully",
                "vehicle_category": deleted
            }
    raise HTTPException(status_code=404, detail="Vehicle deleted successfully")