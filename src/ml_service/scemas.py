from pydantic import BaseModel

class CarModel(BaseModel):
    Car_Name : str = "ciaz"
    Year : int = 2017
    Present_Price : float = 9.851562
    Driven_kms : int = 6900
    Fuel_Type : str = "Petrol"
    Selling_type : str	= "Dealer"
    Transmission : str = "Manual"
    Owner : int = 0
    mileage_level : str = "Low"