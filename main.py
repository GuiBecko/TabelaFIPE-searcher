import requests
import pprint
import csv

def convertDicio_csv(dados, nome_do_arquivo):

    if not dados: #checa se a lista de dados está vazia, se estiver retorna ela
        return
    dados = list(dados.items()) # transforma dados em uma lista 


    with open("tabela.csv", "w", newline='') as arquivo:
        csv_writer = csv.writer(arquivo, delimiter=";")
        for produto in dados:
            csv_writer.writerow(produto)

    print(f"\nDados salvos em '{nome_do_arquivo}'!")
            

print("Navegador de tabela FIPE")

condicao = True
while condicao == True:
    tipoVeiculo = input("Informe o tipo do veículo que voce quer procurar (caminhoes/carros/motos): ")

    if tipoVeiculo == "caminhoes" or tipoVeiculo == "carros" or tipoVeiculo == "motos":
        condicao = False


apiFIPE = requests.get("https://parallelum.com.br/fipe/api/v1/" + tipoVeiculo + "/marcas")
apiFIPE = apiFIPE.json()


pprint.pprint(apiFIPE)


while condicao == False:
    marcaVeiculo = input("Selecione a marca do veiculo pelo seu codigo: ")

    for dicionario in apiFIPE:
        if dicionario.get('codigo') == marcaVeiculo:
            condicao = True

apiFIPE = requests.get("https://parallelum.com.br/fipe/api/v1/" + tipoVeiculo +"/marcas/" + marcaVeiculo + "/modelos")
apiFIPE = apiFIPE.json()

pprint.pprint(apiFIPE)

while condicao == True:

    modeloVeiculo = input("Selecione o modelo do veiculo pelo codigo: ")
    if not modeloVeiculo.isdigit():
        print(f"ERRO: O valor '{modeloVeiculo}' não é um código numérico válido.")
    else:
        # 4. Convertendo a entrada (string) para um número inteiro
        codigo_para_buscar = int(modeloVeiculo)
    
        # Pega a lista de modelos de forma segura
        lista_de_modelos = apiFIPE.get('modelos', [])

        # 5. A função any() agora compara o 'codigo' do modelo
        modelo_encontrado = any(
            # Compara o código do modelo com o código que o usuário digitou
            modelo.get('codigo') == codigo_para_buscar
            for modelo in lista_de_modelos
        )

    if modelo_encontrado:
        condicao = False
    


apiFIPE = requests.get("https://parallelum.com.br/fipe/api/v1/" + tipoVeiculo +"/marcas/" + marcaVeiculo + "/modelos/" + modeloVeiculo + "/anos" )
apiFIPE = apiFIPE.json()

pprint.pprint(apiFIPE)

anoVeiculo = input("Selecione o ano do veículo: ")

apiFIPE = requests.get("https://parallelum.com.br/fipe/api/v1/" + tipoVeiculo +"/marcas/" + marcaVeiculo + "/modelos/" + modeloVeiculo + "/anos/" + anoVeiculo )
apiFIPE = apiFIPE.json()

print(" ")
pprint.pprint(apiFIPE)

dadoFinal = apiFIPE

convertDicio_csv(dadoFinal, 'tabela.csv')
