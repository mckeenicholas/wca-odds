import requests


def get_wcif(competition: str, event: str):
    url = "https://www.worldcubeassociation.org/api/v0/competitions/"\
          + competition + "/wcif/public"
    response = requests.get(url)
    for person in response.json()["persons"]:
        print(person["name"], person["registration"])


if __name__ == "__main__":
    get_wcif("PleaseBeSolvedPickering2023", "333bf")

