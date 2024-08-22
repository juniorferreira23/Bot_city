from datetime import datetime
import env

def data_atual():
        return datetime.now().strftime("%d_%m_%Y")
    
def gravar_log(txt):
    path = env.PATH_FILE_LOG
    try:
        with open(f'{path}/{data_atual()}_log.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(txt + '\n')
            print(f'INFO: Log gravado com sucesso em {path}')
            arquivo.close()
    except Exception as err:
        print(f'Não foi possível gravar o arquivo {err}')

def hora_atual():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def log(txt):
    print(f'{hora_atual()} {txt}')
    gravar_log(f'{hora_atual()} {txt}')