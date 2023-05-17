"""Módulo com funções."""


def is_prime(number: int) -> bool:
    """Retorna True se o número for primo e False caso contrário."""
    cont = 0
    if number<=0:
        print("Número inválido")
    else:    
        for c in range(1, number+1):
            if number%c==0:
                cont+=1
        if cont==2:
            return True
        else:
            return False


def list_prime_factors(number: int) -> list[int]:
    """Retorna uma lista com os fatores primos de cada número da lista fornecida."""
    fator = 2
    lista=[]
    while number!= 1:
        while number%fator == 0:
            number = number / fator
            lista.append(fator)
        fator = fator +1
    return lista
number = int(input("Digite um número: "))
is_prime(number)
print(list_prime_factors(number))