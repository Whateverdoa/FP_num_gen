from collections import namedtuple
import pprint
import PySimpleGUI as sg
import os
import pandas as pd


def main():
    sg.change_look_and_feel('Dark')

    layout = [
        # [sg.Text("VDP"), sg.Checkbox('nummers', default=True), sg.Checkbox('beelden')],

        [sg.Text('Nummer generator 2.0', text_color="Yellow")],
        [sg.Text('Ordernummer', size=(15, 1)), sg.InputText(key="order_number")],
        [sg.Text("Aantal VDP's", size=(15, 1)), sg.InputText(key="aantal_vdps")],

        [sg.Text()],
        [sg.CalendarButton("Datum")],
        [sg.Text()],

        [sg.Text('Totaal aantal', size=(15, 1)), sg.Input(key="totaal_aantal")],
        [sg.Text('Beginnummer', size=(15, 1)), sg.InputText(key="begin_nummer")],
        [sg.Text('posities', size=(15, 1)), sg.InputText(key="posities")],
        [sg.Text('voorloop getal', size=(15, 1)), sg.InputText(key="vlg0")],
        [sg.Text('Aantal_per_rol', size=(15, 1)), sg.InputText(key='aantal_per_rol')],
        [sg.Text('Mes', size=(15, 1)), sg.InputText(key='mes')],

        [sg.Text('Y_waarde', size=(15, 1)), sg.InputText(key="Y_waarde")],
        [sg.Text('Wikkel', size=(15, 1)), sg.InputText(key="wikkel")],
        [sg.Text('prefix', size=(15, 1)), sg.InputText(key="prefix")],
        [sg.Text('postfix', size=(15, 1)), sg.InputText(key="postfix")],
        [sg.Text('hoogte etiket', size=(15, 1)), sg.InputText(key="hoogte")],
        [sg.Text('opmerkingen', size=(15, 1)), sg.InputText(key="opmerkingen")],


        [sg.Button("Ok"), sg.Cancel()],

        [sg.Text('_' * 80)],
        [sg.Text('SAVE of LOAD inputform', size=(35, 1))],
        # [sg.Text('Your Folder', size=(15, 1), justification='right'),
        #  sg.InputText('Default Folder', key='folder'), sg.FolderBrowse()],
        [sg.Button('Exit'),
         sg.Text(' ' * 40), sg.Button('SaveSettings'), sg.Button('LoadSettings')]
    ]

    window = sg.Window('Nummer_Generator 2020').Layout(layout)

    while True:
        event, values = window.Read()

        if event in ("Exit", None):
            break

        elif event == 'SaveSettings':
            filename = sg.popup_get_file('Save Settings', save_as=True, no_window=True)
            # False in mac OS otherwise it will crash
            window.SaveToDisk(filename)

            # save(values)
        elif event == 'LoadSettings':
            filename = sg.popup_get_file('Load Settings', no_window=True)
            # False in mac OS otherwise it will crash
            window.LoadFromDisk(filename)
            # load(form)

        elif event == "Ok":

            print("ok")

            # print(button, values["order_number"], values["begin_nummer"], values["posities"])
            # datum = values["Datum"]
            ordernummer = values["order_number"]
            totaal_aantal = int(values["totaal_aantal"])
            begin_nummer = int(values["begin_nummer"])
            posities = int(values["posities"])
            vlg = int(values["vlg0"])
            aantal_per_rol = int(values["aantal_per_rol"])
            y_waarde = int(values["Y_waarde"])
            wikkel = int(values["wikkel"])
            hoogte = int(values["hoogte"])
            prefix = values["prefix"]
            postfix = values["postfix"]
            mes = int(values["mes"])

            inloop = y_waarde * 10 - y_waarde

            input_var_lijst = ["ordernummer",
                               "totaal_aantal",
                               "begin_nummer",
                               "posities",
                               "voorloopgetal",
                               "aantal_per_rol",
                               "y_waarde",
                               "prefix",
                               "postfix"]


            input_data_1 = namedtuple("input_data", input_var_lijst, defaults=[1])
            input_data_1._field_defaults

            test_data = input_data_1(ordernummer,
                                     totaal_aantal,
                                     begin_nummer,
                                     posities,
                                     vlg,
                                     aantal_per_rol,
                                     y_waarde,
                                     prefix,
                                     postfix)

            input_key_list =[]
            print(test_data.ordernummer)
            print((x for x in test_data))
            def lalalala():
                print("lalalala")

if __name__ == '__main__':

    main()



