import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado.")
            return

        print("\n=== Endereço Encontrado ===")
        print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
        print(f"Bairro    : {dados.get('bairro', 'N/A')}")
        print(f"Cidade    : {dados.get('localidade', 'N/A')}")
        print(f"Estado    : {dados.get('uf', 'N/A')}")

    except requests.RequestException as e:
        print("Erro ao consultar o CEP:", e)

def main():
    cep = input("Digite o CEP (somente números): ").strip()
    if cep.isdigit() and len(cep) == 8:
        consultar_cep(cep)
    else:
        print("CEP inválido. Digite exatamente 8 números.")

if __name__ == "__main__":
    main()
