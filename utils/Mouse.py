from botcity.web import WebBot, Browser, By

bot = WebBot()

x = bot.get_last_x()
y = bot.get_last_y()
print(f'A última posição salva do mouse é: {x}, {y}')