import pyfiglet
import serial
from gtts import gTTS
import os


def readserial(comport, baudrate):
    ser = serial.Serial(comport, baudrate, timeout=1)  # 1/timeout is the frequency at which the port is read

    while True:
        data = ser.readline().decode().strip()
        if data:
            convdata = " " + str(data)[1:]
            result = pyfiglet.figlet_format(str(convdata), font="banner")
            file = open("print.txt", "w")
            file.write("   TECNOMARTINS.PT\n   CLIENTE NÚM.\n\n")
            file.write(result)
            file.close()
            #print(result)

            firstcharacter = str(data)[0]

            if firstcharacter == "a":
                language = "pt"
                mytext = "por favor aguardar a sua vez"
            elif firstcharacter == "b":
                language = "en"
                mytext = "please wait your turn"
            elif firstcharacter == "c":
                language = "fr"
                mytext = "s'il vous plait attendez votre tour"

            talk = gTTS(text=mytext, lang=language, slow=False)
            talk.save("wait.mp3")
            os.system("cvlc wait.mp3  --play-and-exit")

            cmd = "lpr -o media=RP76x2000 -P EPSON_TM-P2.01 /home/tecnomartins/Documents/print/print.txt"
            # qr = "lpr -o media=RP76x2000 -P EPSON_TM-P2.01 /home/tecnomartins/Documents/print/qrcode.png"
            os.system(cmd)
            # os.system(qr)


if __name__ == '__main__':
    readserial('/dev/ttyACM0', 9600)
