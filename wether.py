import requests


url = 'https://ru.wttr.in/Череповец?mMnqT}'
response = requests.get(url)
response.raise_for_status()
print(response.text)
