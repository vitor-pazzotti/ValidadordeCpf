
from random import randint
import operator
import sys

def main():
    a = input('Digite "f" para formatar ou "v" para validar: ')

    if a.lower() == 'f':
        cpf = input('Digite o CPF que deseja formatação: ')
        retira_formatacao(cpf)

    elif a.lower() == 'v':
        cpf = input('Digite o CPF que deseja validacao: ')
        validar_cpf(cpf)
    else:
        print('Não existe esta chamada.')

def retira_formatacao(num_cpf):
    var = str(num_cpf)
    # if operator.contains(var, '.') or operator.contains(var, '-'):
    #     print('apresenta operador "."/"-"')
        
    CPF = num_cpf.replace('.', '').replace('-','').replace('/','').replace(',','')  
    print(CPF)             
             
    if len(num_cpf) < 11:
        print('Erro, seu cpf nao apresenta a quantidade de numeros corretas !')

        
def validar_cpf(num_cpf):

    if len(num_cpf) < 11:
        print('Erro, seu cpf nao apresenta a quantidade de numeros corretas !')
        return False

    if num_cpf == '' :
        print('Inválido')
        return False

    var = []
    for i in num_cpf:
        var.append(int(i))

    if len(set(var)) == 1:
        print('CPF Inválido.')
        return False


    #soma do primeiro verificador
    somaJ = (var[0] * 10) + (var[1] * 9) + (var[2] * 8) + (var[3] * 7) + (var[4] * 6) + (var[5] * 5) \
            + (var[6] * 4) + (var[7] * 3) + (var[8] * 2)

    restoJ = (somaJ * 10) % 11

    #Soma do segundo verificador
    somaK = (var[0] * 11) + (var[1] * 10) + (var[2] * 9) + (var[3] * 8) + (var[4] * 7) + (var[5] * 6) \
            + (var[6] * 5) + (var[7] * 4) + (var[8] * 3) + (var[9] * 2)
    
    restoK = (somaK * 10) % 11

    if restoJ == var[9] and restoK == var[10]:
        print("True")
        return True
    else:
        print("False")
        return False
        
if __name__ ==  '__main__':
    main()
        

