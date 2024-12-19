import requests
import time
import random

fuel_types = ['Petrol','Diesel','CNG']
transmission = ['Automatic', 'Manual']
seller = ['Dealer', 'Individual']
mileage_level = ['High','Mid','Low']

for i in range(50):
    car_id = {"car_id":i}
    data = {
        "Car_Name": "ciaz",
        "Year": random.randint(2003,2018),
        "Present_Price": random.uniform(2,10),
        "Driven_kms": random.randint(5000,100000),
        "Fuel_Type": random.choice(fuel_types),
        "Selling_type": random.choice(seller),
        "Transmission": random.choice(transmission),
        "Owner": random.randint(0,3),
        "mileage_level": random.choice(mileage_level)
    }
    response = requests.post('http://price-predict:8000/api/prediction', params=car_id, json=data)
    print(response.json())
    time.sleep(random.randint(1,5))