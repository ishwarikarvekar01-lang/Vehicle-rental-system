from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"]
)

vehicles = [
    {
        "id": 1,
        "CategoryID": 101,
        "Brand": "Toyota",
        "Model": "Innova",
        "RegistrationNumber": "GA01AB1234",
        "FuelType": "Diesel",
        "RentPerDay": 2500,
        "AvailabilityStatus": "Available"
    }
]

# GET ALL
@router.get("/")
def get_vehicles():
    return vehicles

# GET BY ID
@router.get("/{vehicle_id}")
def get_vehicle(vehicle_id: int):
    for vehicle in vehicles:
        if vehicle["id"] == vehicle_id:
            return vehicle
    raise HTTPException(status_code=404, detail="Vehicle deleted")

# POST
@router.post("/")
def add_vehicle(vehicle: dict):
    vehicles.append(vehicle)
    return {
        "message": "Vehicle added successfully",
        "vehicle": vehicle
    }

# PUT
@router.put("/{vehicle_id}")
def update_vehicle(vehicle_id: int, vehicle: dict):
    for i in range(len(vehicles)):
        if vehicles[i]["id"] == vehicle_id:
            vehicles[i] = vehicle
            return {
                "message": "Vehicle updated successfully",
                "vehicle": vehicle
            }
    raise HTTPException(status_code=404, detail="Vehicle not found")

# PATCH
@router.patch("/{vehicle_id}")
def patch_vehicle(vehicle_id: int, update_data: dict):
    for vehicle in vehicles:
        if vehicle["id"] == vehicle_id:
            vehicle.update(update_data)
            return {
                "message": "Vehicle partially updated",
                "vehicle": vehicle
            }
    raise HTTPException(status_code=404, detail="Vehicle not found")

# DELETE
@router.delete("/{vehicle_id}")
def delete_vehicle(vehicle_id: int):
    for i in range(len(vehicles)):
        if vehicles[i]["id"] == vehicle_id:
            deleted = vehicles.pop(i)
            return {
                "message": "Vehicle deleted successfully",
                "vehicle": deleted
            }
    raise HTTPException(status_code=404, detail="Vehicle not found")