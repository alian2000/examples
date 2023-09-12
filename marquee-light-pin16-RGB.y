from microbit import *
import neopixel
display.show(Image.HAPPY)
# The water lamp is connected to pin pin16, the number is 3
# to mix RGB colors.use https://www.csfieldguide.org.nz/en/interactives/rgb-mixer/
np = neopixel.NeoPixel(pin16, 3)
while True:
    np[0] = (0,255,255)
    np.show()
    sleep(1000)
    np[0] = (0,0,0)
    np.show()
    np[1] = (255,0,2)
    np.show()
    sleep(1000)
    np[1] = (0,0,0)
    np.show()
    np[1] = (0,0,0)
    np[2] = (1,255,1)
    np.show()
    sleep(1000)
    np[2] = (0,0,0)
    np.show()
