import openpyxl
from openpyxl import workbook, load_workbook
from openpyxl.styles import Alignment  # aligning
from openpyxl.styles import Font  # changing style
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
from openpyxl.styles.colors import Color
from openpyxl.styles import Font

excel_location = 'C:/Users/johnc/Desktop/Visit Notes QA/QA VISIT NOTES.xlsx'
wb = load_workbook(excel_location)
ws = wb.active
max_row = ws.max_row

def append_to_excel(list_to_add_in_new_row):
    ws.append(list_to_add_in_new_row)
    wb.save(excel_location)

# REQUIRES YOU TO HAVE CURRENT ROW BEFORE
def input_list_to_newline_excel(column, row, list_name):
    # counts the row to get the current row to put findings in right spot
    for row in ws.iter_rows(min_row=1, max_row=max_row):
        iterated_row = str(row[0].row)
        current_row = iterated_row

# for idg in idg_notes_list:
def apppend_list_of_dictionary_row(name_list,sheetname):  ## NEED TO ITERATE EACH DIC TO IT
    key_list = []
    value_list = []
    names = wb.get_sheet_names()  # this ones deprecated
    # names = wb.sheetnames()

    if sheetname not in names:
        wb.create_sheet(sheetname)
        wb.save(excel_location)

    ws = wb[sheetname]
    for dictionary in name_list:
        try:
            for key, value in dictionary.items():
                if value is not None:
                    if value != '':
                        key_list.append(key)
                        value_list.append(value)
        except:
            pass

    # I CAN ADD NOT TO ADD IT IF THE DATE OF QA IS DONE ALREADY OR SOMETHING LIKE THAT>

    ws.append(key_list)
    ws.append(value_list)
    wb.save(excel_location)
    # print("Added Assessment to Excel")

def apppend_list_to_sheetname(list_name,sheetname):
    names = wb.get_sheet_names()  # this ones deprecated
    # names = wb.sheetnames()

    if sheetname not in names:
        wb.create_sheet(sheetname)
        wb.save(excel_location)

    ws = wb[sheetname]
    # I CAN ADD NOT TO ADD IT IF THE DATE OF QA IS DONE ALREADY OR SOMETHING LIKE THAT>

    ws.append(list_name)
    wb.save(excel_location)
    print("Added visit findings to Excel")



