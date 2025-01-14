import math

def f(funcao, x):
    try:
        # Substitui 'x' na string pela variável correspondente
        valor = eval(funcao)
        return valor
    except Exception as e:
        return f"Erro ao calcular a função: {e}"
        
def meio(a, b):
    return (a + b) / 2.0

def bissec(funcao, a, b, precisao, n, itmax):
    mid = meio(a, b)
    if abs(b - a) < precisao or n >= itmax:
        return mid

    n += 1
    
    f_mid = f(funcao, mid)
    
    if f_mid == 0.0:
        return mid
    elif f_mid * f(funcao, a) < 0:
        return bissec(funcao, a, mid, precisao, n, itmax)
    else:
        return bissec(funcao, mid, b, precisao, n, itmax)

def newton(x0, precisao, n, itmax):
    if abs(f(funcao, x0)) <= precisao:
        return x0  

    if n > itmax:
        return x0  

    x1 = x0 - (f(funcao, x0) / f(dfuncao, x0))  
    return newton(x1, precisao, n + 1, itmax) 

def mil(funcao, funcaoIt, x0, precisao, n, itmax):
    if abs(f(funcao, x0)) < precisao:
        return x0  
    
    if n > itmax:
        return x0  

    x1 = f(funcaoIt ,x0) 

    if abs(f(funcao, x1)) < precisao or abs(x1 - x0) < precisao:
        return x1  
    
    return mil(funcao, funcaoIt, x1, precisao, n + 1, itmax)
    
def secante(funcao, x0, x1, precisao, n, itmax):
    if f(funcao, x1) - f(funcao, x0) != 0:
        x2 = x1 - (f(funcao, x1) * (x1 - x0)) / (f(funcao, x1) - f(funcao, x0))
    else:
        x2 = 0

    if abs(f(funcao, x2)) < precisao or abs(x2 - x1) < precisao or n > itmax:
        return x2

    n += 1
    
    return secante(funcao, x1, x2, precisao, n, itmax)
    
def regulafalsi(funcao, x0, x1, precisao, n, itmax):
    if f(funcao, x1) - f(funcao, x0) != 0:
        x2 = (x0 * f(funcao, x1) - x1 * f(funcao, x0)) / (f(funcao, x1) - f(funcao, x0))
    else:
        x2 = 0

    if (abs(x2 - x1) / abs(x2) < precisao or abs(x2 - x0) / abs(x2) < precisao or n > itmax):
        return x2

    n += 1

    if funcao(x1) < 0:
        return regulafalsi(funcao, x0, x2, precisao, n, itmax)
    
    return regulafalsi(funcao, x2, x1, precisao, n, itmax)
    
def main():
    funcao = " "
    dfuncao = " "
    funcaoIt = " "
    a = 0
    b = 0
    x0 = 0
    x1 = 0
    precisao = 0.0
    itmax = 0
    n = 0
   
    while True:
        print("\nMenu:")
        print("1. Método da Bissecção")
        print("2. Método Iterativo Linear (MIL)")
        print("3. Método de Newton")
        print("4. Método da Secante")
        print("5. Método da Regula Falsi")
        print("6. Operadores")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            funcao = str(input("Digite a função: "))
            a = float(input("Digite a: "))
            b = float(input("Digite b: "))
            precisao = float(input("Digite a precisão: "))
            itmax = int(input("Digite o número máximo de iterações: "))
            raiz = bissec(funcao, a, b, precisao, n, itmax)
            print(f"A raiz encontrada é: {raiz}")
            print(f"Número de iterações: {n}")

        elif escolha == '2':
            funcao = str(input("Digite a função: "))
            funcaoIt = str(input("Digite a função iterativa: "))
            x0 = float(input("Digite x0: "))
            precisao = float(input("Digite a precisão: "))
            itmax = int(input("Digite o número máximo de iterações: "))
            raiz = newton(funcao, funcaoIt, x0, precisao, n, itmax)
            print(f"A raiz encontrada é: {raiz}")
            print(f"Número de iterações: {n}")
            
        elif escolha == '3':
            funcao = str(input("Digite a função: "))
            print(f(funcao,2))
            dfuncao = str(input("Digite a derivada da função: "))
            x0 = float(input("Digite x0: "))
            precisao = float(input("Digite a precisão: "))
            itmax = int(input("Digite o número máximo de iterações: "))
            raiz = mil(funcao, funcaoIt, x0, precisao, n, itmax)
            print(f"A raiz encontrada é: {raiz}")
            print(f"Número de iterações: {n}")
            
        elif escolha == '4':
            funcao = str(input("Digite a função: "))
            x0 = float(input("Digite x0: "))
            x1 = float(input("Digite x1: "))
            precisao = float(input("Digite a precisão: "))
            itmax = int(input("Digite o número máximo de iterações: "))
            raiz = secante(funcao, x0, x1, precisao, n, itmax)
            print(f"A raiz encontrada é: {raiz}")
            print(f"Número de iterações: {n}")
            
        elif escolha == '5':
            funcao = str(input("Digite a função: "))
            x0 = float(input("Digite x0: "))
            x1 = float(input("Digite x1: "))
            precisao = float(input("Digite a precisão: "))
            itmax = int(input("Digite o número máximo de iterações: "))
            raiz = regulafalsi(funcao, x0, x1, precisao, n, itmax)
            print(f"A raiz encontrada é: {raiz}")
            print(f"Número de iterações: {n}")
        
        elif escolha == '6':
            print("Adição(+)\t\tPotenciação(pow(base,expoente))\t\tCosseno(math.cos(x))")
            print("Subtração(-)\t\tRadiciação(math.sqrt(x))\t\tTangente(math.tan(x))")
            print("Multiplicação(*)\tLogaritmo(math.log(logaritmando,base))")
            print("Divisão(/)\t\tSeno(math.sin(x))")
            
        elif escolha == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()