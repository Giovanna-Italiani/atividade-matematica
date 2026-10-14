import math

def mdc(a, b):
    """Calcula o Máximo Divisor Comum (para simplificar frações)."""
    while b:
        a, b = b, a % b
    return abs(a)

def simplificar_fracao(num, den):
    divisor = mdc(num, den)
    if den < 0:
        num = -num
        den = -den
    return num // divisor, den // divisor

def geratriz_dizima(entrada):
    """Calcula a fração geratriz de uma dízima no formato A,B(C) ou A,(C)"""
    entrada = entrada.replace(" ", "").replace('.', ',')
    partes = entrada.split(',')
    
    inteiro = partes[0]
    sinal = -1 if inteiro.startswith('-') else 1
    inteiro = inteiro.replace('-', '')
    
    dec_split = partes[1].split('(')
    nao_periodico = dec_split[0]
    periodo = dec_split[1].replace(')', '')
    
    num_str_toda = inteiro + nao_periodico + periodo
    num_str_sub = inteiro + nao_periodico if (inteiro + nao_periodico) else "0"
    
    numerador = int(num_str_toda) - int(num_str_sub)
    denominador = int("9" * len(periodo) + "0" * len(nao_periodico))
    
    return simplificar_fracao(numerador * sinal, denominador), nao_periodico, periodo

def crivo_eratostenes(n):
    """Retorna lista de primos até n."""
    if n < 2: return []
    primos = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primos[p]:
            for i in range(p * p, n + 1, p):
                primos[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primos[p]]

def divisores(n):
    """Retorna lista de divisores de n."""
    if n == 0: return []
    return [i for i in range(1, abs(n) + 1) if n % i == 0]

def classificar_numero(entrada_str):
    """Analisa a string de entrada e exibe a formatação exata pedida, incluindo os bónus."""
    entrada_limpa = entrada_str.strip().replace(" ", "")
    
    conjuntos = []
    tipo = ""
    fracao_geratriz_str = "Não possui (é um número irracional)"
    numero_inteiro = None  # Usado para ativar o bónus automaticamente

    try:
        # 1. É uma RAIZ?
        if entrada_limpa.upper().startswith('V'):
            numero = int(entrada_limpa[1:])
            raiz = math.sqrt(numero)
            if raiz.is_integer():
                valor = int(raiz)
                numero_inteiro = valor
                conjuntos = ['N', 'Z', 'Q', 'R']
                tipo = f"número inteiro (raiz exata de {numero})"
                fracao_geratriz_str = f"{valor}/1"
            else:
                conjuntos = ['I', 'R']
                tipo = f"número irracional (raiz não exata de {numero})"
                fracao_geratriz_str = "Não possui"

        # 2. É uma DÍZIMA PERIÓDICA?
        elif '(' in entrada_limpa and ')' in entrada_limpa:
            (num, den), nao_periodico, periodo = geratriz_dizima(entrada_limpa)
            
            if nao_periodico:
                tipo = f"dízima periódica (parte não periódica: {nao_periodico}; período: {periodo})"
            else:
                tipo = f"dízima periódica (período: {periodo})"
                
            fracao_geratriz_str = f"{num}/{den}"
            
            if den == 1: 
                numero_inteiro = num
                if num >= 0: conjuntos = ['N', 'Z', 'Q', 'R']
                else: conjuntos = ['Z', 'Q', 'R']
            else:
                conjuntos = ['Q', 'R']

        # 3. É uma FRAÇÃO?
        elif '/' in entrada_limpa:
            num, den = map(int, entrada_limpa.split('/'))
            s_num, s_den = simplificar_fracao(num, den)
            fracao_geratriz_str = f"{s_num}/{s_den}"
            
            if num % den == 0:
                valor = num // den
                numero_inteiro = valor
                if valor >= 0: conjuntos = ['N', 'Z', 'Q', 'R']
                else: conjuntos = ['Z', 'Q', 'R']
                tipo = "fração (equivalente a um inteiro)"
            else:
                conjuntos = ['Q', 'R']
                tipo = "fração"

        # 4. É um NÚMERO INTEIRO OU DECIMAL EXATO?
        else:
            valor = float(entrada_limpa.replace(',', '.'))
            if valor.is_integer():
                valor_int = int(valor)
                numero_inteiro = valor_int
                fracao_geratriz_str = f"{valor_int}/1"
                
                if valor_int >= 0:
                    conjuntos = ['N', 'Z', 'Q', 'R']
                    tipo = "número natural"
                else:
                    conjuntos = ['Z', 'Q', 'R']
                    tipo = "inteiro negativo"
            else:
                conjuntos = ['Q', 'R']
                tipo = "decimal exato"
                
                partes = entrada_limpa.split(',')
                casas_decimais = len(partes[1]) if len(partes) > 1 else 0
                denominador = 10 ** casas_decimais
                numerador = int(entrada_limpa.replace(',', ''))
                
                s_num, s_den = simplificar_fracao(numerador, denominador)
                fracao_geratriz_str = f"{s_num}/{s_den}"

        # --- SAÍDA FORMATADA ---
        nao_pertence = [c for c in ['N', 'Z', 'Q', 'I', 'R'] if c not in conjuntos]
        
        print(f"\nEntrada: {entrada_str}")
        print(f"Tipo: {tipo}")
        print(f"Fração geratriz: {fracao_geratriz_str}")
        print(f"Pertence a: {', '.join(conjuntos)}")
        print(f"Não pertence a: {', '.join(nao_pertence)}")

        # --- PROCESSAMENTO AUTOMÁTICO DO BÓNUS ---
        print("\n--- BÔNUS ---")
        if numero_inteiro is not None:
            if numero_inteiro >= 2:
                print(f"Primos de N até {numero_inteiro}: {crivo_eratostenes(numero_inteiro)}")
            elif numero_inteiro > 0:
                print(f"Primos de N até {numero_inteiro}: Nenhum primo encontrado neste intervalo.")
            else:
                print("Primos: O Crivo de Eratóstenes aplica-se a naturais maiores ou iguais a 2.")
            
            print(f"Divisores de {numero_inteiro}: {divisores(numero_inteiro)}\n")
        else:
            print("Cálculo de primos e divisores aplica-se apenas a números que representam inteiros.\n")

    except Exception as e:
        print("\n[Erro] Formato inválido! Tente formatos como: 7, -3, 3/4, 0,(3), 1,2(5), V9\n")


def fluxo_principal():
    print("="*50)
    print("   CLASSIFICADOR DE CONJUNTOS NUMÉRICOS")
    print("="*50)
    print("Digite 'sair' para encerrar.")
    
    while True:
        entrada = input("Entrada: ").strip()
        
        if entrada.lower() == 'sair':
            print("A encerrar a Parte 2. Até logo!")
            break
        else:
            classificar_numero(entrada)

if __name__ == "__main__":
    fluxo_principal()