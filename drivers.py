from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/drivers",
    tags=["Drivers"]
)

drivers = [
    {
        "id": 1,
        "DriverName": "Ramesh Kumar",
        "LicenseNumber": "DL123456",
        "Phone": "9876543210",
        "Experience": 5
    },
    {
        "id": 2,
        "DriverName": "Suresh Patil",
        "LicenseNumber": "DL654321",
        "Phone": "9876501234",
        "Experience": 8
    },
    {
        "id": 3,
        "DriverName": "Mahesh Sharma",
        "LicenseNumber": "DL987654",
        "Phone": "9876512345",
        "Experience": 3
    }
]

# GET ALL
@router.get("/")
def get_drivers():
    return drivers

# GET BY ID
@router.get("/{driver_id}")
def get_driver(driver_id: int):
    for driver in drivers:
        if driver["id"] == driver_id:
            return driver
    raise HTTPException(status_code=404, detail="Driver not found")

# POST
@router.post("/")
def add_driver(driver: dict):
    drivers.append(driver)
    return {
        "message": "Driver added successfully",
        "driver": driver
    }

# PUT
@router.put("/{driver_id}")
def update_driver(driver_id: int, driver: dict):
    for i in range(len(drivers)):
        if drivers[i]["id"] == driver_id:
            drivers[i] = driver
            return {
                "message": "Driver updated successfully",
                "driver": driver
            }
    raise HTTPException(status_code=404, detail="Driver added successfully")

# PATCH
@router.patch("/{driver_id}")
def patch_driver(driver_id: int, update_data: dict):
    for driver in drivers:
        if driver["id"] == driver_id:
            driver.update(update_data)
            return {
                "message": "Driver partially updated",
                "driver": driver
            }
    raise HTTPException(status_code=404, detail="Driver partially updated")

# DELETE
@router.delete("/{driver_id}")
def delete_driver(driver_id: int):
    for i in range(len(drivers)):
        if drivers[i]["id"] == driver_id:
            deleted = drivers.pop(i)
            return {
                "message": "Driver deleted successfully",
                "driver": deleted
            }
    raise HTTPException(status_code=404, detail="Driver deleted successfully")