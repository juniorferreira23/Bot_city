# Import for the Web Bot
from botcity.web import WebBot, Browser, By
import env
import keys
from datetime import datetime

def main(extrato: list[object]):

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
        
    
    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.FIREFOX

    # Uncomment to set the WebDriver path
    bot.driver_path = env.drivers['windows']['firefox']

    # Opens the BotCity website.
    bot.start_browser()
    bot.maximize_window()
    bot.browse(env.url)

    # Implement here your logic...
    # Selecionando login
    campo_email = bot.find_element(selector='email', by=By.ID)
    bot.wait_for_element_visibility(element=campo_email, visible=True, waiting_time=env.time)
    campo_email.click()
    # Digitando login
    bot.kb_type(keys.login)
    # Clicando botão continuar
    btn_continue = bot.find_element(selector='btn-continue', by=By.ID)
    btn_continue.click()
    
    # Digitando Senha
    campo_senha = bot.find_element(selector='current-password', by=By.ID)
    bot.wait_for_element_visibility(element=campo_senha, visible=True, waiting_time=env.time)
    campo_senha.click()
    bot.kb_type(keys.senha)
    # Clicando botão entrar
    btn_entrar = bot.find_element(selector='btn-login', by=By.ID)
    btn_entrar.click()
    
    # Selecionando botão acessar
    btn_acessar = bot.find_element(selector='/html/body/div[1]/main/div/div[1]/div[2]/div/div[1]/div/div[2]/div[2]/div/div/button', by=By.XPATH)
    bot.wait_for_element_visibility(element=btn_acessar, visible=True, waiting_time=env.time)
    # Clicando no botão
    btn_acessar.click()
    
    # Obtendo a lista de manipuladores de guias.
    abas_abertas = bot.get_tabs()
    # Obtendo o identificador de uma nova guia aberta.
    nova_aba = abas_abertas[1]
    # Ativando a guia como o contexto atual.
    bot.activate_tab(nova_aba)
    
    bot.wait(5000)
    
    # Selecionar botão fechar alert
    btn_fechar_alert = bot.find_element(selector='onesignal-slidedown-cancel-button', by=By.ID)
    bot.wait_for_element_visibility(element=btn_fechar_alert, visible=True, waiting_time=env.time)
    # Clicar no botão fechar alert
    btn_fechar_alert.click()
    
    # Selecionar categoria financeira
    ctg_financeiro = bot.find_element(selector='/html/body/div[2]/div[5]/div[2]/ul/li[5]/a',by=By.XPATH)
    bot.wait_for_element_visibility(element=ctg_financeiro, visible=True, waiting_time=env.time)
    # Clicar no botão financeiro
    ctg_financeiro.click()
    
    bot.wait(10000)
    
    # Selecionar aba financeira
    aba_financeira = bot.find_element(selector='/html/body/div[2]/header/div[3]/div/ul/li[5]/a', by=By.XPATH)
    bot.wait_for_element_visibility(element=aba_financeira, visible=True, waiting_time=env.time)
    # Clicar no botão financeiro
    aba_financeira.click()
    
    bot.wait(3000)
    
    # Selecionar exibir todas contas a pagar
    btn_exibir = bot.find_element(selector='/html/body/div[2]/div[1]/div[5]/form/div/div[2]/div/div[2]/div[3]/ul/li[3]/a', by=By.XPATH)
    bot.wait_for_element_visibility(element=btn_exibir, visible=True, waiting_time=env.time)
    # Clicar no botão financeiro
    btn_exibir.click()
    
    bot.wait(10000)
    
    # # Loop main dos documentos
    for documento in extrato:
        # Log de iniciação da execução
        log(f'INFO: Iniciando execução do documento - {documento}')
        
        # Filtrar pelo contrato
        # Selecionar campo de filtro numero de documento
        campo_filtro = bot.find_element(selector='/html/body/div[2]/div[7]/div[2]/div[3]/div[2]/div[2]/div/div[3]/table/thead/tr[2]/td[3]/span/input', by=By.XPATH)
        bot.wait_for_element_visibility(element=campo_filtro, visible=True, waiting_time=env.time)
        # Clicar no botão financeiro
        campo_filtro.click()
        # Digitar contrato
        bot.control_a()
        bot.kb_type(documento['contrato'])
        bot.enter()
    
        bot.wait(10000)
        
        # Encontrado linhas de parcela da tabela
        elementos = bot.find_elements(selector='/html/body/div[2]/div[7]/div[2]/div[3]/div[2]/div[2]/div/div[5]/table/tbody/tr/td[4]', by=By.XPATH)
        # Tratando se não achar os elementos
        if not elementos:
            log(f'ERRO: Linhas da tabela não encontradas')
            continue
        
        for elemento in elementos:
            log(f'INFO: Iniciando verificação na linha - {elemento.text}')
            
            # Formatando a parcela
            parcela = elemento.text[0] + elemento.text[1] + elemento.text[2]
            if parcela[0] == '0':
                parcela = parcela[1] + parcela[2]

            log(f'INFO: Iniciando comparação entre parcela omie {parcela} e parcela extrato {documento["parcela"]}')
            
            # Tratando diferença das parcelas
            if parcela != documento['parcela']:
                log(f'INFO: Parcela extrato {documento["parcela"]} difente da parcela Omie {parcela}')
                continue
                
            elemento.click()
            bot.enter()
            
            bot.wait(5000)
            
            # Selecionar aba Diversos
            aba_diversos = bot.find_element(selector='/html/body/div[2]/div[7]/div[2]/div[3]/div[3]/div/nav/div[2]/ul/li[6]/a', by=By.XPATH)
            bot.wait_for_element_visibility(element=aba_diversos, visible=True, waiting_time=env.time)
            # Clicar no botão financeiro
            aba_diversos.click()

            bot.wait(5000)
            
            # Selecionar Campo de parcelas
            campo_parcela = bot.find_element(selector='//*[@id="d51533c165"]', by=By.XPATH)
            bot.wait_for_element_visibility(element=campo_parcela, visible=True, waiting_time=env.time)
            # Clicar no campo de parcelas
            campo_parcela.click()
            
            # Selecionar botão de voltar
            botao_voltar = bot.find_element(selector='/html/body/div[2]/div[7]/div[1]/button/i', by=By.XPATH)
            bot.wait_for_element_visibility(element=botao_voltar, visible=True, waiting_time=env.time)
            # Clicar no botão de voltar
            botao_voltar.click()
            
            bot.wait(5000)
            
    
    # Wait 3 seconds before closing
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    log(f'INFO: Fim da execução (Execução concluída com sucesso)')
    # bot.stop_browser()

if __name__ == '__main__':
    main()
