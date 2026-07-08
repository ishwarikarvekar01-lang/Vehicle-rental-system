from fastapi import FastAPI

from routers import users
from routers import vehicles
from routers import vehicle_categories
from routers import bookings
from routers import drivers
from routers import payments
from routers import rental_location
from routers import vehicle_maintenance
from routers import reviews
from routers import insurance

app = FastAPI(
    title="Vehicle Rental System API",
    version="1.0.0",
    description="FastAPI CRUD Operations for Vehicle Rental System"
)

# Home Route
@app.get("/")
def home():
    return {
        "message": "Welcome to Vehicle Rental System API"
    }

# Include all routers
app.include_router(users.router)
app.include_router(vehicles.router)
app.include_router(vehicle_categories.router)
app.include_router(bookings.router)
app.include_router(drivers.router)
app.include_router(payments.router)
app.include_router(rental_location.router)
app.include_router(vehicle_maintenance.router)
app.include_router(reviews.router)
app.include_router(insurance.router)