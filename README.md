# 📧 Microsserviço Notifications - Ateliê Digital

## 📖 Sobre o Projeto

O **Ateliê Digital** é um sistema web que funciona como um marketplace exclusivo para produtos artesanais. O objetivo da plataforma é conectar diretamente os artesãos independentes aos consumidores, oferecendo ferramentas para que os vendedores gerenciem seus negócios e os clientes encontrem produtos com facilidade e segurança.

Neste repositório encontra-se o microsserviço de **Notifications (Notificações)**. Sua principal responsabilidade é realizar o envio assíncrono de e-mails a partir de eventos publicados pelos demais microsserviços da plataforma.

Ao desacoplar o envio de e-mails da lógica de negócio, a arquitetura torna-se mais escalável, resiliente e performática, permitindo que operações como cadastro de usuários, criação de pedidos e recuperação de senha não fiquem bloqueadas aguardando o envio das notificações.

---

# 🚀 Tecnologias e Recursos

Este microsserviço foi construído utilizando as seguintes tecnologias:

* **FastStream:** Framework utilizado para consumo assíncrono de mensagens do broker.
* **RabbitMQ:** Broker responsável pela comunicação entre os microsserviços.
* **SMTP:** Utilizado para o envio de e-mails aos usuários.
* **Docker:** Containerização da aplicação.
* **Docker Compose:** Orquestração do ambiente de desenvolvimento.
* **UV:** Gerenciador de dependências e ambientes virtuais desenvolvido pela Astral.

---

# 🏗️ Arquitetura

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

# ⚙️ Configuração do Ambiente

Para executar este projeto localmente, utilizamos o **UV** como gerenciador de dependências.

## 1. Instalação do UV

Caso ainda não possua o UV instalado, execute:

### Linux / macOS

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows (PowerShell)

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## 2. Criando o ambiente virtual

Na raiz do projeto:

```bash
uv venv
```

Ative o ambiente virtual.

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

---

## 3. Instalando as dependências

Caso exista um arquivo `uv.lock`, basta executar:

```bash
uv sync
```

Sempre que novas dependências forem adicionadas ao projeto, execute novamente:

```bash
uv sync
```

---

# 🐳 Executando com Docker

Construir a imagem:

```bash
docker compose build
```

Iniciar o serviço:

```bash
docker compose up
```

Ou executar em segundo plano:

```bash
docker compose up -d
```

---

# ▶️ Executando Localmente

Para iniciar o worker do FastStream:

```bash
faststream run infra.messaging.broker:app
```

---

# 📨 Fluxo de Funcionamento

O Notification Service possui um fluxo simples e desacoplado:

1. Um microsserviço publica um evento no RabbitMQ.
2. O Notification Service consome a mensagem utilizando o FastStream.
3. O payload recebido é processado.
4. O serviço monta a mensagem de e-mail.
5. O e-mail é enviado utilizando o servidor SMTP.
6. O processamento da mensagem é concluído.

Toda a regra de negócio permanece nos microsserviços produtores dos eventos, mantendo o Notification Service desacoplado e focado exclusivamente na entrega das notificações.

