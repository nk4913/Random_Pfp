import requests


class Pfp:

    def __init__(self) -> None:
        self.url = "https://any-anime.p.rapidapi.com/anime/img"
        self.headers = None

    def fetch_image(self):

        self.headers = {
            "X-RapidAPI-Key": "ac4b2b67e6msh85f2775b307ee58p1b5147jsnc4fe82aec600",
            "X-RapidAPI-Host": "any-anime.p.rapidapi.com"
        }

        response = requests.request("GET", self.url, headers=self.headers , timeout=8)

        return response.text
