import requests
import streamlit as st

city_name = st.text_input("City Name")

url = "api.openweathermap.org/data/2.5/weather?q=${city_name}&appid=29dabdd9237ba71d01601da27f3d052b"

payload={}
headers = {
  'Authorization': 'Bearer 3P5CAoQiMU4_Lbl5JPxzi0x4zMVIuNSf833uBlGS24_7mxQZtXw1SaYd8vilpJFXXojHFmu0ays51Kaga3WiCXg0a5y-UQ6lVa-LMp-F3L2yQpX82EM33r-3Z_NkYXYx'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
