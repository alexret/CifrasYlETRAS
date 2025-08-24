import requests

def get_word_definition(word):
    url = f"https://rae-api.com/api/words/{word}"
    response = requests.get(url)
    if response.status_code == 404:
        print("Palabra no encontrada")
        return None
    else:
        print("Palabra encontrada")