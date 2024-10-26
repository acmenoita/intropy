import sys
import requests

def main ():
#Verifica se o argumento da linha de cmd foi fornecido.
    if len(sys.argv) != 2:
        sys.exit ('Erro: Argumento da linha de cmd ausente')

#Tenta converter o argumento para float
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit('Erro: O argumento da linha de cmd não é um número')

#Tenta fazer a solicitação à API CoinDesk
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()

 # Obtem a informação do preço atual do bitcoin
        price = float(data["bpi"]["USD"]["rate_float"])

        # Calcula o custo total para o número de Bitcoins que se quer
        total_cost = bitcoins * price

        # Exibe o custo total em 4 casas decimais e com o separador de milhar
        print(f"${total_cost:,.4f}")

    except requests.RequestException:
        sys.exit("Erro: Não foi possível obter o preço do Bitcoin")

# Executa o programa
if __name__ == "__main__":
    main()
