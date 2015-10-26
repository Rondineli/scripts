# -*- coding: utf-8 -*-

# Importando as libs do python
import argparse
import gnupg
import os


# Definição da função para encriptar o arquivo
def encrypt_file(gpg, file_encrypt, recipients, output_file_name):
    # Váriavel "None" para em caso de erro do criptografia não estourar exception errada
    status = ''
    # Abre o arquivo a ser encriptado
    with open(file_encrypt, 'rb') as new_file:
        # Sobrepões a variável status para a novo arquivo encriptado
        status = gpg.encrypt_file(
            new_file,
            recipients=recipients,
            output=output_file_name
        )
    # Retorna o status
    return status

# Definição do inicio do script
# Primeiro bloco a ser executadp
if __name__ == "__main__":
    # Parser é a lib que utilizaremos, para pegar os argumentos no script
    # Eu prefiro usar o sys.argv, mas nesse caso, achei mais prático usar o argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_encrypt', '-f', required=True)
    parser.add_argument('--output', '-t', required=True)
    parser.add_argument('--recipients', '-r', required=True)
    parser.add_argument('--gpg-home', default=os.path.join(os.environ['HOME'], '.gnupg'))

    # Define os valores dos argumentos para um objeto chamado "args"
    args = parser.parse_args()
    # Define a home da base de chaves do gpg, por default, ele fica em
    # ~/.gnupg
    gpg_home = args.gpg_home

    # Inicia a lib gpg, para gerenciamentos das chaves públicas e privadas
    gpg = gnupg.GPG(gnupghome=gpg_home, verbose=True, use_agent=False)
    # Executa função que irpa criptografar o arquivo escolhido.
    encrypt_file(gpg=gpg, file_encrypt=args.file_encrypt,
                 recipients=args.recipients, output_file_name=args.output)
