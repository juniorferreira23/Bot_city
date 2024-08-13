# Import for the Web Bot
from botcity.web import WebBot, Browser, By
import env

def main():
    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.FIREFOX

    # Uncomment to set the WebDriver path
    # bot.driver_path = "C:\WebDriver\chromedriver-win64\chromedriver.exe"
    bot.driver_path = r"/home/junior/Área de Trabalho/Bot_city/drivers/geckodriver"

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
    bot.kb_type(env.login)
    # Clicando botão continuar
    btn_continue = bot.find_element(selector='btn-continue', by=By.ID)
    btn_continue.click()
    
    # Digitando Senha
    campo_senha = bot.find_element(selector='current-password', by=By.ID)
    bot.wait_for_element_visibility(element=campo_senha, visible=True, waiting_time=env.time)
    campo_senha.click()
    bot.kb_type(env.senha)
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
    
    bot.wait(3000)
    
    # Selecionar campo de filtro numero de documento
    campo_filtro = bot.find_element(selector='/html/body/div[2]/div[7]/div[2]/div[3]/div[2]/div[2]/div/div[3]/table/thead/tr[2]/td[3]/span/input', by=By.XPATH)
    bot.wait_for_element_visibility(element=campo_filtro, visible=True, waiting_time=env.time)
    # Clicar no botão financeiro
    campo_filtro.click()
    
    dados = 91498471
    
    # Localizar todos os checkbox
    checkboxs = bot.find_element(selector='oGridCheckbox', by=By.CLASS_NAME)
    bot.wait_for_element_visibility(element=checkboxs, visible=True, waiting_time=env.time)
    # Clicar no botão financeiro
    checkbox = 1
    while checkbox <= len(checkboxs) - 1:
        ...
        
    
    # Wait 3 seconds before closing
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    # bot.stop_browser()

if __name__ == '__main__':
    main()
