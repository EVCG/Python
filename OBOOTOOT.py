#Essa é uma atividade para o dia 24/09

class Pessoa:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    @staticmethod
    def criar_pessoa(nome, numero):
        pessoa = Pessoa(nome, numero)
        return pessoa


class Conversa:
    def __init__(self):
        self.mensagens = []

    def enviar_mensagem(self, remetente, destinatario, mensagem):
        self.mensagens.append({'remetente': remetente, 'destinatario': destinatario, 'mensagem': mensagem})

    def ver_conversa(self, pessoa):
        conversa = []
        for mensagem in self.mensagens:
            if mensagem['remetente'] == pessoa or mensagem['destinatario'] == pessoa:
                conversa.append(mensagem)
        return conversa


def entrar_na_conversa(pessoas, conversa):
    if not pessoas:
        print("Erro: Não há pessoas na lista.")
        return

    print("Pessoas na lista:")
    for i, pessoa in enumerate(pessoas, start=1):
        print(f"{i}. Nome: {pessoa.nome}, Número: {pessoa.numero}")

    escolha = int(input("Escolha o número da pessoa para ver a conversa: "))

    if escolha < 1 or escolha > len(pessoas):
        print("Escolha inválida.")
        return

    pessoa_escolhida = pessoas[escolha - 1]
    conversa_pessoa = conversa.ver_conversa(pessoa_escolhida.nome)

    if not conversa_pessoa:
        print(f"Nenhuma conversa encontrada para {pessoa_escolhida.nome}.")
        return

    print(f"Conversa de {pessoa_escolhida.nome}:")
    for mensagem in conversa_pessoa:
        remetente = mensagem['remetente']
        destinatario = mensagem['destinatario']
        texto_mensagem = mensagem['mensagem']

        if remetente == pessoa_escolhida.nome:
            print(f"Você: {texto_mensagem}")
        else:
            print(f"{remetente} : {texto_mensagem}")


def main():
    logo = """
  ______    ____     ____     ______    _______    ______   _______
 /  __  \  |  _ \   /  __ \  /  __  \  |__   __|  /  __  \  |__   __|
|  |  |  | | |_) | |  |  | | |  |  | |    | |    |  |  | |    | |
|  |  |  | |  _ <  |  |  | | |  |  | |    | |    |  |  | |    | |
|  |__|  | | |_) | |  |__| | |  |__| |    | |    |  |__| |    | |
 \______/  |____/   \_____/   \______/    |_|     \______/    |_|
    """
    print(logo)

    # Lista para armazenar as pessoas criadas
    pessoas = []
    conversa = Conversa()  # Criar uma instância de Conversa

    while True:
        print("\n[1] Adicionar um contato")
        print("[2] Enviar uma mensagem")
        print("[3] Entrar na conversa")
        resposta = input(":")
        if resposta == "1":
            nome = input("Digite o nome da pessoa: ")
            numero = input("Digite o número da pessoa: ")
            nova_pessoa = Pessoa.criar_pessoa(nome, numero)
            pessoas.append(nova_pessoa)
            print("\nContatos:")
            for pessoa in pessoas:
                print(f"Nome: {pessoa.nome}, Número: {pessoa.numero}")

        elif resposta == "2":
            if not pessoas:
                print("Erro: Não há pessoas na lista.")
            else:
                remetente = input("Digite o nome do remetente: ")
                destinatario = input("Digite o nome do destinatário: ")
                mensagem = input("Digite a mensagem: ")

                conversa.enviar_mensagem(remetente, destinatario, mensagem)
                print("Mensagem enviada com sucesso.")

        elif resposta == "3":
            entrar_na_conversa(pessoas, conversa)


if __name__ == '__main__':
    main()
