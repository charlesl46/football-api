import requests
import ast
import time

API_URL = "https://sportscore1.p.rapidapi.com/"

FOOTBALL_ID = 1
PREMIER_LEAGUE_ID = 317

class APIKeyMissingError(Exception):
    def __init__(self) -> None:
        super().__init__(
        "All methods require an API key. See "
        "https://rapidapi.com/tipsters/api/sportscore1/"
        "for how to retrieve an authentication token from "
        "SportScore API"
    )
    pass

def set_api_key(api_key : str):
    global API_KEY
    API_KEY = api_key
    pass

def _api_request(end_url : str,querystring = None, type = None) -> dict:
    time.sleep(0.06)
    url = str(API_URL + end_url)
    
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "sportscore1.p.rapidapi.com"
    }
    if type == None:
        response = requests.request("GET", url, headers=headers, params = querystring)
    elif type == "POST":
        response = requests.request("POST", url, headers=headers, params = querystring)
    if response == "<Response [401]>":
        raise APIKeyMissingError
    else:
        return response.json()
    
def _adapt_json_to_python(json : str):
    json = json.replace("null","None")
    json = json.replace("true","True")
    json = json.replace("false","False")
    print(json)
    return ast.literal_eval(json)


