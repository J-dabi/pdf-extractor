from openpyxl import Workbook

def generate_excel(info_dict, output_path):
    wb = Workbook()
    ws = wb.active
    ws.title = "추출 정보"

    ws.append(["항목", "내용"])
    for key, value in info_dict.items():
        ws.append([key, value])

    wb.save(output_path)