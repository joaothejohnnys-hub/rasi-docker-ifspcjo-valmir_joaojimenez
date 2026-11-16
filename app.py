import os
from flask import Flask, render_template_string
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('DB_NAME', 'meu_banco'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', '')
    )

def init_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100),
                prontuario VARCHAR(20)
            )
        ''')
        cursor.execute("SELECT COUNT(*) FROM alunos")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO alunos (nome, prontuario) VALUES ('João Jimenez de Oliveira', 'CJ3028216')")
            cursor.execute("INSERT INTO alunos (nome, prontuario) VALUES ('Valmir Pereira', 'CJ3027678')")
            conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Erro ao inicializar o banco de dados: {e}")

BASE_TEMPLATE = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{{ title }} - RASI IFSP</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f6f9; margin: 0; padding: 0; }
        header { background: #1b4d3e; color: white; padding: 20px; text-align: center; }
        nav { background: #2c3e50; padding: 10px; text-align: center; }
        nav a { color: white; margin: 0 15px; text-decoration: none; font-weight: bold; }
        nav a:hover { text-decoration: underline; }
        .container { max-width: 800px; margin: 30px auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
        th { background-color: #1b4d3e; color: white; }
        footer { text-align: center; padding: 15px; color: #7f8c8d; font-size: 0.9em; margin-top: 30px; }
    </style>
</head>
<body>
    <header>
        <h1>IFSP - Campus Campos do Jordão</h1>
        <p>Redes e Administração de Sistemas (RASI)</p>
    </header>
    <nav>
        <a href="/">Início</a>
        <a href="/sobre">Sobre</a>
        <a href="/contato">Contato</a>
        <a href="/alunos">Alunos (MySQL)</a>
    </nav>
    <div class="container">
        {{ content | safe }}
    </div>
    <footer>
        <p>Trabalho Acadêmico - Docker Compose, Flask e Apache | Autores: João Jimenez e Valmir Pereira</p>
    </footer>
</body>
</html>
'''

@app.route('/')
def index():
    content = '''
        <h2>Bem-vindo ao Ambiente Docker Multi-container</h2>
        <p>Esta aplicação está rodando em um contêiner Python Flask (imagem <code>python:3.14-slim</code>), orquestrada via Docker Compose, integrada a um banco de dados MySQL 8.0 (com root sem senha) e exposta através de um proxy reverso Apache HTTPD 2.4.</p>
        <p>Utilize o menu superior para navegar pelas rotas institucionais e testar a persistência de dados.</p>
    '''
    return render_template_string(BASE_TEMPLATE, title="Início", content=content)

@app.route('/sobre')
def sobre():
    content = '''
        <h2>Sobre o Projeto</h2>
        <p>Projeto desenvolvido para atender aos critérios de avaliação da disciplina de RASI sob a orientação do Professor Cesar Augusto de Moraes Costa.</p>
        <p>A arquitetura substitui servidores monolíticos por uma infraestrutura em microsserviços isolados com rede bridge, volumes persistentes e validação de saúde automatizada (<em>healthcheck</em>).</p>
    '''
    return render_template_string(BASE_TEMPLATE, title="Sobre", content=content)

@app.route('/contato')
def contato():
    content = '''
        <h2>Canal de Atendimento e Suporte</h2>
        <p>Instituição: IFSP - Campus Campos do Jordão</p>
        <p>Curso: Técnico em Informática Integrado ao Ensino Médio</p>
        <p>Alunos Responsáveis: João Jimenez de Oliveira e Valmir Pereira</p>
    '''
    return render_template_string(BASE_TEMPLATE, title="Contato", content=content)

@app.route('/alunos')
def alunos():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, prontuario FROM alunos")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        
        table_html = '''
            <h2>Registros de Alunos (Integrados ao MySQL 8.0)</h2>
            <p>Dados recuperados dinamicamente da tabela persistida no banco de dados do contêiner MySQL:</p>
            <table>
                <tr><th>ID</th><th>Nome do Aluno</th><th>Prontuário</th></tr>
        '''
        for row in rows:
            table_html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"
        table_html += "</table>"
        content = table_html
    except Exception as e:
        content = f"<h2>Erro de Conexão com o Banco de Dados</h2><p>{e}</p>"
        
    return render_template_string(BASE_TEMPLATE, title="Alunos", content=content)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
