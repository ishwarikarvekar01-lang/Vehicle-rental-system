from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GET ALL USERS
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.Users).all()


# GET USER BY ID
@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.UserID == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# ADD USER
@router.post("/")
def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.Users(
        FullName=user.FullName,
        Email=user.Email,
        Phone=user.Phone,
        Address=user.Address,
        Password=user.Password,
        DrivingLicenseNo=user.DrivingLicenseNo,
        Role=user.Role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User added successfully",
        "user": new_user
    }


# UPDATE USER (PUT)
@router.put("/{user_id}")
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.Users).filter(models.Users.UserID == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.FullName = user.FullName
    db_user.Email = user.Email
    db_user.Phone = user.Phone
    db_user.Address = user.Address
    db_user.Password = user.Password
    db_user.DrivingLicenseNo = user.DrivingLicenseNo
    db_user.Role = user.Role

    db.commit()
    db.refresh(db_user)

    return {
        "message": "User updated successfully",
        "user": db_user
    }


# PARTIAL UPDATE (PATCH)
@router.patch("/{user_id}")
def patch_user(user_id: int, user: dict, db: Session = Depends(get_db)):
    db_user = db.query(models.Users).filter(models.Users.UserID == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)

    return {
        "message": "User partially updated",
        "user": db_user
    }


# DELETE USER
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.Users).filter(models.Users.UserID == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()

    return {
        "message": "User deleted successfully",
        "user": db_user
    }
