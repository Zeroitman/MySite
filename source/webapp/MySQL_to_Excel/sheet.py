import xlsxwriter
from webapp.models import  Child, Program, Session, Result, SkillsInProgram


def create_table(child_id):
    child = Child.objects.get(pk=child_id)
    program = Program.objects.get(child=child, status=True)
    sessions = Session.objects.get_queryset().filter(program=program)
    skills = SkillsInProgram.objects.get_queryset().filter(program=program)

    workbook = xlsxwriter.Workbook('chart_line.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': 1})

    headings = ['Дата', 'Номер сессии', 'С подсказкой', 'Без подсказки', 'Общее', 'Процент']
    position = 7

    for skill in skills:
        session_number = 1
        session_numbers = []
        session_date = []
        done = []
        done_with_hint = []
        total = []
        percent = []

        for session in sessions:
            session_numbers.append(session_number)
            session_number += 1

            date = session.created_date.strftime('%d-%b-%Y')[0: 11]
            session_date.append(date)

            results = Result.objects.get(session=session, skill=skill.skill)

            done.append(results.done)
            done_with_hint.append(results.done_with_hint)
            total.append(results.total)
            percent.append(results.percent)

        data = [session_date, session_numbers, done, done_with_hint, total, percent]

        worksheet.write_string('A' + str(position), skill.skill.name, bold)
        worksheet.write_column('A' + str(position + 1), headings, bold)

        for i in range(0, 6):
            worksheet.write_row('B' + str(position + i + 1), data[i])

        chart1 = workbook.add_chart({'type': 'line'})

        series_end_numb = len(data[1])

        chart1.add_series({
            'name': ['Sheet1', 2 + position, 0],
            'categories': ['Sheet1', 1 + position, 1, 1 + position, series_end_numb],
            'values': ['Sheet1', 2 + position, 1, 2 + position, series_end_numb],
        })

        chart1.add_series({
            'name': ['Sheet1', 3 + position, 0],
            'categories': ['Sheet1', 1 + position, 1, 1 + position, series_end_numb],
            'values': ['Sheet1', 3 + position, 1, 3 + position, series_end_numb],
        })

        chart1.set_title({'name': skill.skill.name})
        chart1.set_x_axis({'name': 'Сессии'})
        chart1.set_y_axis({'name': 'Кол-во выполнений'})

        chart1.set_style(2)

        worksheet.insert_chart('A' + str(position + 8), chart1, {'x_offset': 25, 'y_offset': 10})

        position += 26

    workbook.close()
