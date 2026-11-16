# Projeto 4º Bimestre RASI - Infraestrutura Multi-container com Docker Compose

Repositório acadêmico desenvolvido para a disciplina de **Redes e Administração de Sistemas (RASI)** do Instituto Federal de Educação, Ciência e Tecnologia de São Paulo (IFSP) – *Campus Campos do Jordão*, sob a orientação do Professor Cesar Augusto de Moraes Costa.

## Autores
* **João Jimenez de Oliveira** (Prontuário: CJ3028216)
* **Valmir Pereira** (Prontuário: CJ3027678)

---

## Sobre o Projeto
Este projeto consiste na evolução de um ambiente computacional tradicional para uma arquitetura moderna baseada em microsserviços containerizados. O sistema utiliza o **Docker Compose** para orquestrar três serviços interligados de forma isolada, reprodutível e segura:
1. **Servidor Web (Proxy Reverso):** Apache HTTPD 2.4 respondendo na porta `80`.
2. **Aplicação Web:** Python Flask (utilizando a imagem base `python:3.14-slim`) expondo as rotas institucionais e dinâmicas.
3. **Banco de Dados Relacional:** MySQL 8.0 com acesso root sem senha, persistência de dados em volume e verificação automática de integridade (*healthcheck*).

---

## Tecnologias Utilizadas
* **Virtualização e Sistema Operacional:** Ubuntu Server (via VirtualBox em modo Bridge e acesso remoto via SSH).
* **Containerização:** Docker e Docker Compose.
* **Linguagens e Frameworks:** Python 3.14 (Flask 3.1.2) e HTML/CSS.
* **Banco de Dados:** MySQL 8.0 (`mysql-connector-python`).
* **Servidor HTTP:** Apache HTTPD 2.4.

---

## Como Executar o Projeto

### Pré-requisitos
* Máquina Virtual com Ubuntu Server configurada.
* Docker e Docker Compose instalados.

### Passo a Passo

1. **Clone o repositório na sua máquina virtual:**
   ```bash
   git clone [https://github.com/joaothejohnnys-hub/rasi-docker-ifspcjo-valmir_joaojimenez.git](https://github.com/joaothejohnnys-hub/rasi-docker-ifspcjo-valmir_joaojimenez.git)
   cd rasi-docker-ifspcjo-valmir_joaojimenez
