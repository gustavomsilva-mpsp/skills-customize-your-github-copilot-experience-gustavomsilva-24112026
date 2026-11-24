# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar tarefas usando FastAPI, praticando rotas HTTP, validação de dados e respostas com códigos de status apropriados.

## 📝 Tarefas

### 🛠️ Criar a API Básica

#### Descrição
Configure uma aplicação FastAPI e implemente uma rota de verificação do funcionamento da API.

#### Requisitos
O programa concluído deve:

- Criar uma instância de `FastAPI` chamada `app`.
- Definir uma rota `GET /` que responda com um objeto JSON.
- Retornar uma mensagem que confirme que a API está funcionando.
- Executar a API localmente com `uvicorn main:app --reload`.

### 🛠️ Criar o Modelo de Dados

#### Descrição
Defina o formato dos dados de uma tarefa usando Pydantic e valide os campos recebidos pela API.

#### Requisitos
O programa concluído deve:

- Criar uma classe `Task` baseada em `BaseModel`.
- Incluir os campos `title` como texto e `completed` como booleano.
- Definir `completed` com o valor padrão `False`.
- Retornar uma resposta de erro automática quando os dados forem inválidos.

### 🛠️ Implementar Operações CRUD

#### Descrição
Implemente um recurso REST que permita criar, listar e excluir tarefas em uma lista armazenada na memória.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` para adicionar uma nova tarefa.
- Implementar `GET /tasks` para listar todas as tarefas.
- Implementar `GET /tasks/{task_id}` para buscar uma tarefa pelo identificador.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa.
- Retornar o código HTTP `404` com uma mensagem clara quando a tarefa não existir.
