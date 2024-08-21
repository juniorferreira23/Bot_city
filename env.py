url = 'https://app.omie.com.br/login/'
time = 10000

drivers = {
    'linux': {
        'firefox': './drivers/firefoxdriver/geckodriver'
    },
    
    'windows' : {
        'chrome': r'.\\drivers\\windows\\chromedriver-win64\\chromedriver.exe',
        'firefox': r'.\\drivers\\windows\\geckodriver-v0.35.0-win64\\geckodriver.exe'
    }
}

PATH_FILE_LOG = './log'