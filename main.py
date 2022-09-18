import PySimpleGUI as sg
import time
import request

layout = [
        [sg.Text('Time (Sec)')],
        [sg.Slider(range=(10,90),default_value=10,size=(20,15),orientation='horizontal',
         enable_events=True,key='slide',font=('Helvetica', 12))],

        [sg.Text('URL')],
        [sg.Input(key='url')],

        [sg.Text('Auth Code')],
        [sg.Input(key='auth')],

        [sg.Text('Message')],
        [sg.Input(key='msg')],

        [sg.Button('Ok')],

        [sg.Output(size=(50,10))]
        ]


window = sg.Window('Farm BOT', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        window.close()
        break
    if event == 'Ok':
        break


end_time = time.time() + values['slide']
countTimer = 0
sleepTime = 0.500

while True:
    window.Refresh()
    time.sleep(sleepTime)
    countTimer += sleepTime
    if time.time() > end_time:
        print(request.send_and_del_msg(values['msg'], values['auth'], values['url']))
        countTimer = 0
        end_time = time.time() + values['slide']
