import requests
import pandas as pd
import time
from playsound import playsound

def generar_keypair():
    url = "https://asymmetricfrequency.org/utils/generate-keypair"
    response = requests.get(url)
    if response.status_code == 200:
        datos = response.json()
        return {
            'public_key': datos['solana_keypair']['public_key'],
            'private_key': datos['solana_keypair']['private_key'],
            'mnemonic': datos['mnemonic']
        }
    else:
        return None

def obtener_balance_solana(llave_publica):
    base_url = "https://asymmetricfrequency.org/solana/get-solana-balance/"
    url_completa = f"{base_url}{llave_publica}"
    response = requests.get(url_completa)
    if response.status_code == 200:
        return response.json()  # Suponemos que la API devuelve el balance como un número o un JSON que incluye el balance
    else:
        return None

def guardar_en_excel(datos):
    df = pd.DataFrame([datos])
    with pd.ExcelWriter('solana_balances.xlsx', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, index=False, sheet_name='Balances')
    print("Datos guardados en Excel.")

def main():
    while True:
        keypair = generar_keypair()
        if keypair:
            balance = obtener_balance_solana(keypair['public_key'])
            if balance and balance['balance'] > 0:  # Asumimos que el balance viene en un campo llamado 'balance'
                print(f"¡Balance encontrado! Balance: {balance['balance']}")
                playsound('alert_sound.mp3')  # Sonido de alerta
                guardar_en_excel({
                    'Public Key': keypair['public_key'],
                    'Private Key': keypair['private_key'],
                    'Mnemonic': keypair['mnemonic'],
                    'Balance': balance['balance']
                })
        time.sleep(1)  # Pequeña pausa para evitar sobrecargar la API

if __name__ == '__main__':
    main()
