# CRUD.py
Sistema básico de CRUD sem interface.
Desenvolvido em python para fins acadêmicos, focando na compreensão do uso de lista e dicionários.

________________________________________________________________________________________________________        
 ***  Instalção  *** 		

       pip3 install -r requirements.txt
   
________________________________________________________________________________________________________
 ***  Execução Menu  ***
               -- Gestão --
        1 - Listar todos os alunos
        2 - Listar todos os alunos por ordem alfabetica
        3 - Remover aluno
        4 - Atualizar aluno
        5 - Cadastrar aluno
        6 - Procurar aluno por nome
        7 - Sair
   Escolha sua opção:
________________________________________________________________________________________________________
 ***  Execução Cadastrar aluno  ***
 
 Escolha sua opção: 5

Digite o nome do aluno (-1 para sair): Adelia Camargo
Digite o e-mail do aluno: a#b.com (falta do @)
Digite um e-mail valido!!

Digite o nome do aluno (-1 para sair): Adelia Camargo (exemplo)
Digite o e-mail do aluno: a@b.com (exemplo)
O aluno foi cadastrado com sucesso
________________________________________________________________________________________________________
***  Execução Atualizar aluno  ***

Escolha sua opção: 4

Digite o e-mail do aluno para atualizar o nome (-1 para sair): a@c.com (email não existente)
Novo nome: Adelia Cs
O aluno não foi encontrado 

Digite o e-mail do aluno para atualizar o nome (-1 para sair): a@a.com
Novo nome: Adelia C.
O aluno foi atualizado com sucesso
__________________________________________________________________________________________________________
***  Execução Listar todos os alunos  ***

Escolha sua opção: 1
Aluno: Adelia S. Email: a@b.com
Aluno: Adelia C. Email: a@a.com
__________________________________________________________________________________________________________
***  Execução Listar todos os alunos em ordem alfabética ***

Escolha sua opção: 2
Aluno: Adelia C. Email: a@a.com
Aluno: Adelia S. Email: a@b.com
__________________________________________________________________________________________________________
***  Execução Procurar aluno por nome ***
Escolha sua opção: 6
Digite o nome do aluno (-1 para sair): Adelia
Aluno: Adelia C. Email: a@a.com

Digite o nome do aluno (-1 para sair): C. (Pesquisa pelo Sobrenome)
Aluno: Adelia C. Email: a@a.com
___________________________________________________________________________________________________________
***  Execução Remover aluno  ***

Escolha sua opção: 3
Digite o e-mail do aluno para remover (-1 para sair): a@c.com (email não existente)
Aluno: Adelia S. Email: a@b.com 
O aluno não foi encontrado (retorna que não foi encontrado e lista os alunos possiveis)

Digite o e-mail do aluno para remover (-1 para sair): a@a.com
O aluno foi removido com sucesso
___________________________________________________________________________________________________________
***  Execução Sair  ***

Escolha sua opção: 7
Você será deslogado

