
from xlwt import Workbook
import xlwt
i = 1

wb = Workbook()
sheet = wb.add_sheet('Maths')

for year in range(2018, 2022):
    for paper in range(31, 34):
        sheet.write(i, 0, f"9709_s{str(year)[-2:]}_qp_{paper}")
        sheet.write(i, 1, f"https://papers.gceguide.com/A%20Levels/Mathematics%20(9709)/{year}/9709_s{str(year)[-2:]}_qp_{paper}.pdf")
        i += 1

    for paper in range(31, 34):
        sheet.write(i, 0, f"9709_w{str(year)[-2:]}_qp_{paper}")
        sheet.write(i, 1, f"https://papers.gceguide.com/A%20Levels/Mathematics%20(9709)/{year}/9709_w{str(year)[-2:]}_qp_{paper}.pdf")

        i += 1

print(i)

wb.save('xlwt example.xls')
