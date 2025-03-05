import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# OpenWeatherMap API Key
API_KEY = '1d9d014b3bfd21d36f0df835f51e72b2'

# User input for city
user_input = input("Enter city: ")

# Fetch weather data
url = f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={API_KEY}"
weather_data = requests.get(url).json()

# Check for valid city
if weather_data.get("cod") != 200:
    print("No City Found! Please try again.")
    exit()

# Extract relevant data
weather = weather_data['weather'][0]['main']
temp = weather_data['main']['temp']
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']

# Print weather details
print(f"The weather in {user_input} is: {weather}")
print(f"The temperature in {user_input} is: {temp}°C")
print(f"Humidity in {user_input}: {humidity}%")
print(f"Wind Speed in {user_input}: {wind_speed} m/s")

# Create a DataFrame for visualization
data = pd.DataFrame({
    'Weather Parameter': ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)'],
    'Values': [temp, humidity, wind_speed]
})

# Visualization using Matplotlib and Seaborn
plt.figure(figsize=(8, 5))
sns.barplot(x="Weather Parameter", y="Values", data=data, palette="coolwarm")
plt.title(f"Weather Data for {user_input}")
plt.ylabel("Value")
plt.show()