import json
import random



def ler_arquivo():
    with open('palavras.json', encoding='utf8') as f:
        palavras_dict=json.loads(f.read())
    palavras=palavras_dict["palavras"]
    return palavras


def escolher_palavra(palavras):
    palavra_escolhida=random.choice(list(palavras.keys()))
    lista=[f"{palavra_escolhida.upper()}",palavras[palavra_escolhida]]
    return lista


def validar_input(letra):
    if len(letra)>1:
        return False
    if letra.isdigit():
        return False
    return True


def mostrar_palavra(palavra_escolhida):
    primeira=True
    palavra=''
    for i in palavra_escolhida:
        if primeira:
            palavra+=f'{i}'
        else:
            palavra+=f' {i}'
    # print(palavra)
    return palavra


palavras=ler_arquivo()
lista_palavra_com_dicas=escolher_palavra(palavras)
palavra_escolhida=lista_palavra_com_dicas[0]
dicas=lista_palavra_com_dicas[1]
chances=5
contador_dicas=0
letras_utilizadas=[]
palavra_oculta=['_ ' for x in palavra_escolhida]
texto_inicial="""
Bem vindo ao jogo da forca!
"""
print(texto_inicial)
while chances>0:
    print(f"""
          Letras utilizadas: {letras_utilizadas}
          Tentativas restantes: {chances}
          Palavra: {mostrar_palavra(palavra_oculta)}
          Dica: {dicas[contador_dicas]}
          """)
    if palavra_oculta == list(palavra_escolhida):
        print('Jogo terminado.')
        break
    letra=input("Digite uma letra: ").upper()
    if validar_input(letra):
        if letra in letras_utilizadas:
            print('Esta letra ja foi informada.')
            continue
        elif letra in palavra_escolhida:
            for i in range(len(palavra_escolhida)):
                if palavra_escolhida[i] == letra:
                    palavra_oculta[i]=letra
        else:
            chances-=1
            contador_dicas+=1
            print('A palavra não possui essa letra.')
        letras_utilizadas.append(letra.upper())
    else:
        print("Valor informado inválido.")
        continue
if chances==0:
    print("Fim de jogo, número de chances chegou a zero.")

