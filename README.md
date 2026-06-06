# 📦 FastDelivery Express - Sistema de Gestão de Entregas Urbanas

O **FastDelivery Express** é uma solução em linha de comando (CLI) desenvolvida em Python para otimizar e gerenciar o fluxo de entregas urbanas. O sistema foi projetado seguindo rigorosamente os padrões de arquitetura de software e os pilares da **Programação Orientada a Objetos (POO)**, garantindo modularidade, reutilização de código e facilidade de manutenção.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Versionamento:** Git & GitHub

---

## 📂 Estrutura de Pastas e Camadas

O projeto está organizado em pacotes isolados por responsabilidade, permitindo uma separação clara entre modelos de dados, regras de negócio e utilitários de sistema:

``
fast_delivery/
│
├── main.py              # Ponto de entrada do sistema (fluxo principal)
│
├── interfaces/          # Contratos e abstrações puras
│   └── calculo_frete_interface.py
│
├── modelos/             # Entidades do sistema (classes de dados)
│   ├── pessoa.py
│   ├── cliente.py
│   ├── entregador.py
│   ├── pedido.py
│   └── entrega.py
│
├── services/            # Camada de serviços (regras de negócio)
│   ├── cliente_service.py
│   ├── entrega_service.py
│   └── pedido_service.py
│
└── util/                # Componentes auxiliares e interface gráfica de texto
    ├── validador.py
    ├── menu.py
    └── formatador.py
``
🧩 Conceitos de POO Implementados:
🧬 1. Herança
A classe abstrata Pessoa foi criada como superclasse para agrupar atributos e comportamentos comuns (como nome e CPF). As classes Cliente e Entregador herdam diretamente de Pessoa, especializando o comportamento conforme a necessidade do negócio.

🔗 2. Interface e Abstração
Utilizando o módulo nativo abc (Abstract Base Classes), foi definida a CalculoFreteInterface. Ela impõe um contrato obrigatório através do método abstrato calcular_frete(), garantindo que qualquer nova modalidade de entrega implemente sua própria lógica de custos.

🔄 3. Polimorfismo
As classes EntregaComum, EntregaExpressa e EntregaPremium herdam a interface de cálculo de frete, mas reescrevem o método calcular_frete() de formas totalmente distintas:
Comum: distância x 1.5
Expressa: distância x 3.0
Premium: (distância x 5.0) + 20.0

🔒 4. Encapsulamento
Todos os atributos sensíveis das entidades utilizam modificadores de acesso privados (prefixados com __). O acesso e a modificação desses estados são feitos exclusivamente por meio de propriedades controladas usando os decoradores @property e @setter.

🚀 Como Executar o Projeto
1- Certifique-se de ter o Python 3 instalado em sua máquina.
2- Baixe ou clone este repositório.
3- Abra o terminal na pasta raiz do projeto (fast_delivery) e execute o comando:
``python main.py``

💻 Exemplos de Uso (Interface do Terminal)
Ao iniciar o sistema, você terá acesso ao menu interativo totalmente validado contra entradas incorretas:
``--- FastDelivery Express ---
1 - Cadastrar Cliente
2 - Listar Clientes
3 - Buscar Cliente
4 - Cadastrar Entregador
5 - Criar Pedido
6 - Listar Pedidos
7 - Atualizar Status do Pedido
0 - Sair
Escolha uma opção:``

Fluxo de Criação de Pedido:
O sistema valida se o cliente existe antes de aceitar um pedido e calcula o frete em tempo real baseado no tipo selecionado:
``CPF do cliente do pedido: 12345678900
Peso do pedido (kg): 2.5
Distância da entrega (km): 10
Tipos de Entrega: 1-Comum | 2-Expressa | 3-Premium
Escolha o tipo: 2
Pedido 1001 criado! Valor do Frete: R$ 30.00``
