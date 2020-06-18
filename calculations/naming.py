"""a lot of things get names, a lot of things get called.
It might be useful if there was only one function to give away the names"""
import pandas as pd
import math

def csv_name_giver():

    def naming_a_csv(name, count, exp=".csv"):
        csv_name = f'{name}_{count}{exp}'
        return  csv_name
    return naming_a_csv



def standard_number():

    def number_vlg(x, vlg, positions, prefix='', postfix=''):
        num = f'{prefix}{x:>{vlg}{positions}}{postfix}'
        return num
    return number_vlg

nummer = standard_number()

def dataframe_from_csv():

    def df_from_csv_file_in(dataframe_name, csv_file):
        dataframe_name = pd.read_csv(csv_file, ";", dtype="str")
        return dataframe_name
    return  df_from_csv_file_in


def wikkel_handmatig():
    """"use input value"""
    def wikkel_(value_in):
        return value_in
    return wikkel


def wikkel():

    def calculate_wrapper(Aantalperrol, formaat_hoogte, kern=76):
        materiaal=145 # global var
        var_1 = int(math.sqrt((4/math.pi)*((Aantalperrol*formaat_hoogte)/1000)* materiaal+pow(kern,2)))
        wikkel = int(2*math.pi*(var_1/2)/formaat_hoogte+2)
        return wikkel

    return calculate_wrapper


def lists_in_list():
    def lists_in_list_divider(list_obj, items_in_list_mes):
        length_list = len(list_obj)
        list_divider = length_list // items_in_list_mes
        new_list = []

        start = 0
        end = items_in_list_mes
        for index in range(list_divider):
            new_list.append(list_obj[start:end])
            start += items_in_list_mes
            end += items_in_list_mes

        return new_list

    return lists_in_list_divider


# maak functie die lengte lijst checked (de rest functie) zodat er altijd
def lijst_checker_op_mes():
    def check_1(list_obj, items_in_list_mes):
        if len(list_obj) % items_in_list_mes != 0:
            print("todo")
            return False
        else:
            return True
    return check_1


def rest():
    def rest_rollen_uitrekenen(mes, totaal, aantal_per_rol):
        """het totaal delen door de aantal per rol  de restwaarde hievan geeft het aantal rollen dat te kort is"""
        if totaal <= mes * aantal_per_rol:

            # print(f'aantal rest rollen = {abs((mes * aantal_per_rol - totaal) // aantal_per_rol)} uit if')
            return abs((mes * aantal_per_rol - totaal) // aantal_per_rol)

        else:
            rest_rollen = totaal // aantal_per_rol % mes
            # print(f'aantal rest rollen = {rest_rollen} uit else')
            return rest_rollen
    return rest_rollen_uitrekenen

def dikt_rol_nummers():

    def rol_num_dikt(begin, vlg, positions, totaal, aantal_per_rol,prefix, postfix):
        """"maak twee lijsten nummers en rolnummers voeg samen tot dikt"""
        rollen_metbegin_nummers = {}

        beginnummers = [nummer(begin, vlg, positions, postfix, prefix) for begin in range(begin, begin + totaal, aantal_per_rol)]

        # beginnummers
        aantal_rollen = len(beginnummers)
        getallenvoorrol = len(str(aantal_rollen))

        # rolnummers
        rolnummers = [f'Rol {rolnummer:>{0}{getallenvoorrol}}' for rolnummer in range(1, aantal_rollen + 1)]
        rollen_metbegin_nummers = {rolnummers[i]: beginnummers[i] for i in range(aantal_rollen)}
        # rollen_metbegin_nummers
        return rollen_metbegin_nummers

    return rol_num_dikt

#todo  hoe wikkel implementeren

def roll():
    def df_csv_rol_builder_met_rolnummer(begin_nummer_uit_lijst, posities, vlg, aantal_per_rol, wikkel, prefix, postfix, rolnummer, qr_waarde="", pdf="leeg.pdf"):

        rol = [
            (nummer(getal,vlg,posities,prefix,postfix), "", pdf,"")
            for getal in range(
                begin_nummer_uit_lijst,
                (begin_nummer_uit_lijst + aantal_per_rol)
            )
        ]

        df_rol = pd.DataFrame(rol, columns=["num", "omschrijving", "pdf", "QR"])

        begin = df_rol.iat[0, 0]
        eind_positie_rol = (aantal_per_rol) - 1
        eind = df_rol.iat[eind_positie_rol, 0]

        twee_extra = pd.DataFrame(
            [(nummer(1,vlg,posities,prefix,postfix), "", "stans.pdf","") for x in range(2)],
            columns=["num", "omschrijving", "pdf", "QR"],
        )

        wikkel_df = pd.DataFrame(
            [(nummer(1,vlg,posities,prefix,postfix), "", "stans.pdf","") for x in range(wikkel)],
            columns=["num", "omschrijving", "pdf","QR"],
        )

        sluitstuk = pd.DataFrame(
            [[nummer(1,vlg,posities,prefix,postfix), f"{rolnummer} | {begin} t/m {eind} | {aantal_per_rol} etiketten", "stans.pdf",qr_waarde]],
            columns=["num", "omschrijving", "pdf","QR"],
        )

        naam = f"df_{begin_nummer_uit_lijst:>{vlg}{posities}}"
        # print(f'{naam} ____when its used to append the dataFrame in a list or dict<-----')
        naam = pd.concat([twee_extra, sluitstuk, wikkel_df, df_rol])

        return naam
    return df_csv_rol_builder_met_rolnummer