from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/rental_locations",
    tags=["Rental Locations"]
)

rental_locations = [
    {
        "id": 1,
        "LocationName": "Panaji Branch",
        "City": "Panaji",
        "State": "Goa",
        "Pincode": "403001"
    },
    {
        "id": 2,
        "LocationName": "Margao Branch",
        "City": "Margao",
        "State": "Goa",
        "Pincode": "403601"
    },
    {
        "id": 3,
        "LocationName": "Mapusa Branch",
        "City": "Mapusa",
        "State": "Goa",
        "Pincode": "403507"
    }
]

# GET ALL
@router.get("/")
def get_rental_locations():
    return rental_locations

# GET BY ID
@router.get("/{location_id}")
def get_rental_location(location_id: int):
    for location in rental_locations:
        if location["id"] == location_id:
            return location
    raise HTTPException(status_code=404, detail="Rental Location not found")

# POST
@router.post("/")
def add_rental_location(location: dict):
    rental_locations.append(location)
    return {
        "message": "Rental Location added successfully",
        "rental_location": location
    }

# PUT
@router.put("/{location_id}")
def update_rental_location(location_id: int, location: dict):
    for i in range(len(rental_locations)):
        if rental_locations[i]["id"] == location_id:
            rental_locations[i] = location
            return {
                "message": "Rental Location updated successfully",
                "rental_location": location
            }
    raise HTTPException(status_code=404, detail="Rental Location updated successfully")

# PATCH
@router.patch("/{location_id}")
def patch_rental_location(location_id: int, update_data: dict):
    for location in rental_locations:
        if location["id"] == location_id:
            location.update(update_data)
            return {
                "message": "Rental Location partially updated",
                "updated_data": location
            }
    raise HTTPException(status_code=404, detail="Rental Location partially updated")

# DELETE
@router.delete("/{location_id}")
def delete_rental_location(location_id: int):
    for i in range(len(rental_locations)):
        if rental_locations[i]["id"] == location_id:
            deleted = rental_locations.pop(i)
            return {
                "message": "Rental Location deleted successfully",
                "deleted_data": deleted
            }
    raise HTTPException(status_code=404, detail="Rental Location deleted successfully")