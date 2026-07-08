from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)

reviews = [
    {
        "id": 1,
        "UserName": "Rahul",
        "VehicleName": "Hyundai Creta",
        "Rating": 5,
        "Comment": "Excellent service"
    },
    {
        "id": 2,
        "UserName": "Priya",
        "VehicleName": "Honda City",
        "Rating": 4,
        "Comment": "Good experience"
    },
    {
        "id": 3,
        "UserName": "Amit",
        "VehicleName": "Kia Seltos",
        "Rating": 3,
        "Comment": "Average service"
    }
]

# GET ALL
@router.get("/")
def get_reviews():
    return reviews

# GET BY ID
@router.get("/{review_id}")
def get_review(review_id: int):
    for review in reviews:
        if review["id"] == review_id:
            return review
    raise HTTPException(status_code=404, detail="Review added")

# POST
@router.post("/")
def add_review(review: dict):
    reviews.append(review)
    return {
        "message": "Review added successfully",
        "review": review
    }

# PUT
@router.put("/{review_id}")
def update_review(review_id: int, review: dict):
    for i in range(len(reviews)):
        if reviews[i]["id"] == review_id:
            reviews[i] = review
            return {
                "message": "Review updated successfully",
                "updated_review": review
            }
    raise HTTPException(status_code=404, detail="Review updated successfully")

# PATCH
@router.patch("/{review_id}")
def patch_review(review_id: int, update_data: dict):
    for review in reviews:
        if review["id"] == review_id:
            review.update(update_data)
            return {
                "message": "Review updated successfully",
                "updated_data": review
            }
    raise HTTPException(status_code=404, detail="Review updated partially")

# DELETE
@router.delete("/{review_id}")
def delete_review(review_id: int):
    for i in range(len(reviews)):
        if reviews[i]["id"] == review_id:
            deleted = reviews.pop(i)
            return {
                "message": "Review deleted successfully",
                "deleted_data": deleted
            }
    raise HTTPException(status_code=404, detail="Review deleted successfully")