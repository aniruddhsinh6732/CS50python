import pyfiglet
import sys
import random

if len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        font = sys.argv[2]
    else:
        sys.exit()
elif len(sys.argv) == 1:
    fonts = pyfiglet.Figlet().getFonts()
    font = random.choice(fonts)
else:
    sys.exit()

figlet = pyfiglet.Figlet(font = font)
text = figlet.renderText(input("Input : "))

print(text)