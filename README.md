# 📧 Microsserviço Notifications - Ateliê Digital

## 📖 Sobre o Projeto

O **Ateliê Digital** é um sistema web que funciona como um marketplace exclusivo para produtos artesanais. O objetivo da plataforma é conectar diretamente os artesãos independentes aos consumidores, oferecendo ferramentas para que os vendedores gerenciem seus negócios e os clientes encontrem produtos com facilidade e segurança.

Neste repositório encontra-se o microsserviço de **Notifications (Notificações)**. Sua principal responsabilidade é realizar o envio assíncrono de e-mails a partir de eventos publicados pelos demais microsserviços da plataforma.

Ao desacoplar o envio de e-mails da lógica de negócio, a arquitetura torna-se mais escalável, resiliente e performática, permitindo que operações como cadastro de usuários, criação de pedidos e recuperação de senha não fiquem bloqueadas aguardando o envio das notificações.

---

## 🚀 Tecnologias e Recursos

Este microsserviço foi construído utilizando as seguintes tecnologias:

* **FastStream:** Framework utilizado para consumo assíncrono de mensagens do broker.
* **RabbitMQ:** Broker responsável pela comunicação entre os microsserviços.
* **SMTP:** Utilizado para o envio de e-mails aos usuários.
* **Docker:** Containerização da aplicação.
* **Docker Compose:** Orquestração do ambiente de desenvolvimento.
* **Ferramentas de Suporte:**
    * **uv:** Gerenciador de pacotes e ambientes virtuais ultrarrápido.

---

## 🏗️ Arquitetura

O Notification Service atua exclusivamente como consumidor de mensagens.

```text
                  Publica evento
+-------------------------------+
| Outros Microsserviços         |
| (Accounts, Orders, etc.)      |
+---------------+---------------+
                |
                v
          +-------------+
          | RabbitMQ    |
          +------+------+
                 |
                 | Consome mensagens
                 v
      +------------------------+
      | Notification Service   |
      +------------+-----------+
                   |
                   | Envia e-mails
                   v
             Servidor SMTP
```

---

## ⚙️ Configuração do Ambiente

Para executar este projeto localmente, utilizamos o **UV** como gerenciador de dependências.

### 1. Instalação do UV

Caso ainda não possua o UV instalado, execute:

**No Linux (ou macOS):**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**No Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

### 2. Criando o ambiente virtual

Na pasta raiz do projeto, crie um ambiente virtual limpo executando:
```bash
uv venv
```

Após a criação, **ative o ambiente virtual**:
* **Linux / macOS:**
    ```bash
    source .venv/bin/activate
    ```
* **Windows:**
    ```cmd
    .venv\Scripts\activate
    ```

### 3. Instalando as dependências

Caso exista um arquivo `uv.lock`, basta executar:

```bash
uv sync
```

Sempre que novas dependências forem adicionadas ao projeto, execute novamente:

```bash
uv sync
```

*Caso precise instalar as bibliotecas manualmente para testar o ambiente, o comando base seria:*
```bash
uv pip install fastapi uvicorn psycopg2-binary sqlalchemy python-jose[cryptography] pika pytest ruff taskipy faststream[cli, rabbit]
```

---

## ▶️ Como Executar a API

Você pode rodar o serviço em modo local de desenvolvimento diretamente via terminal ou de forma conteinerizada utilizando o Docker Compose para emular o ecossistema completo do Ateliê Digital.

### Opção 1: Execução Local

Para iniciar o servidor local de desenvolvimento, basta rodar:

```bash
faststream run infra.messaging.broker:app
```

### Opção 2: Execução via Docker Compose (Recomendado)
Para integrar o serviço de orders aos demais microsserviços do **Ateliê Digital** (como o RabbitMQ e o banco de dados PostgreSQL), a execução via Docker Compose garante que todos os containers compartilhem a mesma rede de comunicação interna.

1. **Crie a rede de comunicação global do projeto** (caso ainda não tenha sido criada no seu ambiente docker):
   ```bash
   docker network create atelie-network
   ```

2. **Inicie o serviço construindo a imagem do container**:
   Na raiz do repositório, execute o comando abaixo para realizar o build da imagem Docker e subir o serviço em background ou anexado ao terminal:
   ```bash
   docker compose up --build
   ```
