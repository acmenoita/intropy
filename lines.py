import sys
import os

def main():
    #Verifica se o utilizador fornece exatamente um argumento
    if len (sys.argv)!= 2:
        sys.exit ('Erro: número incorreto de argumentos fornecidos')

    #Obtem o nome do arquivo e verifica a extensão
    filename = sys.argv[1]
    if not filename.endswith('.py'):
        sys.exit('Erro: o arquivo ñ é um arquivo Python (.py)')

    #Verifica se o arquivo existe
    if not os.path.isfile(filename):
        sys.exit('Erro: o arquivo especifico ñ existe')

    #varaivel para a contagem das linhas de codigo
    total_linhas = 0

    #Abre o arquivo para leitura
    with open (filename, 'r') as file:
        for linha in file:
        #Remove os espaços em branco do inicio e do fim da linha
            linha_formatada = linha.strip()

        #Ignora as linhas em branco e as linhas que começam com #
            if linha_formatada and not linha_formatada.startwith('#'):
                total_linhas += 1 #Soma 1 à contagem para cada linha de código válida

    #Exibe o total de linhas de código
    print(total_linha)

#Exevuta a funçao principal se o script estiver sendo executado diretamente
if __name__ == '__main__':
    main()
