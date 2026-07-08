from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/vehicle_maintenance",
    tags=["Vehicle Maintenance"]
)

vehicle_maintenance = [
    {
        "id": 1,
        "VehicleID": 201,
        "ServiceDate": "2026-07-01",
        "ServiceType": "Oil Change",
        "Cost": 2500,
        "Status": "Completed"
    },
    {
        "id": 2,
        "VehicleID": 202,
        "ServiceDate": "2026-07-10",
        "ServiceType": "Brake Service",
        "Cost": 4500,
        "Status": "Pending"
    },
    {
        "id": 3,
        "VehicleID": 203,
        "ServiceDate": "2026-07-15",
        "ServiceType": "Engine Check",
        "Cost": 6000,
        "Status": "Completed"
    }
]

# GET ALL
@router.get("/")
def get_vehicle_maintenance():
    return vehicle_maintenance

# GET BY ID
@router.get("/{maintenance_id}")
def get_maintenance(maintenance_id: int):
    for maintenance in vehicle_maintenance:
        if maintenance["id"] == maintenance_id:
            return maintenance
    raise HTTPException(status_code=404, detail="Maintenance record not found")

# POST
@router.post("/")
def add_maintenance(maintenance: dict):
    vehicle_maintenance.append(maintenance)
    return {
        "message": "Maintenance record added successfully",
        "maintenance": maintenance
    }

# PUT
@router.put("/{maintenance_id}")
def update_maintenance(maintenance_id: int, maintenance: dict):
    for i in range(len(vehicle_maintenance)):
        if vehicle_maintenance[i]["id"] == maintenance_id:
            vehicle_maintenance[i] = maintenance
            return {
                "message": "Maintenance record updated successfully",
                "maintenance": maintenance
            }
    raise HTTPException(status_code=404, detail="Maintenance record updated successfully")

# PATCH
@router.patch("/{maintenance_id}")
def patch_maintenance(maintenance_id: int, update_data: dict):
    for maintenance in vehicle_maintenance:
        if maintenance["id"] == maintenance_id:
            maintenance.update(update_data)
            return {
                "message": "Maintenance record partially updated",
                "maintenance": maintenance
            }
    raise HTTPException(status_code=404, detail="Maintenance record partially updated")

# DELETE
@router.delete("/{maintenance_id}")
def delete_maintenance(maintenance_id: int):
    for i in range(len(vehicle_maintenance)):
        if vehicle_maintenance[i]["id"] == maintenance_id:
            deleted = vehicle_maintenance.pop(i)
            return {
                "message": "Maintenance record deleted successfully",
                "delated_data": deleted
            }
    raise HTTPException(status_code=404, detail="Maintenance record deleted successfully")