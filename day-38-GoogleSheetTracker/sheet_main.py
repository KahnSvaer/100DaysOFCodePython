import os
import requests

import sheety_integration as sheety

NUTRITIONIX_ID = os.environ.get("NUTRITIONIX_ID")
NUTRITIONIX_KEY = os.environ.get("NUTRITIONIX_KEY")

NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'


user_param = {
    "query": input("How much did you exercise today?\n"),
}

request_header = {
    'x-app-id': NUTRITIONIX_ID,
    'x-app-key': NUTRITIONIX_KEY
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=request_header, json=user_param)
response.raise_for_status()

exercise_data = response.json().get('exercises')
resulting_list = [{"exercise": row.get("name"), "duration": row.get("duration_min"), "calories": row.get("nf_calories")}
                  for row in exercise_data]
print(resulting_list)
for row in resulting_list:
    sheety.add_row(row.get("exercise"), row.get("duration"), row.get("calories"))
