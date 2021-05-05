import blumenauimoveis
import acrc
import xlsxwriter
import datetime
from termcolor import colored
import time


def run():
    apartamentos = []
    apartamentos = blumenauimoveis.scrap(apartamentos)
    time.sleep(1)
    apartamentos = acrc.scrap(apartamentos)
    time.sleep(1)

    workbook = xlsxwriter.Workbook(f'Apartamentos{datetime.datetime.now().strftime("_%d-%m-%Y")}.xlsx')
    worksheet = workbook.add_worksheet(name='Apartamentos')
    bold = workbook.add_format({'bold': True})
    money = workbook.add_format({'num_format': '$#,##0'})
    row = 0
    col = 0

    for key in apartamentos[0].keys():
        worksheet.write(row, col, str(key).upper(), bold)
        col += 1

    row = 1
    col = 0

    for ap in apartamentos:
        worksheet.write(row, col, ap['link'])
        worksheet.write(row, col+1, ap['titulo'])
        worksheet.write(row, col+2, ap['valor'], money)
        worksheet.write(row, col+3, ap['descricao'])
        worksheet.write(row, col+4, ap['cod'])
        row += 1

    print(colored("Criado com sucesso. "+ workbook.filename, "green"))
    workbook.close()

if __name__ == "__main__":
    try:
        run()
    except Exception as erro:
        print(erro)