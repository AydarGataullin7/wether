import requests


def main():
    cities = ["Череповец", "Шереметьево", "Лондон"]
    params = {"mMnqT": "", "lang": "ru"}
    for city in cities:
        url = 'https://wttr.in/{0}'.format(city)
        response = requests.get(url, params=params)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
