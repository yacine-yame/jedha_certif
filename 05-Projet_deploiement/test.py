import requests

# ENDPOINT ='http://127.0.0.1:8000/predict'
ENDPOINT ='https://my-jedha-api2021.herokuapp.com/predict'
response = requests.post(ENDPOINT,json={"input": [[6.2,0.66,0.48,1.2,0.029,29.0,75.0,0.98920,3.33,0.39,12.8]]
})
print(response.json())