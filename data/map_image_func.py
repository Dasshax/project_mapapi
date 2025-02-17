import requests

def get_map_image(coord: list, size:list):
    reguest = f"https://static-maps.yandex.ru/v1?ll={coord[0]},{coord[1]}&spn={size[0]},{size[1]}&apikey="
    reponce = requests.get(reguest)
    if not reponce:
        print(reponce.status_code)
        return None
    else:
        return reponce.content

