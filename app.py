import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_do_programa():
    print("""
╭━╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━┳━╮
┃━╋━╮┃╰┳━┳┳╮╭━┳┳┳━┳┳┳━┫━┫━┫
┣━┃╋╰┫╋┃╋┃╭╯┃┻╋┃┫╋┃╭┫┻╋━┣━┃
╰━┻━━┻━┻━┻╯╱╰━┻┻┫╭┻╯╰━┻━┻━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯""")

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo("Encerrando o Programa")

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('Opção Invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes:\n')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    voltar_ao_menu_principal()
    
def escolher_opcao():
    try: 
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar Restaurante")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
