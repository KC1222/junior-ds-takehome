import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_dataset(n_rows=1000):
    np.random.seed(42)
    
    # Generate timestamps
    base_time = datetime(2023, 1, 1)
    timestamps = [base_time + timedelta(minutes=np.random.randint(0, 50000)) for _ in range(n_rows)]
    
    # Features
    distance_km = np.random.uniform(1, 20, n_rows).round(1)
    weather_options = ['Sunny', 'Rainy', 'Cloudy', 'Stormy']
    weather = np.random.choice(weather_options, n_rows, p=[0.6, 0.2, 0.15, 0.05])
    
    traffic_options = ['Low', 'Medium', 'High']
    traffic = np.random.choice(traffic_options, n_rows)
    
    package_weight = np.random.uniform(0.5, 30, n_rows).round(1)
    # Introduce some errors (negative weight) for cleaning task
    package_weight[::50] = -1.0 
    
    driver_rating = np.random.uniform(3.0, 5.0, n_rows).round(1)
    # Introduce missing values
    driver_rating[::20] = np.nan 

    # Target: Delivery Time (Linear relationship + noise)
    # Base 15 mins + 2 mins per km + weather penalty + traffic penalty
    weather_penalty = {'Sunny': 0, 'Cloudy': 2, 'Rainy': 10, 'Stormy': 20}
    traffic_penalty = {'Low': 0, 'Medium': 5, 'High': 15}
    
    delivery_time = []
    for i in range(n_rows):
        base = 15 + (2 * distance_km[i])
        w_pen = weather_penalty[weather[i]]
        t_pen = traffic_penalty[traffic[i]]
        noise = np.random.normal(0, 5)
        delivery_time.append(base + w_pen + t_pen + noise)

    df = pd.DataFrame({
        'timestamp': timestamps,
        'distance_km': distance_km,
        'weather_condition': weather,
        'traffic_level': traffic,
        'package_weight': package_weight,
        'driver_rating': driver_rating,
        'delivery_time_minutes': np.abs(np.array(delivery_time).round(0))
    })

    df.to_csv('delivery_data.csv', index=False)
    print("✅ 'delivery_data.csv' generated successfully!")

if __name__ == "__main__":
    generate_dataset()
