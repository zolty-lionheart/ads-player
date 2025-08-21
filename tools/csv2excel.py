'''
Author: zolty zolty@qq.com
Date: 2025-04-22 14:55:19
LastEditors: zolty zolty@qq.com
LastEditTime: 2025-04-22 14:59:27
FilePath: /ads-player/tools/csv2excel.py
Description: 遍历 csv 文件夹中的所有 CSV 文件并转换为 Excel 文件
'''
import os
import csv
from openpyxl import Workbook

def csv_to_excel(csv_file, excel_file):
    """将单个 CSV 文件转换为 Excel 文件"""
    workbook = Workbook()
    sheet = workbook.active

    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            sheet.append(row)

    workbook.save(excel_file)
    print(f"转换完成: {excel_file}")

def convert_all_csv_in_folder(folder_path):
    """遍历文件夹中的所有 CSV 文件并转换为 Excel 文件"""
    if not os.path.exists(folder_path):
        print(f"文件夹不存在: {folder_path}")
        return

    # 遍历文件夹中的所有文件
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv'):
                csv_file = os.path.join(root, file)
                excel_file = os.path.splitext(csv_file)[0] + ".xlsx"
                try:
                    csv_to_excel(csv_file, excel_file)
                except Exception as e:
                    print(f"转换失败: {csv_file}, 错误: {e}")

if __name__ == "__main__":
    # 默认文件夹名为 csv
    folder_path = os.path.join(os.getcwd(), "../csv")
    convert_all_csv_in_folder(folder_path)