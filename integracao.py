# ==============================================================================
# PARTE 3 - MINI-PROJETO 2: CONTROLE DE ACESSO POR PERFIS (RBAC)
# Aplicação Fictícia: Gestão e Controle de Acessos com Teoria dos Conjuntos
# ==============================================================================

# Definição dos perfis base do sistema através de conjuntos (set)
PERFIS_BASE = {
    "leitor": {"ler"},
    "editor": {"ler", "editar"},
    "admin": {"ler", "editar", "excluir", "gerir_usuarios"}
}

def calcular_permissoes(perfis_atribuidos):
    """Calcula a união (U) das permissões de todos os perfis atribuídos."""
    permissoes_consolidadas = set()
    for perfil in perfis_atribuidos:
        perfil = perfil.strip().lower()
        if perfil in PERFIS_BASE:
            permissoes_consolidadas = permissoes_consolidadas.union(PERFIS_BASE[perfil])
    return permissoes_consolidadas

def cadastrar_4_usuarios_iniciais():
    """Recolhe os 4 utilizadores iniciais exigidos pelo fluxo de teste."""
    usuarios = {}
    print("=" * 65)
    print("      CONFIGURAÇÃO INICIAL DO APP: CADASTRO DE 4 UTILIZADORES")
    print("=" * 65)
    print("Perfis base disponíveis no sistema:")
    print(" - leitor: {ler}")
    print(" - editor: {ler, editar}")
    print(" - admin: {ler, editar, excluir, gerir_usuarios}")
    print("Dica: Pode combinar perfis (ex.: 'leitor e editor', 'leitor, editor')")
    print("-" * 65)

    for i in range(1, 5):
        nome = input(f"\nDigite o nome do {i}º utilizador: ").strip()
        while not nome:
            nome = input(f"Nome inválido. Digite o nome do {i}º utilizador: ").strip()
            
        print(f"Perfis disponíveis para {nome}: [leitor, editor, admin]")
        entrada_perfis = input(f"Escolha o(s) perfil(is) para {nome}: ").strip().lower()
        
        # Tratamento da entrada para aceitar múltiplos formatos
        entrada_tratada = entrada_perfis.replace(" e ", ",").replace(" / ", ",")
        perfis_escolhidos = [p.strip() for p in entrada_tratada.split(",") if p.strip()]
        
        perfis_validos = [p for p in perfis_escolhidos if p in PERFIS_BASE]
        if not perfis_validos:
            print("Nenhum perfil válido reconhecido. Atribuído perfil base 'leitor'.")
            perfis_validos = ["leitor"]
            
        permissoes = calcular_permissoes(perfis_validos)
        usuarios[nome] = {
            "perfis": perfis_validos,
            "permissoes": permissoes
        }
        print(f"-> Permissões consolidadas (União) de {nome}: {permissoes}")
        
    return usuarios

def buscar_usuario(usuarios, nome_busca):
    """Auxiliar para encontrar utilizador sem distinção de maiúsculas/minúsculas."""
    for u in usuarios:
        if u.lower() == nome_busca.strip().lower():
            return u
    return None

def adicionar_usuario(usuarios):
    print("\n--- ADICIONAR NOVO UTILIZADOR NO APP ---")
    responsavel = input("Quem está a solicitar a adição do utilizador? ").strip()
    u_resp = buscar_usuario(usuarios, responsavel)
    
    if not u_resp:
        print(f"[ERRO] Utilizador '{responsavel}' não existe no sistema.")
        return

    # Verificação de Pertinência: 'gerir_usuarios' ∈ Permissões
    if "gerir_usuarios" not in usuarios[u_resp]["permissoes"]:
        print(f"\n[ACESSO NEGADO] {u_resp} não tem permissão para gerir utilizadores.")
        print(f"Justificação: 'gerir_usuarios' ∉ {usuarios[u_resp]['permissoes']}")
        return

    print(f"\n[ACESSO AUTORIZADO] {u_resp} possui 'gerir_usuarios' ∈ Permissões.")
    novo_nome = input("Digite o nome do novo utilizador: ").strip()
    if not novo_nome or buscar_usuario(usuarios, novo_nome):
        print("[ERRO] Nome inválido ou já registado.")
        return

    entrada_perfis = input(f"Escolha o(s) perfil(is) para {novo_nome} (leitor, editor, admin): ").strip().lower()
    entrada_tratada = entrada_perfis.replace(" e ", ",").replace(" / ", ",")
    perfis_escolhidos = [p.strip() for p in entrada_tratada.split(",") if p.strip()]
    perfis_validos = [p for p in perfis_escolhidos if p in PERFIS_BASE] or ["leitor"]

    permissoes = calcular_permissoes(perfis_validos)
    usuarios[novo_nome] = {
        "perfis": perfis_validos,
        "permissoes": permissoes
    }
    print(f"[SUCESSO] Utilizador '{novo_nome}' adicionado com as permissões: {permissoes}")

def remover_usuario(usuarios):
    print("\n--- EXCLUIR UTILIZADOR DO APP ---")
    responsavel = input("Quem está a solicitar a exclusão? ").strip()
    u_resp = buscar_usuario(usuarios, responsavel)
    
    if not u_resp:
        print(f"[ERRO] Utilizador '{responsavel}' não existe no sistema.")
        return

    # Verificação de Pertinência: 'excluir' ∈ Permissões
    if "excluir" not in usuarios[u_resp]["permissoes"]:
        print(f"\n[ACESSO NEGADO] {u_resp} não pode excluir pessoas.")
        print(f"Justificação: 'excluir' ∉ {usuarios[u_resp]['permissoes']}")
        return

    print(f"\n[ACESSO AUTORIZADO] {u_resp} possui 'excluir' ∈ Permissões.")
    alvo = input("Digite o nome do utilizador a ser excluído: ").strip()
    u_alvo = buscar_usuario(usuarios, alvo)
    
    if not u_alvo:
        print(f"[ERRO] Utilizador '{alvo}' não encontrado.")
        return
    
    if u_alvo == u_resp:
        print("[AVISO] Não pode excluir o seu próprio utilizador.")
        return

    del usuarios[u_alvo]
    print(f"[SUCESSO] O utilizador '{u_alvo}' foi removido do aplicativo.")

def menu_principal(usuarios):
    while True:
        print("\n" + "=" * 65)
        print("          PAINEL DE CONTROLO DO APLICATIVO FICTÍCIO")
        print("=" * 65)
        print("1. Consultar se um utilizador pode executar uma ação (ex.: A Ana pode editar?)")
        print("2. Consultar quem pode executar uma ação (ex.: Quem pode editar?)")
        print("3. Adicionar utilizador (Requer perfil com permissão 'gerir_usuarios')")
        print("4. Excluir utilizador (Requer perfil com permissão 'excluir')")
        print("5. Verificar hierarquia entre perfis (A ⊆ B)")
        print("6. Listar todos os utilizadores e permissões")
        print("0. Sair")
        print("-" * 65)
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            nome_busca = input("Qual utilizador deseja consultar? ").strip()
            u_encontrado = buscar_usuario(usuarios, nome_busca)
            
            if u_encontrado:
                acao = input(f"Ação a verificar para {u_encontrado} (ler, editar, excluir, gerir_usuarios): ").strip().lower()
                permissoes = usuarios[u_encontrado]["permissoes"]
                
                if acao in permissoes:
                    print(f"\n[SIM] {u_encontrado} PODE '{acao}'.")
                    print(f"Justificação matemática: '{acao}' ∈ {permissoes}")
                else:
                    print(f"\n[NÃO] {u_encontrado} NÃO PODE '{acao}'.")
                    print(f"Justificação matemática: '{acao}' ∉ {permissoes}")
            else:
                print(f"Utilizador '{nome_busca}' não encontrado.")

        elif opcao == '2':
            acao = input("Deseja saber quem pode realizar qual ação? ").strip().lower()
            autorizados = [u for u, dados in usuarios.items() if acao in dados["permissoes"]]
            if autorizados:
                print(f"\nUtilizadores autorizados para '{acao}': {', '.join(autorizados)}")
            else:
                print(f"\nNenhum utilizador tem permissão para '{acao}'.")

        elif opcao == '3':
            adicionar_usuario(usuarios)

        elif opcao == '4':
            remover_usuario(usuarios)

        elif opcao == '5':
            print("\nPerfis base: leitor, editor, admin")
            p1 = input("Perfil A: ").strip().lower()
            p2 = input("Perfil B: ").strip().lower()
            
            if p1 in PERFIS_BASE and p2 in PERFIS_BASE:
                conj_a = PERFIS_BASE[p1]
                conj_b = PERFIS_BASE[p2]
                e_sub = conj_a.issubset(conj_b)
                print(f"\n{p1} ⊆ {p2}? {e_sub}")
                print(f"Detalhe: {p1} = {conj_a} | {p2} = {conj_b}")
            else:
                print("Perfil não reconhecido.")

        elif opcao == '6':
            print("\n" + "-" * 60)
            print(f"{'Utilizador':<15} | {'Perfis':<20} | {'Permissões (União)'}")
            print("-" * 60)
            for u, dados in usuarios.items():
                perfis_str = ", ".join(dados["perfis"])
                perm_str = ", ".join(dados["permissoes"])
                print(f"{u:<15} | {perfis_str:<20} | {{{perm_str}}}")
            print("-" * 60)

        elif opcao == '0':
            print("A encerrar o sistema do aplicativo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    banco_usuarios = cadastrar_4_usuarios_iniciais()
    menu_principal(banco_usuarios)