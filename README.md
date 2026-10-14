# Laboratório de Conjuntos: Teoria dos Conjuntos e Conjuntos Numéricos

**Curso:** Desenvolvimento de Software Multiplataforma — FATEC Osasco  
**Linguagem:** Python  
**Autores:** Giovanna Faria Italiani e Everton Freitas

---

## 📌 Descrição da Atividade

Esta atividade prática tem como objetivo aplicar os conceitos matemáticos de **Teoria dos Conjuntos** e **Conjuntos Numéricos** na resolução de problemas de programação estruturada e modelagem de regras de negócio em sistemas.

O projeto foi dividido em três partes progressivas:
1. **Parte 1 (Teoria dos Conjuntos):** Implementação de operações elementares com conjuntos (união, interseção, diferença, diferença simétrica, pertinência, subconjunto e complemento) sem a utilização dos operadores prontos da linguagem, comparando posteriormente a saída manual com a solução nativa do Python para validação algorítmica.
2. **Parte 2 (Conjuntos Numéricos):** Desenvolvimento de um classificador numérico capaz de categorizar entradas nos conjuntos $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{I}$ e $\mathbb{R}$, tratar entradas de decimais (com ponto ou vírgula), calcular frações irredutíveis e frações geratrizes de dízimas periódicas simples e compostas, validar casos de exceção matemática (divisão por zero e raízes de números negativos), além de gerar números primos via Crivo de Eratóstenes e listar divisores inteiros.
3. **Parte 3 (Integração - Mini-projeto 2):** Implementação de um sistema de controle de acesso baseado em funções/perfis (RBAC) para um aplicativo fictício, demonstrando na prática como a agregação de papéis utiliza a união de conjuntos e a verificação de permissões utiliza a pertinência lógica ($\in$).

---

## 🛠️ Decisões Tomadas e Justificativas Técnicas

### 1. Mapeamento Lógico-Formal
Para consolidar os operadores lógicos abordados em aula, o código e as saídas foram alinhados às seguintes definições:
- **Negação ($\sim$):** Utilizada no filtro da diferença ($A - B = \{x \mid x \in A \land \sim(x \in B)\}$).
- **Disjunção ($\lor$):** Utilizada na composição da união ($A \cup B = \{x \mid x \in A \lor x \in B\}$).
- **Conjunção ($\land$):** Utilizada na determinação da interseção ($A \cap B = \{x \mid x \in A \land x \in B\}$).
- **Condicional ($\rightarrow$):** Utilizada para a relação de inclusão ($A \subseteq B \iff \forall x (x \in A \rightarrow x \in B)$).

### 2. Implementação Manual vs. Validação Nativa (Parte 1)
- **Desafio dos Algoritmos Manuais (Custom):** Foi criada uma coleção de funções desenvolvidas apenas com estruturas de repetição (`for`) e testes condicionais (`if`), iterando sobre listas puras para garantir que as operações fossem executadas passo a passo a partir da sua definição matemática fundamental.
- **Eliminação de Repetições:** Na entrada dos conjuntos, foi implementada uma função de sanitização que descarta elementos duplicados, respeitando a definição fundamental de conjunto.
- **Validação Cruzada (Nativo):** Para cumprir a exigência de validação matemática do enunciado, cada resultado manual é confrontado em tempo de execução com o resultado correspondente gerado pelas funções e operadores nativos do Python (`set`, `|`, `&`, `-`, `^`, `.issubset()`), emitindo uma confirmação automática de equivalência.
- **Conjunto Universo Dinâmico ($U$):** Em vez de exigir a digitação manual de um universo arbitrário, o sistema assume como Universo $U$ todos os elementos fornecidos entre os conjuntos $A$ e $B$ ($U = A \cup B$), viabilizando o cálculo determinístico do complementar ($U - A$).

### 3. Decomposição e Classificação Numérica (Parte 2)
- **Padronização de Decimais Exatos:** A entrada numérica aceita tanto vírgula (ex.: `1,25`) quanto ponto (ex.: `1.25`), padronizando o separador decimal internamente antes de calcular o numerador e a potência de base 10 do denominador para obter a fração geratriz simplificada.
- **Algoritmo da Fração Geratriz (Dízimas):** Para dízimas simples no formato $A,(C)$ e compostas no formato $A,B(C)$, a fração geratriz é calculada algebricamente subtraindo a parte não periódica da junção completa dos dígitos e aplicando ao denominador a quantidade correspondente de noves ($9$) e zeros ($0$). Todas as frações são simplificadas via Algoritmo de Euclides (MDC).
- **Caso Específico $0,(9)$ e Frações Aparentes:** O algoritmo reconhece que a fração geratriz de $0,(9)$ resulta em $9/9 = 1/1$ e que frações aparentes como $6/3$ simplificam para $2/1$, integrando esses valores aos conjuntos dos Inteiros ($\mathbb{Z}$) e Naturais ($\mathbb{N}$).
- **Tratamento de Restrições no Conjunto dos Reais ($\mathbb{R}$):**
  * **Divisão por zero:** Frações com denominador igual a zero (ex.: `3/0`) são interceptadas antes da simplificação, exibindo um alerta específico de indeterminação/impossibilidade matemática.
  * **Raízes de números negativos:** Entradas como `V-4` são validadas antes do cálculo da raiz quadrada, informando explicitamente que raízes quadradas de números negativos não possuem resultado no conjunto dos números reais ($\mathbb{R}$).
- **Convenção Numérica:** Foi adotada a convenção de que o número zero pertence ao conjunto dos números naturais ($0 \in \mathbb{N}$), configurável no código pela constante `ZERO_EH_NATURAL`.
- **Bônus Automatizado:** Sempre que a entrada numérica representar um valor inteiro (seja digitado diretamente, via fração aparente ou raiz exata), o Crivo de Eratóstenes (para $n \ge 2$) e a listagem de divisores são executados automaticamente.

### 4. Gestão de Perfis e Permissões no App Fictício (Parte 3)
- **Estrutura de Perfis:** Os papéis foram definidos como conjuntos:
  * `leitor`: `{"ler"}`
  * `editor`: `{"ler", "editar"}`
  * `admin`: `{"ler", "editar", "excluir", "gerir_usuarios"}`
- **Composição de Permissões por União:** Quando um usuário acumula múltiplos perfis (por exemplo, `leitor e editor`), o sistema calcula a união das permissões para definir os acessos finais.
- **Controle de Execução por Pertinência:** As operações críticas no aplicativo (adicionar novo usuário ou remover usuário existente) exigem a verificação prévia de pertinência ($\in$) das ações `'gerir_usuarios'` e `'excluir'`, bloqueando o acesso de perfis não autorizados com justificativa matemática explícita.

---

## 📷 Exemplos de Execução

### Parte 1: Teoria dos Conjuntos

#### Exemplo 1: Caso Geral, Conjunto Vazio e Conjuntos Iguais

```text
==================================================
      INICIALIZAÇÃO DOS CONJUNTOS
==================================================
Digite os elementos do conjunto A, separados por espaço (ou deixe vazio): 1 2 3
Digite os elementos do conjunto B, separados por espaço (ou deixe vazio): 2 3 4

==================================================
       MENU - TEORIA DOS CONJUNTOS
==================================================
Conjunto A: [1, 2, 3]
Conjunto B: [2, 3, 4]
Universo U: [1, 2, 3, 4]
--------------------------------------------------
1. União (A ∪ B)
2. Interseção (A ∩ B)
3. Diferença (A - B e B - A)
4. Diferença simétrica (A Δ B)
5. Verificar pertinência (x ∈ A)
6. Verificar inclusão (A ⊆ B e A ⊂ B)
7. Cardinalidade e complemento de A em U
8. Redefinir conjuntos A e B
0. Sair
==================================================
Escolha uma operação: 1
União: Custom=[1, 2, 3, 4] | Nativo=[1, 2, 3, 4] -> [APROVADO]

==================================================
Escolha uma operação: 2
Interseção: Custom=[2, 3] | Nativo=[2, 3] -> [APROVADO]

==================================================
Escolha uma operação: 3
Diferença (A - B): Custom=[1] | Nativo=[1] -> [APROVADO]
Diferença (B - A): Custom=[4] | Nativo=[4] -> [APROVADO]

==================================================
Escolha uma operação: 4
Diferença simétrica: Custom=[1, 4] | Nativo=[1, 4] -> [APROVADO]

==================================================
Escolha uma operação: 8

Redefinindo os conjuntos...
Digite os elementos do conjunto A, separados por espaço (ou deixe vazio): 
Digite os elementos do conjunto B, separados por espaço (ou deixe vazio): 2 3 4

==================================================
       MENU - TEORIA DOS CONJUNTOS
==================================================
Conjunto A: []
Conjunto B: [2, 3, 4]
Universo U: [2, 3, 4]
--------------------------------------------------
Escolha uma operação: 1
União: Custom=[2, 3, 4] | Nativo=[2, 3, 4] -> [APROVADO]

Escolha uma operação: 2
Interseção: Custom=[] | Nativo=[] -> [APROVADO]

Escolha uma operação: 3
Diferença (A - B): Custom=[] | Nativo=[] -> [APROVADO]
Diferença (B - A): Custom=[2, 3, 4] | Nativo=[2, 3, 4] -> [APROVADO]

==================================================
Escolha uma operação: 8

Redefinindo os conjuntos...
Digite os elementos do conjunto A, separados por espaço (ou deixe vazio): 1 2 3
Digite os elementos do conjunto B, separados por espaço (ou deixe vazio): 1 2 3

==================================================
       MENU - TEORIA DOS CONJUNTOS
==================================================
Conjunto A: [1, 2, 3]
Conjunto B: [1, 2, 3]
Universo U: [1, 2, 3]
--------------------------------------------------
Escolha uma operação: 1
União: Custom=[1, 2, 3] | Nativo=[1, 2, 3] -> [APROVADO]

Escolha uma operação: 2
Interseção: Custom=[1, 2, 3] | Nativo=[1, 2, 3] -> [APROVADO]

Escolha uma operação: 3
Diferença (A - B): Custom=[] | Nativo=[] -> [APROVADO]
Diferença (B - A): Custom=[] | Nativo=[] -> [APROVADO]

Escolha uma operação: 0
```

---

### Parte 2: Conjuntos Numéricos

#### Exemplos de Classificação (Inteiros, Decimais com Ponto/Vírgula, Frações, Dízimas, Raízes e Erros Tratados)

```text
==================================================
   CLASSIFICADOR DE CONJUNTOS NUMÉRICOS
==================================================
Digite 'sair' para encerrar.
Entrada: 7

Entrada: 7
Tipo: número natural
Fração geratriz: 7/1
Pertence a: N, Z, Q, R
Não pertence a: I

--- BÔNUS ---
Primos de N até 7: [2, 3, 5, 7]
Divisores de 7: [1, 7]

Entrada: 0

Entrada: 0
Tipo: número natural
Fração geratriz: 0/1
Pertence a: N, Z, Q, R
Não pertence a: I

--- BÔNUS ---
Primos de N até 0: Nenhum primo encontrado neste intervalo.
Divisores de 0: Todos os inteiros diferentes de zero são divisores de 0.

Entrada: -8

Entrada: -8
Tipo: inteiro negativo
Fração geratriz: -8/1
Pertence a: Z, Q, R
Não pertence a: N, I

--- BÔNUS ---
Primos: O Crivo de Eratóstenes aplica-se a naturais maiores ou iguais a 2.
Divisores de -8: [1, 2, 4, 8]

Entrada: 1,25

Entrada: 1,25
Tipo: decimal exato
Fração geratriz: 5/4
Pertence a: Q, R
Não pertence a: N, Z, I

--- BÔNUS ---
Cálculo de primos e divisores aplica-se apenas a números que representam inteiros.

Entrada: 1.25

Entrada: 1.25
Tipo: decimal exato
Fração geratriz: 5/4
Pertence a: Q, R
Não pertence a: N, Z, I

--- BÔNUS ---
Cálculo de primos e divisores aplica-se apenas a números que representam inteiros.

Entrada: 3/4

Entrada: 3/4
Tipo: fração
Fração geratriz: 3/4
Pertence a: Q, R
Não pertence a: N, Z, I

--- BÔNUS ---
Cálculo de primos e divisores aplica-se apenas a números que representam inteiros.

Entrada: 6/3

Entrada: 6/3
Tipo: fração (equivalente a um inteiro)
Fração geratriz: 2/1
Pertence a: N, Z, Q, R
Não pertence a: I

--- BÔNUS ---
Primos de N até 2: [2]
Divisores de 2: [1, 2]

Entrada: 3/0

Erro: o denominador não pode ser zero.

Entrada: 0,(3)

Entrada: 0,(3)
Tipo: dízima periódica (período: 3)
Fração geratriz: 1/3
Pertence a: Q, R
Não pertence a: N, Z, I

--- BÔNUS ---
Cálculo de primos e divisores aplica-se apenas a números que representam inteiros.

Entrada: 0,(6)

Entrada: 0,(6)
Tipo: dízima periódica (período: 6)
Fração geratriz: 2/3
Pertence a: Q, R
Não pertence a: N, Z, I

--- BÔNUS ---
Cálculo de primos e divisores aplica-se apenas a números que representam inteiros.

Entrada: 1,2(5)

Entrada: 1,2(5)
Tipo: dízima periódica (parte não periódica: 2; período: 5)
Fração geratriz: 113/90
Pertence a: Q, R
Não pertence a: N, Z, I

--- BÔNUS ---
Cálculo de primos e divisores aplica-se apenas a números que representam inteiros.

Entrada: 0,1(6)

Entrada: 0,1(6)
Tipo: dízima periódica (parte não periódica: 1; período: 6)
Fração geratriz: 1/6
Pertence a: Q, R
Não pertence a: N, Z, I

--- BÔNUS ---
Cálculo de primos e divisores aplica-se apenas a números que representam inteiros.

Entrada: 0,(9)

Entrada: 0,(9)
Tipo: dízima periódica (período: 9)
Fração geratriz: 1/1
Pertence a: N, Z, Q, R
Não pertence a: I

--- BÔNUS ---
Primos de N até 1: Nenhum primo encontrado neste intervalo.
Divisores de 1: [1]

Entrada: V9

Entrada: V9
Tipo: número inteiro (raiz exata de 9)
Fração geratriz: 3/1
Pertence a: N, Z, Q, R
Não pertence a: I

--- BÔNUS ---
Primos de N até 3: [2, 3]
Divisores de 3: [1, 3]

Entrada: V2

Entrada: V2
Tipo: número irracional (raiz não exata de 2)
Fração geratriz: Não possui
Pertence a: I, R
Não pertence a: N, Z, Q

--- BÔNUS ---
Cálculo de primos e divisores aplica-se apenas a números que representam inteiros.

Entrada: V-4

Entrada: V-4
Erro: Raiz quadrada de número negativo não possui resultado no conjunto dos números reais (R).

Entrada: sair
A encerrar a Parte 2. Até logo!
```

---

### Parte 3: Integração (Controle de Acesso por Perfis)

#### Cadastro e Resolução de Permissões dos 4 Usuários

```text
=================================================================
      CONFIGURAÇÃO INICIAL DO APP: CADASTRO DE 4 UTILIZADORES
=================================================================
Perfis base disponíveis no sistema:
 - leitor: {ler}
 - editor: {ler, editar}
 - admin: {ler, editar, excluir, gerir_usuarios}
Dica: Pode combinar perfis (ex.: 'leitor e editor', 'leitor, editor')
-----------------------------------------------------------------

Digite o nome do 1º utilizador: Ana
Perfis disponíveis para Ana: [leitor, editor, admin]
Escolha o(s) perfil(is) para Ana: leitor
-> Permissões consolidadas (União) de Ana: {'ler'}

Digite o nome do 2º utilizador: Giovanna
Perfis disponíveis para Giovanna: [leitor, editor, admin]
Escolha o(s) perfil(is) para Giovanna: editor
-> Permissões consolidadas (União) de Giovanna: {'editar', 'ler'}

Digite o nome do 3º utilizador: Roberto
Perfis disponíveis para Roberto: [leitor, editor, admin]
Escolha o(s) perfil(is) para Roberto: admin
-> Permissões consolidadas (União) de Roberto: {'gerir_usuarios', 'editar', 'ler', 'excluir'}

Digite o nome do 4º utilizador: Kaiki
Perfis disponíveis para Kaiki: [leitor, editor, admin]
Escolha o(s) perfil(is) para Kaiki: admin
-> Permissões consolidadas (União) de Kaiki: {'gerir_usuarios', 'editar', 'ler', 'excluir'}

=================================================================
          PAINEL DE CONTROLE DO APLICATIVO FICTÍCIO
=================================================================
1. Consultar se um utilizador pode executar uma ação (ex.: A Ana pode editar?)
2. Consultar quem pode executar uma ação (ex.: Quem pode editar?)
3. Adicionar utilizador (Requer perfil com permissão 'gerir_usuarios')
4. Excluir utilizador (Requer perfil com permissão 'excluir')
5. Verificar hierarquia entre perfis (A ⊆ B)
6. Listar todos os utilizadores e permissões
0. Sair
-----------------------------------------------------------------
Escolha uma opção: 1
Qual utilizador deseja consultar? Ana
Ação a verificar para Ana (ler, editar, excluir, gerir_usuarios): excluir

[NÃO] Ana NÃO PODE 'excluir'.
Justificação matemática: 'excluir' ∉ {'ler'}

=================================================================
Escolha uma opção: 2
Deseja saber quem pode realizar qual ação? ler

Utilizadores autorizados para 'ler': Ana, Giovanna, Roberto, Kaiki

=================================================================
Escolha uma opção: 3

--- ADICIONAR NOVO UTILIZADOR NO APP ---
Quem está a solicitar a adição do utilizador? Giovanna

[ACESSO NEGADO] Giovanna não tem permissão para gerir utilizadores.
Justificação: 'gerir_usuarios' ∉ {'editar', 'ler'}

=================================================================
Escolha uma opção: 4

--- EXCLUIR UTILIZADOR DO APP ---
Quem está a solicitar a exclusão? Kaiki

[ACESSO AUTORIZADO] Kaiki possui 'excluir' ∈ Permissões.
Digite o nome do utilizador a ser excluído: Ana
[SUCESSO] O utilizador 'Ana' foi removido do aplicativo.

=================================================================
Escolha uma opção: 5

Perfis base: leitor, editor, admin
Perfil A: admin
Perfil B: admin

admin ⊆ admin? True
Detalhe: admin = {'gerir_usuarios', 'editar', 'ler', 'excluir'} | admin = {'gerir_usuarios', 'editar', 'ler', 'excluir'}

=================================================================
Escolha uma opção: 6

------------------------------------------------------------
Utilizador      | Perfis               | Permissões (União)
------------------------------------------------------------
Giovanna        | editor               | {editar, ler}
Roberto         | admin                | {gerir_usuarios, editar, ler, excluir}
Kaiki           | admin                | {gerir_usuarios, editar, ler, excluir}
------------------------------------------------------------

=================================================================
Escolha uma opção: 5

Perfis base: leitor, editor, admin
Perfil A: leitor
Perfil B: admin

leitor ⊆ admin? True
Detalhe: leitor = {'ler'} | admin = {'gerir_usuarios', 'editar', 'ler', 'excluir'}

=================================================================
Escolha uma opção: 0
A encerrar o sistema do aplicativo...
```
