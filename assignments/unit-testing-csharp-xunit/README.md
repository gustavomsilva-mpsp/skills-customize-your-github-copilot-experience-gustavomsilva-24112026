# 📘 Assignment: Unit Testing in C# with xUnit

## 🎯 Objective

Crie testes unitários em C# com xUnit para verificar o comportamento de uma classe e seus casos-limite. Você praticará a estrutura Arrange-Act-Assert e aprenderá a executar testes automatizados com o .NET CLI.

## 📝 Tasks

### 🛠️ Set Up an xUnit Test Project

#### Descrição
Configure uma solução .NET com uma biblioteca de classes e um projeto de testes xUnit que referencie a biblioteca.

#### Requisitos
O programa concluído deve:

- Criar uma solução .NET, um projeto de biblioteca de classes e um projeto de testes xUnit.
- Adicionar ambos os projetos à solução e referenciar a biblioteca a partir do projeto de testes.
- Executar `dotnet test` e confirmar que o teste de exemplo criado pelo template passa.

### 🛠️ Implement the InventoryItem Class

#### Descrição
Implemente uma classe simples para representar um item de inventário e determinar se há estoque suficiente para atender a um pedido.

#### Requisitos
O programa concluído deve:

- Definir uma classe `InventoryItem` com propriedades para nome e quantidade em estoque.
- Implementar `CanFulfillOrder(int quantity)`, retornando `true` apenas quando a quantidade pedida for maior que zero e não ultrapassar o estoque.
- Manter a lógica da classe na biblioteca de classes, separada do projeto de testes.

### 🛠️ Test Inventory Behavior with xUnit

#### Descrição
Escreva testes automatizados para confirmar que `CanFulfillOrder` aceita pedidos válidos e rejeita pedidos que não podem ser atendidos.

#### Requisitos
O programa concluído deve:

- Usar testes xUnit com a estrutura Arrange-Act-Assert.
- Verificar um pedido válido e um pedido maior que o estoque.
- Verificar que quantidades iguais a zero e negativas são rejeitadas.
- Executar `dotnet test` e confirmar que todos os testes passam.