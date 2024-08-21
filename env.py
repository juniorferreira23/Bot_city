url = 'https://app.omie.com.br/login/'
time = 10000

drivers = {
    'linux': {
        # bot.driver_path = r"/home/junior/Área de Trabalho/Bot_city/drivers/firefoxdriver/geckodriver"
        'firefox': './drivers/firefoxdriver/geckodriver'
    },
    
    'windows' : {
        #bot.driver_path = "C:\chromedriver-win64\chromedriver.exe"
        'chrome': r'.\\drivers\\windows\\chromedriver-win64\\chromedriver.exe',
        'firefox': r'.\\drivers\\windows\\geckodriver-v0.35.0-win64\\geckodriver.exe'
    }
}

PATH_FILE_LOG = f'./log'