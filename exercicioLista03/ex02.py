# 02 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
# igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as
# informações.

usuario = input('Insira seu nome de usuário: ')
senha = input('Insira sua senha: ')

while usuario == senha:
    print('ERRO! Não é possível utilizar o nome de usuário como senha.')
    usuario = input('Insira seu nome de usuário: ')
    senha = input('Insira sua senha: ')
