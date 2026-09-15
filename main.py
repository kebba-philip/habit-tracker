import os
from dotenv import load_dotenv
import requests

def main():
    load_dotenv()
    pixela_endpoint = "https://pixe.la/v1/users"
    token = os.getenv("PIXELA_TOKEN")

    parameters = {
        "token":token,
        "username": "bee107",
        "agreeTermsOfService": "yes",
        "notMinor": "yes"

    }

    #create account
    # response = requests.post(url=pixela_endpoint, json=parameters)
    # print(response.text)


if __name__ == "__main__":
    main()
