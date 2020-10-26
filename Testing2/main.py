import requests


def init_dolar():
    url = "https://www.dolarsi.com/api/api.php?type=valoresprincipales"
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload).json()
    for i, item in enumerate(response):
        casa = item["casa"]
        nombre = casa["nombre"]
        if nombre == "Dolar turista":
            dolar_turista = casa["venta"]
            return float(dolar_turista.replace(",", "."))
    return 0


print(init_dolar() + 100)



