import sys
# sys.path.insert(1, "./lib") # Adds lib folder in this directory to sys

from lib import epd2in9b_V2

from PIL import Image, ImageDraw, ImageFont

epd = epd2in9b_V2.EPD() #get the display
epd.init()              #initialize the display
print("Clear...")       #prints to console, not the display, for debuggin
epd.Clear()         #clear the display

def printToDisplay(string):
    HBlackImage = Image.new('1', (epd2in9b_V2.EPD_HEIGHT, epd2in9b_V2.EPD_WIDTH), 225)
    HRedImage = Image.new('1', (epd2in9b_V2.EPD_HEIGHT, epd2in9b_V2.EPD_WIDTH,), 225)

    draw = ImageDraw(HBlackImage) #Create draw object and pass in the image layer we want to work with HBlackImage
    font = ImageFont.truetype('/usr/share/fonts/truetype/google/Bangers-Regular.ttf', 30) #Create our font, passing in the font file and font size
    draw.text((25, 65), string, font = font, fill = 0)
    epd.display(epd.getbuffer(HBlackImage), epd.getbuff(HRedImage))

def handleBtnPress():
    printToDisplay("Hello, World!!!!")

handleBtnPress()