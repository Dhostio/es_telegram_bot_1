import PySimpleGUI as sg
import telegram

sg.theme("LightGray1")

chat_id=""
token = ""
bot = telegram.Bot(token=token)
colonna = [[sg.Button('Invia',key="Invia", button_color=("black", "white"), font=("italics")), 
            sg.Button('Exit',key='Exit', button_color=("white","blue"), font=("italics")),
            sg.FileBrowse('immagine',target='immagine',file_types=(("JPEG",".JPG"),("PNG",".png")),key='immagine')]]

layout = [  [sg.Text('Invia il tuo messaggio:')],
            [sg.Input('immagine',key='immagine',enable_events=True,visible=False)] ,
            [sg.Multiline(size=(70, 5),no_scrollbar=True)],
            [sg.Column(colonna, expand_x=True, element_justification='center')]]

window = sg.Window('TelePonti', layout, default_element_size=(50, 2), location=(100, 100))

while True:
    event, value = window.read()
    if event == 'Invia':
        try:
            bot.send_message(chat_id=chat_id, text=value[0])
            sg.popup.quick_message("-messaggio inviato",grab_anywhere=True) 
        except Exception as ex:
            sg.popup('-Inserisci un messaggio!',location = (100, 100))
    if event=="immagine":
        try:
            bot.send_photo(chat_id, photo=open(value['immagine'], 'rb'))
        except Exception as ex:
            sg.popup('-Inserisci un immagine!', location = (100, 100))
    if event == sg.WIN_CLOSED or event =="Exit":
        break
    print("inviato", value[0])

window.close()