import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

ID = "6a478103"
API_KEY = "c7ad6f17d8f84dcf7cc3ef35396c8691"
GENDER = "MALE"
WEIGHT_KG = 82
HEIGHT_CM = 1.75
AGE = 26

USERNAME = "Meliodas"
PASSWORD = "12dafa23dqwefd23412sd"

os.environ["ID"] = ID
os.environ["API_KEY"] = API_KEY

print(os.environ)
cont = True

while cont:
    exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

    exercise_text = input("Tell me which exercises you did: ")
    headers = {
        "x-app-id": ID,
        "x-app-key": API_KEY
    }
    parameters = {
        "query": exercise_text,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }

    response = requests.post(exercise_endpoint, headers=headers, json=parameters)

    results = response.json()

    exercise = results["exercises"][0]
    workouts_name = exercise["name"].title()
    calories_burned = exercise["nf_calories"]
    duration_minutes = exercise["duration_min"]

    # print("Workout Results:", workouts_name)
    # print("Calories Burned:", calories_burned)
    # print("Duration (minutes):", duration_minutes , type(duration_minutes))

    let_url = "https://api.sheety.co/d3d34f7c5502b9b5dfd7cf50b432cee8/myWorkouts/workouts"

    response_sheet = requests.get(let_url)

    today = datetime.now()
    re_today = today.strftime("%d/%m/%Y")
    time_now = today.strftime("%X")

    post_url = "https://api.sheety.co/d3d34f7c5502b9b5dfd7cf50b432cee8/myWorkouts/workouts"

    workouts = {'workout': {'date': re_today,
                            'time': time_now,
                            'exercise': workouts_name,
                            'duration': duration_minutes,
                            'calories': calories_burned,
                            }
                }

    print(workouts)

    correct = input("Is this correct : ")

    if correct == "y":
        sheet_response = requests.post(
            post_url,
            json=workouts,
            auth=(
                USERNAME,
                PASSWORD,
            )
        )
    else:
        cont = False
