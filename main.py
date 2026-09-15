import os
from dotenv import load_dotenv
import requests
from datetime import datetime


def main():
    load_dotenv()
    token = os.getenv("PIXELA_TOKEN")
    username = os.getenv("PIXELA_USERNAME")
    graph_id = os.getenv("GRAPH_ID")

    pixela_endpoint = "https://pixe.la/v1/users"
    graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

    parameters = {
        "token":token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    #create account
    # response = requests.post(url=pixela_endpoint, json=parameters)
    # print(response.text)

    graph_config = {
        "id": graph_id,
        "name": "Coding Graph",
        "unit": "Hours",
        "type": "int",
        "color": "shibafu",
    }

    headers = {
        "X-USER-TOKEN": token,
    }


    pixela_creation_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"
    today = datetime(year=2026, month=9, day=14)
    pixel_data = {
        "date": today.strftime("%Y%m%d"),
        "quantity": "3600000",

    }

    response = requests.post(url=pixela_creation_endpoint, json=pixel_data, headers=headers)
    print(response.text)

if __name__ == "__main__":
    main()
