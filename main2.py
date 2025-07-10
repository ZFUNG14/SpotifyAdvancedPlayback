from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json


#small program that use SpotifyAPI to get artist top 10 tracks
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)

    # Check if the request was successful
    if result.status_code == 200:
        json_result = json.loads(result.content)
        # Safely get the access token
        token = json_result.get("access_token")
        if token:
            return token
        else:
            print("Error: 'access_token' not found in the response.")
            print("Response:", json_result)  # Print the full response for debugging
    else:
        print(f"Error: Request failed with status code {result.status_code}")
        print("Response:", result.text)  # Print the response content for debugging

def get_auth_header(token):
    return {"Authorization": f"Bearer {token}"}


def search_for_artists(token, artist_name):
    url = "https://api.spotify.com/v1/search" # change this according to what we wanna do -> refer to spotify endpoint lists
    headers = get_auth_header(token)
    query = f"q={artist_name}&type=artist&limit=1"

    query_url = url + "?" + query
    result = get(query_url, headers= headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artist with this name exists! ")
        return None
    
    return json_result[0]


def get_songs_by_artist(token,artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=AU" 
    headers = get_auth_header(token)
    result = get(url, headers= headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

print("Enter Artist Name:")
artist = input()
token = get_token()
result = search_for_artists(token, artist)
artist_id = result["id"]
songs = get_songs_by_artist(token,artist_id) 

for idx, song in enumerate(songs):
    print(f"{idx + 1}.{song['name']}")