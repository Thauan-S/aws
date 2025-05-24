import requests
from datetime import datetime

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        
        dados = resposta.json()
        
        # A chave vem no formato MOEDA + BRL, por exemplo: "USDBRL"
        chave = f"{moeda}BRL"
        
        if chave not in dados:
            print("Moeda não encontrada ou inválida.")
            return
        
        cotacao = dados[chave]
        
        valor = cotacao['bid']
        maximo = cotacao['high']
        minimo = cotacao['low']
        timestamp = int(cotacao['create_date'].split()[0].replace("-", ""))
        hora = cotacao['create_date'].split()[1]
        
        # A API fornece a data em formato "YYYY-MM-DD HH:MM:SS"
        data_hora = cotacao['create_date']
        dt = datetime.strptime(data_hora, "%Y-%m-%d %H:%M:%S")
        
        print(f"\nCotação para {moeda}/BRL:")
        print(f"Valor atual: R$ {valor}")
        print(f"Máximo    : R$ {maximo}")
        print(f"Mínimo    : R$ {minimo}")
        print(f"Última atualização: {dt.strftime('%d/%m/%Y %H:%M:%S')}")

    except requests.RequestException as e:
        print("Erro ao consultar a API:", e)

def main():
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").strip().upper()
    if len(moeda) == 3 and moeda.isalpha():
        consultar_cotacao(moeda)
    else:
        print("Código de moeda inválido. Deve ter 3 letras.")

if __name__ == "__main__":
    main()
