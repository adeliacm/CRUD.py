import colorama

def menu():
    print('''
        1 - Listar todos os alunos
        2 - Listar todos os alunos por ordem alfabetica
        3 - Remover aluno
        4 - Atualizar aluno
        5 - Cadastrar aluno
        6 - Procurar aluno por nome
        7 - Sair
    ''')

class Gestao:
    def __init__(self):
        self.alunos = []
    def cadastrar(self):
        print(colorama.Fore.RESET)
        nome = input("Digite o nome do aluno (-1 para sair): ")
        if(nome == "-1"):
            return "retirada"
        if(len(nome) == 0):
            print(colorama.Fore.RED + "Digite um nome valido")
            self.cadastrar()
            return
        email = input("Digite o e-mail do aluno: ")
        if(email.find("@") == -1 or email.find(".com") == -1):
            print(colorama.Fore.RED + "Digite um e-mail valido!!")
            self.cadastrar()
            return
        for aluno in self.alunos:
            if(aluno["email"] == email):
                print("O e-mail já existe!")
                self.cadastrar()
                return
        self.alunos.append({
            "nome": nome,
            "email": email
        })
        return "cadastrado"

    def listarTodosOsUsuarios(self):
        for aluno in self.alunos:
            print(f"Aluno: { aluno['nome'] } Email: { aluno['email'] }")
    def listarPorOrdemAlfabetica(self):
        alunos_ordenados = sorted(self.alunos, key=lambda aluno: aluno["nome"])
        for aluno in alunos_ordenados:
            print(f"Aluno: { aluno['nome'] } Email: { aluno['email'] }")

    def procurarAlunoPorNome(self):
        nome = input("Digite o nome do aluno (-1 para sair): ")
        if(nome == "-1"):
            return "retirada"
        if(len(nome) == 0):
            print("Digite um nome valido")
            self.procurarAlunoPorNome()
            return
        alunos_nome = []
        for aluno in self.alunos:
            if(aluno["nome"].find(nome) != -1):
                alunos_nome.append(aluno)
        for aluno in alunos_nome:
            print(colorama.Fore.GREEN + f"Aluno: {aluno['nome']} Email: {aluno['email']}")
        if (len(alunos_nome) == 0):
            print(colorama.Fore.YELLOW + "Aluno não encontrado")

    def removerAlunoEmail(self):
        email = input("Digite o e-mail do aluno para remover (-1 para sair): ")
        if(email == "-1"):
            return "retirada"
        for aluno in self.alunos:
            if(aluno["email"] == email):
                indice = self.alunos.index(aluno)
                self.alunos.pop(indice)
                return "sucesso"
        self.listarTodosOsUsuarios()
        return "nao_encontrado"
    def atualizarPorEmail(self):
        print(colorama.Fore.RESET)
        email = input("Digite o e-mail do aluno para atualizar o nome (-1 para sair): ")
        if (email == "-1"):
            return "retirada"

        nome = input("Novo nome: ")

        if (len(nome) == 0):
            print(colorama.Fore.RED + "Digite um nome valido")
            self.atualizarPorEmail()
            return

        for aluno in self.alunos:
            if (aluno["email"] == email):
                indice = self.alunos.index(aluno)
                self.alunos[indice] = {
                    "nome": nome,
                    "email": email
                }
                return "sucesso"
        print(colorama.Fore.YELLOW + "O aluno não foi encontrado")

if __name__ == "__main__":
    print("\t\t-- Gestão -- \t\t")
    gestao = Gestao()
    while(True):
        print(colorama.Fore.WHITE)
        menu()
        opcao = input("Escolha sua opção: ")
        if(opcao == "7"):
            print(colorama.Fore.WHITE + "Você será deslogado")
            break
        elif (opcao == "6"):
            resultado = gestao.procurarAlunoPorNome()
            if (resultado == "retirada"):
                print(colorama.Fore.RED + "A ação foi cancelada")
        elif(opcao == "5"):
            resultado = gestao.cadastrar()
            if(resultado == "retirada"):
                print(colorama.Fore.RED + "A ação foi cancelada")
            elif(resultado == "cadastrado"):
                print(colorama.Fore.GREEN + "O aluno foi cadastrado com sucesso")
        elif(opcao == "4"):
            resultado = gestao.atualizarPorEmail()
            if(resultado == "retirada"):
                print(colorama.Fore.RED + "A ação foi cancelada")
            elif(resultado == "sucesso"):
                print(colorama.Fore.GREEN + "O aluno foi atualizado com sucesso")
        elif(opcao == "3"):
            resultado = gestao.removerAlunoEmail()
            if(resultado == "retirada"):
                print(colorama.Fore.RED + "A ação foi cancelada")
            elif(resultado == "nao_encontrado"):
                print(colorama.Fore.YELLOW + "O aluno não foi encontrado")
            elif(resultado == "sucesso"):
                print(colorama.Fore.GREEN + "O aluno foi removido com sucesso")
        elif(opcao == "2"):
            gestao.listarPorOrdemAlfabetica()
        elif(opcao == "1"):
            gestao.listarTodosOsUsuarios()
        else:
            print(colorama.Fore.RED + "Nenhuma opção valida foi encontrada")
