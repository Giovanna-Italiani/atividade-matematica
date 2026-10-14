def pertinencia(x, A):
    """Verifica se x pertence a A (x ∈ A)"""
    for elemento in A:
        if elemento == x:
            return True
    return False

def criar_conjunto(elementos):
    """Remove repetições e cria o conjunto base"""
    conjunto = []
    for e in elementos:
        if not pertinencia(e, conjunto):
            conjunto.append(e)
    return conjunto

def uniao(A, B):
    """A U B: elementos em A V em B"""
    resultado = criar_conjunto(A)
    for e in B:
        if not pertinencia(e, resultado):
            resultado.append(e)
    return resultado

def intersecao(A, B):
    """A ^ B: elementos em A ^ em B"""
    resultado = []
    for e in A:
        if pertinencia(e, B):
            resultado.append(e)
    return resultado

def diferenca(A, B):
    """A - B: elementos em A ^ ~em B"""
    resultado = []
    for e in A:
        if not pertinencia(e, B):
            resultado.append(e)
    return resultado

def diferenca_simetrica(A, B):
    """A Δ B: (A - B) V (B - A)"""
    diff_AB = diferenca(A, B)
    diff_BA = diferenca(B, A)
    return uniao(diff_AB, diff_BA)

def subconjunto(A, B):
    """A ⊆ B: se x ∈ A -> x ∈ B"""
    for e in A:
        if not pertinencia(e, B):
            return False
    return True

def subconjunto_proprio(A, B):
    """A ⊂ B: A ⊆ B ^ A ≠ B"""
    return subconjunto(A, B) and cardinalidade(A) < cardinalidade(B)

def cardinalidade(A):
    """|A|: número de elementos"""
    contador = 0
    for _ in A:
        contador += 1
    return contador

def complemento(A, U):
    """Complemento de A em U: U - A"""
    return diferenca(U, A)

def validar_operacao(nome, res_custom, res_nativo):
    custom_set = set(res_custom) if isinstance(res_custom, list) else res_custom
    status = "APROVADO" if custom_set == res_nativo else "FALHOU"
    print(f"{nome}: Custom={res_custom} | Nativo={list(res_nativo) if isinstance(res_nativo, set) else res_nativo} -> [{status}]")

def ler_conjunto(nome):
    entrada = input(f"Digite os elementos do conjunto {nome} separados por espaço (ou deixe vazio para conjunto vazio): ")
    elementos = []
    for x in entrada.split():
        try:
            elementos.append(int(x))
        except ValueError:
            elementos.append(x)
    return criar_conjunto(elementos)

# --- FLUXO PRINCIPAL ---
def iniciar():
    print("="*45)
    print("    INICIALIZAÇÃO DOS CONJUNTOS")
    print("="*45)
    A = ler_conjunto("A")
    B = ler_conjunto("B")
    
    # O Universo U é definido automaticamente como todos os elementos inseridos
    U = uniao(A, B)
    
    while True:
        print("\n" + "="*45)
        print("    MENU DE OPERAÇÕES - TEORIA DOS CONJUNTOS")
        print("="*45)
        print(f"Conjunto A: {A}")
        print(f"Conjunto B: {B}")
        print(f"Universo U (Automático): {U}")
        print("-" * 45)
        print("1. União (A V B)")
        print("2. Interseção (A ^ B)")
        print("3. Diferença (A - B) e (B - A)")
        print("4. Diferença Simétrica (A Δ B)")
        print("5. Verificação de Pertinência (x ∈ A)")
        print("6. Verificação de Inclusão (A ⊆ B e A ⊂ B)")
        print("7. Cardinalidade e Complemento de A em U")
        print("8. Redefinir Conjuntos A e B")
        print("0. Sair do programa")
        print("=" * 45)
        
        opcao = input("Escolha uma operação: ")

        if opcao == '1':
            res = uniao(A, B)
            validar_operacao("União", res, set(A) | set(B))
        elif opcao == '2':
            res = intersecao(A, B)
            validar_operacao("Interseção", res, set(A) & set(B))
        elif opcao == '3':
            res1 = diferenca(A, B)
            res2 = diferenca(B, A)
            validar_operacao("Diferença (A - B)", res1, set(A) - set(B))
            validar_operacao("Diferença (B - A)", res2, set(B) - set(A))
        elif opcao == '4':
            res = diferenca_simetrica(A, B)
            validar_operacao("Diferença Simétrica", res, set(A) ^ set(B))
        elif opcao == '5':
            x = input("Digite o elemento para verificar se pertence a A: ")
            try: x = int(x)
            except: pass
            res = pertinencia(x, A)
            validar_operacao(f"{x} ∈ A", res, x in set(A))
        elif opcao == '6':
            res_sub = subconjunto(A, B)
            res_proprio = subconjunto_proprio(A, B)
            validar_operacao("A ⊆ B", res_sub, set(A).issubset(set(B)))
            validar_operacao("A ⊂ B", res_proprio, set(A) < set(B))
        elif opcao == '7':
            print(f"|A| (Cardinalidade) Custom: {cardinalidade(A)} | Nativo: {len(set(A))}")
            res_comp = complemento(A, U)
            validar_operacao("Complemento de A em U", res_comp, set(U) - set(A))
        elif opcao == '8':
            print("\nRedefinindo os conjuntos...")
            A = ler_conjunto("A")
            B = ler_conjunto("B")
            U = uniao(A, B)
        elif opcao == '0':
            print("Encerrando a Parte 1. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    iniciar()