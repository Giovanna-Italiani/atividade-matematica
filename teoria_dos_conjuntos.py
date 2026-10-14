
def pertinencia(x, A):
    """Verifica se x pertence a A (x ∈ A)."""
    for elemento in A:
        if elemento == x:
            return True
    return False


def criar_conjunto(elementos):
    """Remove repetições e cria um conjunto representado por lista."""
    conjunto = []

    for elemento in elementos:
        if not pertinencia(elemento, conjunto):
            conjunto.append(elemento)

    return conjunto


def uniao(A, B):
    """Retorna A ∪ B."""
    resultado = criar_conjunto(A)

    for elemento in B:
        if not pertinencia(elemento, resultado):
            resultado.append(elemento)

    return resultado


def intersecao(A, B):
    """Retorna A ∩ B."""
    resultado = []

    for elemento in A:
        if pertinencia(elemento, B):
            if not pertinencia(elemento, resultado):
                resultado.append(elemento)

    return resultado


def diferenca(A, B):
    """Retorna A - B."""
    resultado = []

    for elemento in A:
        if not pertinencia(elemento, B):
            if not pertinencia(elemento, resultado):
                resultado.append(elemento)

    return resultado


def diferenca_simetrica(A, B):
    """Retorna A Δ B = (A - B) ∪ (B - A)."""
    diferenca_AB = diferenca(A, B)
    diferenca_BA = diferenca(B, A)

    return uniao(diferenca_AB, diferenca_BA)


def subconjunto(A, B):
    """Verifica se A ⊆ B."""
    for elemento in A:
        if not pertinencia(elemento, B):
            return False

    return True


def subconjunto_proprio(A, B):
    """Verifica se A ⊂ B."""
    return (
        subconjunto(A, B)
        and cardinalidade(A) < cardinalidade(B)
    )


def cardinalidade(A):
    """Conta a quantidade de elementos distintos de A."""
    contador = 0

    for elemento in A:
        if not pertinencia(elemento, A[:contador]):
            contador += 1

    return contador


def complemento(A, U):
    """Retorna o complemento de A em U: U - A."""
    return diferenca(U, A)


def validar_operacao(nome, res_custom, res_nativo):
    """Compara o resultado personalizado com o nativo."""
    if isinstance(res_custom, list):
        custom_set = set(res_custom)
    else:
        custom_set = res_custom

    status = "APROVADO" if custom_set == res_nativo else "FALHOU"

    if isinstance(res_nativo, set):
        nativo_exibido = sorted(
            res_nativo, key=lambda x: (type(x).__name__, str(x))
        )
    else:
        nativo_exibido = res_nativo

    print(
        f"{nome}: Custom={res_custom} | "
        f"Nativo={nativo_exibido} -> [{status}]"
    )


def ler_conjunto(nome):
    """Lê os elementos informados e elimina repetições."""
    entrada = input(
        f"Digite os elementos do conjunto {nome}, "
        "separados por espaço (ou deixe vazio): "
    )

    elementos = []

    for elemento in entrada.split():
        try:
            elementos.append(int(elemento))
        except ValueError:
            elementos.append(elemento)

    return criar_conjunto(elementos)


def iniciar():
    print("=" * 50)
    print("      INICIALIZAÇÃO DOS CONJUNTOS")
    print("=" * 50)

    A = ler_conjunto("A")
    B = ler_conjunto("B")

    # Universo automático: U = A ∪ B
    U = uniao(A, B)

    while True:
        print("\n" + "=" * 50)
        print("       MENU - TEORIA DOS CONJUNTOS")
        print("=" * 50)
        print(f"Conjunto A: {A}")
        print(f"Conjunto B: {B}")
        print(f"Universo U: {U}")
        print("-" * 50)
        print("1. União (A ∪ B)")
        print("2. Interseção (A ∩ B)")
        print("3. Diferença (A - B e B - A)")
        print("4. Diferença simétrica (A Δ B)")
        print("5. Verificar pertinência (x ∈ A)")
        print("6. Verificar inclusão (A ⊆ B e A ⊂ B)")
        print("7. Cardinalidade e complemento de A em U")
        print("8. Redefinir conjuntos A e B")
        print("0. Sair")
        print("=" * 50)

        opcao = input("Escolha uma operação: ").strip()

        if opcao == "1":
            resultado = uniao(A, B)
            validar_operacao(
                "União", resultado, set(A) | set(B)
            )

        elif opcao == "2":
            resultado = intersecao(A, B)
            validar_operacao(
                "Interseção", resultado, set(A) & set(B)
            )

        elif opcao == "3":
            resultado_AB = diferenca(A, B)
            resultado_BA = diferenca(B, A)

            validar_operacao(
                "Diferença (A - B)",
                resultado_AB,
                set(A) - set(B)
            )

            validar_operacao(
                "Diferença (B - A)",
                resultado_BA,
                set(B) - set(A)
            )

        elif opcao == "4":
            resultado = diferenca_simetrica(A, B)
            validar_operacao(
                "Diferença simétrica",
                resultado,
                set(A) ^ set(B)
            )

        elif opcao == "5":
            entrada = input(
                "Digite o elemento para verificar se pertence a A: "
            )

            try:
                elemento = int(entrada)
            except ValueError:
                elemento = entrada

            resultado = pertinencia(elemento, A)

            validar_operacao(
                f"{elemento} ∈ A",
                resultado,
                elemento in set(A)
            )

        elif opcao == "6":
            resultado_subconjunto = subconjunto(A, B)
            resultado_proprio = subconjunto_proprio(A, B)

            validar_operacao(
                "A ⊆ B",
                resultado_subconjunto,
                set(A).issubset(set(B))
            )

            validar_operacao(
                "A ⊂ B",
                resultado_proprio,
                set(A) < set(B)
            )

        elif opcao == "7":
            cardinalidade_custom = cardinalidade(A)
            cardinalidade_nativa = len(set(A))

            validar_operacao(
                "Cardinalidade de A",
                cardinalidade_custom,
                cardinalidade_nativa
            )

            resultado_complemento = complemento(A, U)

            validar_operacao(
                "Complemento de A em U",
                resultado_complemento,
                set(U) - set(A)
            )

        elif opcao == "8":
            print("\nRedefinindo os conjuntos...")

            A = ler_conjunto("A")
            B = ler_conjunto("B")
            U = uniao(A, B)

        elif opcao == "0":
            print("Encerrando o programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    iniciar()
