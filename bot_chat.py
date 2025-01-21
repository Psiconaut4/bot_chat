import nltk
from nltk.chat.util import Chat, reflections

pares = [
    [
        r"oi|Olá|hey|hello|Oi",
        ["Olá", "Oi", "Hey"]
    ],

    [
        r"Qual é o seu nome?",
        ["O nome que você me der", "Eu sou o seu chatbot"]
    ],

    [
        r"Como vai você?|Como você está?|Tudo bem?",
        ["To indo", "Cada dia um dia", "Ótimo e você", "vou bem"]
    ],

    [
        r"Adeus|Obrigado|Tchau",
        ["Por nada", "De nada", "Até a próxima", "Vai tarde!"]
    ],

]

def chatbot():
    print("Olá meu querido programador, vamos conversar?")
    nome = input('Como você quer que eu te chame? ')
    chat = Chat(pares, reflections)

    while True:
        try:
            respost = chat.respond(input(f'{ nome}: '))
            print(respost)
        except KeyboardInterrupt:
            break

chatbot()