import requests

def gerar_usuario():
    url = "https://randomuser.me/api/"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Lança erro para status HTTP >= 400
        
        dados = resposta.json()
        usuario = dados["results"][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("=== Perfil de Usuário Aleatório ===")
        print(f"Nome : {nome}")
        print(f"Email: {email}")
        print(f"País : {pais}")

    except requests.RequestException as e:
        print("Erro ao conectar à API:", e)

def main():
    gerar_usuario()

if __name__ == "__main__":
    main()
