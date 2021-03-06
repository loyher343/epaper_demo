import sys
# sys.path.insert(1, "./lib") # Adds lib folder in this directory to sys
import requests
import json
import numpy

from lib import epd2in9b_V2

from PIL import Image, ImageDraw, ImageFont


epd = epd2in9b_V2.EPD() #get the display
epd.init()              #initialize the display
print("Clear...")       #prints to console, not the display, for debuggin
epd.Clear()         #clear the display

def printToDisplay(string):
    HBlackImage = Image.new('1', (epd2in9b_V2.EPD_HEIGHT, epd2in9b_V2.EPD_WIDTH), 225)
    HRedImage = Image.new('1', (epd2in9b_V2.EPD_HEIGHT, epd2in9b_V2.EPD_WIDTH,), 225)

    draw = ImageDraw.Draw(HBlackImage) #Create draw object and pass in the image layer we want to work with HBlackImage
    font = ImageFont.truetype('/usr/share/fonts/Hack-Regular.ttf', 15) #Create our font, passing in the font file and font size
    #draw.text((0, 0), string, font = font, fill = 0)
    draw.multiline_text((0, 0), string, font = font, fill = 0, spacing= 4, align="center")
    epd.display(epd.getbuffer(HBlackImage), epd.getbuffer(HRedImage))
def getCryptoData():
    response = requests.get('http://api.coincap.io/v2/assets?ids=ethereum')
    resData = json.loads(response.text)
    data = resData['data'][0]
    name = data['name']
    #price = float(round(data['priceUsd'], 2))
    #    print(isinstance(price, int))
    cryptoData = name + ': '+ data['priceUsd']
    return cryptoData

def handleBtnPress():
    # message = input()
    printToDisplay("Tis better to Vile \n than Vile esteem")
    #printToDisplay(getCryptoData())

handleBtnPress()
