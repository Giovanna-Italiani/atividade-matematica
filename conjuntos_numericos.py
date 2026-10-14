import math

# Configuração: Altere para False caso a convenção da sua disciplina NÃO inclua o 0 nos Naturais (N)
ZERO_EH_NATURAL = True


def mdc(a, b):
    """Calcula o Máximo Divisor Comum (para simplificar frações)."""
    while b:
        a, b = b, a % b
    return abs(a)


def simplificar_fracao(num, den):
    """Simplifica uma fração e garante que o sinal fique apenas no numerador."""
    divisor = mdc(num, den)
    if den < 0:
        num = -num
        den = -den
    return num // divisor, den // divisor


def obter_conjuntos_inteiro(valor):
    """Retorna a lista de conjuntos para um número inteiro, respeitando a convenção do zero."""
    if valor > 0 or (valor == 0 and ZERO_EH_NATURAL):
        return ['N', 'Z', 'Q', 'R']
    return ['Z', 'Q', 'R']


def geratriz_dizima(entrada):
    """Calcula a fração geratriz de uma dízima no formato A,B(C) ou A,(C)."""
    entrada = entrada.replace(" ", "").replace('.', ',')
    if ',' not in entrada:
        raise ValueError("Formato de dízima inválido.")

    partes = entrada.split(',')
    inteiro_str = partes[0]
    sinal = -1 if inteiro_str.startswith('-') else 1
    inteiro_limpo = inteiro_str.lstrip('+-') or "0"

    if '(' not in partes[1] or not partes[1].endswith(')'):
        raise ValueError("Formato de período inválido.")

    dec_split = partes[1].split('(')
    nao_periodico = dec_split[0]
    periodo = dec_split[1][:-1]  # Remove o ')' final

    if not periodo.isdigit() or (nao_periodico and not nao_periodico.isdigit()) or not inteiro_limpo.isdigit():
        raise ValueError("Os componentes da dízima devem conter apenas dígitos.")

    num_str_toda = inteiro_limpo + nao_periodico + periodo
    num_str_sub = inteiro_limpo + nao_periodico

    numerador = int(num_str_toda) - int(num_str_sub)
    denominador = int("9" * len(periodo) + "0" * len(nao_periodico))

    return simplificar_fracao(numerador * sinal, denominador), nao_periodico, periodo


def crivo_eratostenes(n):
    """Retorna lista de primos até n."""
    if n < 2:
        return []
    primos = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primos[p]:
            for i in range(p * p, n + 1, p):
                primos[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primos[p]]


def divisores(n):
    """Retorna lista de divisores positivos de n (para n != 0)."""
    if n == 0:
        return []
    return [i for i in range(1, abs(n) + 1) if n % i == 0]


def classificar_numero(entrada_str):
    """Analisa a string de entrada e exibe a formatação exata pedida, incluindo os bônus."""
    entrada_limpa = entrada_str.strip().replace(" ", "")

    conjuntos = []
    tipo = ""
    fracao_geratriz_str = "Não possui (é um número irracional)"
    numero_inteiro = None  # Usado para ativar o bônus automaticamente

    try:
        # 1. É uma RAIZ?
        if entrada_limpa.upper().startswith('V'):
            numero = int(entrada_limpa[1:])

            # Problema 3 corrigido: Trata raízes de números negativos explicitamente
            if numero < 0:
                print(f"\nEntrada: {entrada_str}")
                print("Erro: Raiz quadrada de número negativo não possui resultado no conjunto dos números reais (R).\n")
                return

            raiz = math.isqrt(numero)
            if raiz * raiz == numero:
                valor = raiz
                numero_inteiro = valor
                conjuntos = obter_conjuntos_inteiro(valor)
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
                conjuntos = obter_conjuntos_inteiro(num)
            else:
                conjuntos = ['Q', 'R']

        # 3. É uma FRAÇÃO?
        elif '/' in entrada_limpa:
            num, den = map(int, entrada_limpa.split('/'))

            # Problema 2 corrigido: Verifica denominador zero logo após separar a fração
            if den == 0:
                print("\nErro: o denominador não pode ser zero.\n")
                return

            s_num, s_den = simplificar_fracao(num, den)
            fracao_geratriz_str = f"{s_num}/{s_den}"

            # Problema 4 corrigido: Fração aparente (ex: 6/3) é reconhecida como inteiro
            if s_den == 1:
                valor = s_num
                numero_inteiro = valor
                conjuntos = obter_conjuntos_inteiro(valor)
                tipo = "fração (equivalente a um inteiro)"
            else:
                conjuntos = ['Q', 'R']
                tipo = "fração"

        # 4. É um NÚMERO INTEIRO OU DECIMAL EXATO?
        else:
            # Problema 1 corrigido: Padroniza vírgula e ponto antes de converter e calcular a geratriz
            entrada_ponto = entrada_limpa.replace(',', '.')
            valor = float(entrada_ponto)

            if '.' not in entrada_ponto or valor.is_integer():
                valor_int = int(valor)
                numero_inteiro = valor_int
                fracao_geratriz_str = f"{valor_int}/1"
                conjuntos = obter_conjuntos_inteiro(valor_int)

                if valor_int >= 0:
                    tipo = "número natural" if (valor_int > 0 or ZERO_EH_NATURAL) else "número inteiro"
                else:
                    tipo = "inteiro negativo"
            else:
                conjuntos = ['Q', 'R']
                tipo = "decimal exato"

                partes = entrada_ponto.split('.')
                casas_decimais = len(partes[1]) if len(partes) > 1 else 0
                denominador = 10 ** casas_decimais
                numerador = int(entrada_ponto.replace('.', ''))

                s_num, s_den = simplificar_fracao(numerador, denominador)
                fracao_geratriz_str = f"{s_num}/{s_den}"

        # --- SAÍDA FORMATADA ---
        nao_pertence = [c for c in ['N', 'Z', 'Q', 'I', 'R'] if c not in conjuntos]

        print(f"\nEntrada: {entrada_str}")
        print(f"Tipo: {tipo}")
        print(f"Fração geratriz: {fracao_geratriz_str}")
        print(f"Pertence a: {', '.join(conjuntos)}")
        print(f"Não pertence a: {', '.join(nao_pertence)}")

        # --- PROCESSAMENTO AUTOMÁTICO DO BÔNUS ---
        print("\n--- BÔNUS ---")
        if numero_inteiro is not None:
            if numero_inteiro >= 2:
                print(f"Primos de N até {numero_inteiro}: {crivo_eratostenes(numero_inteiro)}")
            elif numero_inteiro >= 0:
                print(f"Primos de N até {numero_inteiro}: Nenhum primo encontrado neste intervalo.")
            else:
                print("Primos: O Crivo de Eratóstenes aplica-se a naturais maiores ou iguais a 2.")

            if numero_inteiro != 0:
                print(f"Divisores de {numero_inteiro}: {divisores(numero_inteiro)}\n")
            else:
                print("Divisores de 0: Todos os inteiros diferentes de zero são divisores de 0.\n")
        else:
            print("Cálculo de primos e divisores aplica-se apenas a números que representam inteiros.\n")

    except Exception:
        print("\n[Erro] Formato inválido! Tente formatos como: 7, -3, 1.25, 1,25, 3/4, 0,(3), 1,2(5), V9\n")


def fluxo_principal():
    print("=" * 50)
    print("   CLASSIFICADOR DE CONJUNTOS NUMÉRICOS")
    print("=" * 50)
    print("Digite 'sair' para encerrar.")

    while True:
        entrada = input("Entrada: ").strip()

        if entrada.lower() == 'sair':
            print("A encerrar a Parte 2. Até logo!")
            break
        elif entrada:
            classificar_numero(entrada)


if __name__ == "__main__":
    fluxo_principal()