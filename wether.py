import requests


def main():
    city = input('Введите город: ')
    params = {"mMnqT": ""}
    url = 'https://ru.wttr.in/{0}'.format(city)
    response = requests.get(url, params=params)
    response.raise_for_status()
    print(response.text)


if __name__ == '__main__':
    main()
