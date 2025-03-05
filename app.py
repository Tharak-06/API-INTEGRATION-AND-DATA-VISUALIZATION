import requests
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# OpenWeatherMap API Key
API_KEY = '1d9d014b3bfd21d36f0df835f51e72b2'

# Streamlit UI
st.title("🌦 Weather Data Visualization App")
city = st.text_input("Enter City Name")

if st.button("Get Weather"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={API_KEY}"
    weather_data = requests.get(url).json()

    if weather_data.get("cod") != 200:
        st.error("❌ No City Found! Please try again.")
    else:
        # Extract data
        weather = weather_data['weather'][0]['main']
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        # Display data
        st.write(f"**Weather:** {weather}")
        st.write(f"**Temperature:** {temp}°C")
        st.write(f"**Humidity:** {humidity}%")
        st.write(f"**Wind Speed:** {wind_speed} m/s")

        # Prepare DataFrame for Visualization
        data = pd.DataFrame({
            'Weather Parameter': ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (m/s)'],
            'Values': [temp, humidity, wind_speed]
        })

        # Plot using Matplotlib & Seaborn
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(x="Weather Parameter", y="Values", data=data, palette="coolwarm", ax=ax)
        ax.set_title(f"Weather Data for {city}")

        # Show plot in Streamlit
        st.pyplot(fig)