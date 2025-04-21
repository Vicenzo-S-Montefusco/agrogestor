# AgroGestor

Sistema de apoio à gestão do agronegócio utilizando Python e banco de dados Oracle.

## 📦 Tecnologias Utilizadas

- Python 3.x
- OracleDB
- SQLAlchemy
- Alembic

## 🚀 Como rodar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/Vicenzo-S-Montefusco/agrogestor.git
cd agrogestor
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
 

3. Instale as dependências

```bash
pip install -r requirements.txt` 
```

4. Adicione as credenciais para conexão com o banco
- Crie um arquivo .env na raiz do projeto e adicione suas credencias de conexão com a Oracle seguindo o exemplo do arquivo .env.example;
- As credenciais podem ser encontradas na aula "How to - Oracle SQL Developer - Comandos SQL"

5. Rode as migrations
- Rode o seguinte comando para aplicar as migrations do projeto e criar as tabelas do banco

```bash 
alembic upgrade head
```

- Caso seja necessária a criação de uma nova migration para a alteração ou criação de uma nova tabela, basta realizar as modificações no arquivo models.py, salvar e rodar os comandos

```bash 
alembic revision --autogenerate -m "descricao da migration"
alembic upgrade head
```

