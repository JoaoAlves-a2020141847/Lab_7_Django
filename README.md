# Aplicação Django - Guia de Utilização

Bem-vindo ao repositório desta aplicação Django! Este documento explica como configurar, executar e utilizar a aplicação.

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de que possui o seguinte:

- Computador Linux ou Windows
- Python 3.8 ou superior
- pip (gestor de pacotes do Python)
- Django 5.1.3

---

## 🚀 Instruções de Configuração

Siga os passos abaixo para configurar a aplicação:

### 1. Clone o Repositório
Faça o clone deste repositório para o seu ambiente local:
```bash
git clone https://github.com/JoaoAlves-a2020141847/Lab_7_Django.git
cd Lab_7_Django
```

### 2. Crie e Ative um Ambiente Virtual

Para isolar as dependências, crie e ative um ambiente virtual:

```python -m venv venv```

- Ativação no Linux

```source venv/bin/activate```
ou
```source ./venv/bin/activate```

- Ativação no Windows

```venv\Scripts\activate```


### 3. Instale as Dependências

Instale os pacotes necessários listados no ficheiro requirements.txt:

```pip install -r requirements.txt```


### 4. Configure a Base de Dados

A aplicação utiliza o SQLite como base de dados padrão. Para configurá-la, execute:

```python manage.py migrate```


### 5. Crie um Superutilizador (superuser)

Para aceder ao painel de administração, crie um superutilizador:

```python manage.py createsuperuser```


### 6. Inicie o Servidor de Desenvolvimento

Para visualizar a aplicação no navegador, execute:

```python manage.py runserver```

Depois, aceda ao endereço http://127.0.0.1:8000/ no seu navegador.
