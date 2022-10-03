import mysql.connector
from prettytable import PrettyTable

def abrirbanco():
    try:
        global conexao
        conexao = mysql.connector.Connect(host='localhost',database='univap',user='root',password='')

        if conexao.is_connected():
            informacao_bd = conexao.get_server_info()
            print('conectado ao banco!')

            global comandos
            comandos = conexao.cursor()

            print(f'Conectado ao banco, informaçoes: {informacao_bd}')

            return 1
        else:
            print('Conexão nao estabelecida com o Banco')
            return 0

    except Exception as erro:
        print(f'ocorreu o seguinte erro: {erro}')


def cadastrar():
    try:
        comandos = conexao.cursor()
        registro = int(input('digite o registro do professor: '))
        nome_professor = input('digite o nome do professor: ')
        telefone_prof = input('digite o telefone do professor: ')
        idade_prof = int(input('digite a idade do professor: '))
        salario_prof = float(input('digite o salario do professor: '))
        comandos.execute(f'insert into professores values ({registro},"{nome_professor}","{telefone_prof}",{idade_prof},{salario_prof});')
        conexao.commit()
        print('cadastrado com sucesso!!')


    except Exception as erro:
        print(f'ocoreu o seguinte erro: {erro}')
        return 0



def selecionarTudo():
    grid = PrettyTable(['Registro Professor', 'Nome professor', 'Telefone Prof', 'Idade prof', 'Salario prof'])
    try:
        comandos = conexao.cursor()
        comandos.execute(f'select * from professores;')
        tabela = comandos.fetchall()
        if comandos.rowcount > 0:
            for i in tabela:
                grid.add_row([i[0],i[1],i[2],i[3],i[4]])
            print(grid)
        else:
            print(f'nao a registro na tabela professor;')
    except Exception as erro:
        print(f'ocorreu um erro: {erro}')
        return 'erro'


def selecionarComEspecificacoes(id):
    try:
        comandos = conexao.cursor()
        comandos.execute(f'select * from professores where registro ={id};')
        tabela = comandos.fetchall()
        if comandos.rowcount > 0:
            for i in tabela:
                print(f'Registros: {i}')
        print('Select executado perfeitamente!!')

        return 1


    except Exception as erro:
        print(f'ocorreu o seginte erro: {erro}')
        return 0



def AlterarRegistro(alterar_registro):
    try:
        comandos = conexao.cursor()
        comandos.execute(f'select * from professores where registro = {alterar_registro};')


        tabela = comandos.fetchall()

        if comandos.rowcount > 0:
            for i in tabela:
                print(f'Nome do professor {i[1]}')

            novo_nome = input('Digite um novo nome para o professor: ')
            comandos.execute(f'update professores set nomeprof = "{novo_nome}" where registro = {alterar_registro};')
            conexao.commit()

            print('Alteração feita com sucesso!')

            return 1

    except Exception as erro:
        print(f'erro ocorrido foi: {erro}')
        return 0


def exclusao(excluir_registro):
    try:
        comandos = conexao.cursor()
        comandos.execute(f'select * from professores where registro = {excluir_registro};')


        tabela = comandos.fetchall()
        if comandos.rowcount > 0:
            for r in tabela:
                print(f'nome do professor: {r[1]}')

        resp = input('deseja excluir o professor? sim/nao ').split()
        if resp[0] == 's':
            comandos.execute(f'delete from professores where registro = {excluir_registro}')
            conexao.commit()
            print('Exclusão realizada com sucesso!')

            return 1
    except Exception as erro:
        print(f'ocorreu o seguite erro: {erro}')
        return 0
def fecharprograma():
    conexao.close()
    comandos.close()
#MODULO PRINCIPAL DO PROGRAMA!!!!

if abrirbanco() == 1:
    while True:
            res = input('deseja entrar no banco de dados Professores? sim/nao ').split()
            if res[0] == 's':
                print('-'*60)
                print('BEM-VINDO AO BANCO DE DADOS UNIVAP!')
                print('-'*60)
            elif res[0] == 'n':
                break
            print('')
            print('-'*30)
            print('1- CREATE')
            print('2- READ')
            print('3- UPDATE')
            print('4- DELETE')
            print('5- FECHAR PROGRAMA')
            print('-'*30)

            resp = int(input('DESEJA EXECUTAR QUAL FUNÇÃO: '))
            while resp != 1 and resp != 2 and resp != 3 and resp != 4:
                resp = int(input('digite um valor valido: '))

            if resp == 1:
                        cadastrar()

            if resp == 2:
                while True:
                    res = int(input('deseja consutar todos os registros pressione 0 / se quiser fazer uma consulta especifica pressione 1: '))
                    while res != 1 and res != 0:
                        res = input('valor invalido, digite um valor valido: ')
                    if res == 0:
                        selecionarTudo()
                        break
                    elif res == 1:
                        escolher_registro = int(input('digite o registro do professor que deseja consultar: '))
                        selecionarComEspecificacoes(escolher_registro)
                        break


            if resp == 3:
                    registro_auteracao = int(input('digite o registro que deseja fazer a alteração: '))
                    AlterarRegistro(registro_auteracao)


            if resp == 4:
                    cod_disc = int(input('digite o registro do professor: '))
                    exclusao(cod_disc)

            if resp == 5:
                fecharprograma()
