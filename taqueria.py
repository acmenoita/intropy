#Menu c/ os preços

menu =  {
    'Baja Taco': 4.25,
    'Burrito': 7.50,
    'Bowl': 8.50,
    'Nachos':  11.00,
    'Quesadilla': 8.50,
    'Super Burrito': 8.50,
    'Super Quesadilla': 9.50,
    'Taco': 3.00,
    'Tortilla Salad': 8.00
}

#Inicia o total, para somar os pedidos (soma os preços)
total = 0.0 

#Solicitar ao utilizador para inserir o que deseja até fechar (Ctrl-Z)
try:
    while True:
        produto = input('Produto: ').strip().title() #Lê o produto, ignora os espaços e ajusta o formato das letras
        if produto in menu: #vai verificar se o produto encontra-se no menu
            total += menu[produto] #Soma o preço do produto ao total
            print (f'Total: ${total:.2f}') #Exibe o total c/ duas casas decimais
except EOFError:
    print() #linha em branco ao encerrar (Crlt-Z)
