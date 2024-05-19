import requests

def obtener_balance_solana(llave_publica):
    base_url = "https://asymmetricfrequency.org/solana/get-solana-balance/"
    url_completa = f"{base_url}{llave_publica}"
    
    response = requests.get(url_completa)
    
    if response.status_code == 200:
        return response.json()  # Suponiendo que la respuesta es un JSON
    else:
        return {'error': 'No se pudo obtener el balance', 'status_code': response.status_code}

# Llave pública de ejemplo
llave_publica = "ByfkQF1bkEuxaWWwPwaojp6MvuMMNT9xqedBykHoEpaG"
balance = obtener_balance_solana(llave_publica)
print("Balance obtenido:", balance)

