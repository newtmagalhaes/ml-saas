# ml-saas

Trabalho final do curso Introdução à Ciência de Dados

## Setup

### Docker

> [django/compose.yml](./django/compose.yml)

Basta utilizar o comando `docker compose -f django/compose.yml up` 

### Venv

Crie um ambiente virtual e ative-o.

```bash
# por exemplo
python3 -m venv .venv

# ative o ambiente no linux
source .venv/bin/activate

# ative o ambiente no windows
.venv/Scripts/Activate.ps1

# instale as dependências da aplicação
pip install -r django/requirements.txt
```

#### Notebook e modelos

> :warning: É recomendado ter um ambiente virtual separado para notebooks.

Crie um ambiente virtual semelhante às etapas acima, mas ao invés de usar o `requirements.txt`, utilize este comando:

```bash
pip install -U notebook seaborn pandas scikit-learn=1.6.1
```
