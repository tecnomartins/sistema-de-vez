import PySimpleGUI as sg
from gtts import gTTS
import os

def talk(mytext):
    myobj = gTTS(text=mytext, lang='pt', slow=False)
    myobj.save("welcome.mp3")
    os.system("cvlc welcome.mp3 --play-and-exit ")

sg.theme('dark amber')

layout1 = [[sg.Text('Senha', text_color='dark orange'), sg.Text(size=(1, 1), key='-OUTPUT1-', text_color='dark orange'),
            sg.Text('-  Balcão', text_color='dark orange'),
            sg.Text(size=(1, 1), key='-OUTPUT2-', text_color='dark orange')],
           [sg.Text('Senha Atual:', text_color='dark orange'),
            sg.Text(justification='center', key='text', text_color='dark orange')],
           [sg.Text('Escolha um Balcão:', text_color='dark orange')],
           [sg.Button('A', button_color='black on dark orange'), sg.Button('B', button_color='black on dark orange'),
            sg.Button('C', button_color='black on dark orange'), sg.Button('D', button_color='black on dark orange')],
           [sg.Button('Voltar', button_color='black on dark orange'),
            sg.Button('Sair', button_color='black on dark orange')]]

window1 = sg.Window('Escolher Caixa', layout1,
                    keep_on_top=True,
                    no_titlebar=True,
                    grab_anywhere=True,
                    font="Helvetica")

layout2 = [[sg.Text('Senha', justification='right', size=(8, 1), text_color='dark orange'),
            sg.Text(size=(2, 1), justification='center', key='-OUTPUT1-', text_color='dark orange'),
            sg.Text('-  Balcão', text_color='dark orange'),
            sg.Text(size=(2, 1), justification='center', key='-OUTPUT2-', text_color='dark orange')]]

window2 = sg.Window('Tela', layout2,
                    keep_on_top=True,
                    no_titlebar=True,
                    grab_anywhere=True,
                    size=(1280, 100),
                    location=(0, 924),

                    font=("Helvetica", 70))
senha = 0
while True:  # Event Loop
    event, values = window1.read(timeout=0)
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == 'A':
        window1['-OUTPUT1-'].update(senha)
        window1['-OUTPUT2-'].update('A')
        window2['-OUTPUT1-'].update(senha)
        window2['-OUTPUT2-'].update('A')
        text = "Senha " + str(senha) + " - .Balcão A"
        talk(str(text))
        senha = senha + 1
        window1['text'].update(senha)
    if event == 'B':
        window1['-OUTPUT1-'].update(senha)
        window1['-OUTPUT2-'].update('B')
        window2['-OUTPUT1-'].update(senha)
        window2['-OUTPUT2-'].update('B')
        text = "Senha " + str(senha) + " - .Balcão B"
        talk(str(text))
        senha = senha + 1
        window1['text'].update(senha)
    if event == 'C':
        window1['-OUTPUT1-'].update(senha)
        window1['-OUTPUT2-'].update('C')
        window2['-OUTPUT1-'].update(senha)
        window2['-OUTPUT2-'].update('C')
        text = "Senha " + str(senha) + " - .Balcão C"
        talk(str(text))
        senha = senha + 1
        window1['text'].update(senha)
    if event == 'D':
        window1['-OUTPUT1-'].update(senha)
        window1['-OUTPUT2-'].update('D')
        window2['-OUTPUT1-'].update(senha)
        window2['-OUTPUT2-'].update('D')
        text = "Senha " + str(senha) + " - Balcão D"
        talk(str(text))
        senha = senha + 1
        window1['text'].update(senha)
    if event == 'Voltar':
        senha = senha - 1
        window1['text'].update(senha)

    event, values = window2.read(timeout=0)
    if event == sg.WIN_CLOSED:
        break
window1.close()
