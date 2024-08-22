# Resumo
Este sistema automatiza o processo de conferência de dados, comparando informações extraídas com os registros atualizados na plataforma Omie. Ao confirmar a correspondência entre os dados, o sistema registra automaticamente o recebimento das contas a receber na plataforma. A interface gráfica intuitiva permite ao usuário definir a data de recebimento e o local do arquivo de origem, otimizando a eficiência e a precisão do processo. 


# Instalação
1º - Clonando o repositório
```
git clone https://github.com/juniorferreira23/Recebidos_Omie.git

```

2º - Criando o ambiente virtual python venv
```
python -m venv venv
```

3º - Instalando as dependências
```
pip install -r requirements.txt
```

4º - Antes de iniciar a aplicação vá no arquivo bot.py e descomente 175 à 177 para que possa confirmar o recebimento

5º - Iniciando a aplicação
```
py app.py
```

# Desenvolvimento
Caso deseje fazer uso da aplicação, basta converter as informações de contrato e parcela para uma lista de objetos e passar como primeiro paramentro na chamada da função bot.main() no arquivo app.py na linha 83.

Formato do objeto:
dado = {
          'contrato': contrato,
          'parcela': parcela
        }


# Drivers

Windows:
    - chrome: Basta entrar no link do driver da documentação, na navegação clicar em chromeDriver, clicar no link "the Chrome for Testing availability dashboard" e escolher a versão stable compativel com seu chrome.
    
    - firefox: Ao entrar no link irá direcionar para o github, ao scrollar para baixo verá as opções de download do drive, se não encontrar a oções win64, clique em "Show all" para que abra o resto das opções, basta baixar e colocar o caminho.

Linux: 
    - firefox: Ao entrar no link irá direcionar para o github, ao scrollar para baixo verá as opções de download do drive, se não encontrar a oções linux64.tar ou é linux-aarch64.tar, clique em "Show all" para que abra o resto das opções, basta baixar e colocar o caminho.


# Criando o projeto do zero com o framework botcity
Documentação: https://documentation.botcity.dev/tutorials/python-automations/web/

1º - Instalar o pacote Cookiecutter para que possamos instalar o botcity e personaliza-lo na hora da instalação do framework
```
python -m pip install --upgrade cookiecutter

```

2º - Criar um novo projeto framework botcity
```
python -m cookiecutter https://github.com/botcity-dev/bot-python-template/archive/v2.zip
```

3º - Criar o ambiente virtual python venv
```
python -m venv venv
```

4º - Iniciar ambiente virtual 
windows:
```
./venv/Script/active
```
Linux:
```
source /venv/bin/active
```

5º - Instalar as dependências
```
pip install --upgrade -r requirements.txt
```

6º - Iniciando a aplicação
```
python bot.py
```