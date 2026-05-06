# Random-quote
 - Criei este projeto para praticar a biblioteca Flask e requests.
 - Um site simples que recebe uma frase aleatoria da API Quote Generator ao pressionar o botão.
 - Acesse em: [link](https://random-quote-flask-yjhq.onrender.com)

## APIs

- **Quote Generator** - Receber Frase ([site](https://armanidrisi.github.io/quote-generator-api/)

# Pré-requisitos para rodar localmente
- Antes de começar, certifique-se de que cumpre os seguintes requisitos:
	- Python >= 3.9 (3.11+ recomendado)
	- Bibliotecas >= Vá para a area de instalação

## Instalação

- Veja como instalar:

```bash
# Clonar o repositório
git clone https://github.com/0xAA55-P/random-quote-flask

# Instalar dependências
pip install -r requirements.txt

# Executar o aplicativo
gunicorn --config gunicorn_config.py main:app

# Abra em 0.0.0.0:8080
```

# Licença

- Este software está sob a licença MIT. Para mais informações, veja LICENSE.md
