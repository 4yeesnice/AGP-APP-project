from fpdf import FPDF
from fpdf.enums import XPos, YPos
import datetime
from IPython.display import display, Latex
import pylab
from transliterate import translit, get_available_language_codes


def change_object_name(object):
    if len(object) == 5:
        return 'CCS' + object[3:]
    else:
        return 'CS' + object[2:]





def create_pdf(object, time, volume, pressure, temperature, z_factor, flow, name1, name2, name3):

    now = datetime.datetime.now()
    formula = r"$Q_{{гпа}}=283.8\cdot\frac{V_{{гпа}}}{T}\cdot(\frac{P}{z}-1)$ = " + flow + r" $м^3$"

    fig = pylab.figure()
    text = fig.text(0, 0, formula)

    # Saving the figure will render the text.
    dpi = 300
    fig.savefig('formula.png', dpi=dpi)

    # Now we can work with text's bounding box.
    bbox = text.get_window_extent()
    width, height = bbox.size / float(dpi) + 0.005
    # Adjust the figure size so it can hold the entire text.
    fig.set_size_inches((width, height))

    # Adjust text's vertical position.
    dy = (bbox.ymin / float(dpi)) / height
    text.set_position((0, -dy))

    # Save the adjusted text.
    fig.savefig('formula.png', dpi=dpi)

    pdf = FPDF('P', 'mm', 'letter')

    pdf.add_page()
    pdf.add_font('DejaVu', 'B', 'font/DejaVuSansCondensed-Bold.ttf')
    pdf.set_font('DejaVu', 'B', 12)

    pdf.set_text_color(0, 0, 0)

    pdf.cell(25, 10, f'{object}')
    pdf.cell(140, 10)

    pdf.cell(25, 10, f'{now.year}.{now.month}.{now.day} г.', align='C')

    pdf.ln(10)
    pdf.set_x(82.5)
    pdf.cell(25, 5, 'Акт №9', align='C',)

    pdf.ln(10)
    pdf.set_x(82.5)
    pdf.cell(25, 3, 'СТРАВЛИВАНИЯ ГАЗА С КОНТУРА ГПА №2', align='C')

    pdf.add_font('DejaVu', '', 'font/DejaVuSansCondensed.ttf')
    pdf.set_font('DejaVu', '', 12)

    pdf.ln(10)
    pdf.multi_cell(190, 6, f"Мы, нижеподписавшиеся, составили настоящий Акт о том, "
                           f"что ({now.day}.{now.month}.{now.year} года) в {time} "
                           f"нами был стравлен газ с контура ГПА №2")
    pdf.ln(1)
    pdf.multi_cell(190, 6, f"We, the undersigned, drew uр this Act stating that, "
                           f"({now.day}.{now.month}.{now.year}) at {time} "
                           f"we аге vent gas from the circuit from GCU №2")
    pdf.ln(10)
    pdf.set_x(15)
    pdf.cell(190, 6,
             'Объем стравливаемого газа составил:' +" "*58+ f'Q = {flow} тыс.м3')

    pdf.ln(10)
    pdf.set_x(15)
    pdf.cell(190, 6, f'Расчет расхода газа на стравливание выполнен согласно СТ 90625-1910-ТОО-21-001-2019')

    pdf.ln(10)
    pdf.set_x(15)
    pdf.cell(190, 6, f'P = {pressure} кг/см2')

    pdf.ln(6)
    pdf.set_x(15)
    pdf.cell(190, 6, f'T = {temperature} K')

    pdf.ln(6)
    pdf.set_x(15)
    pdf.cell(190, 6, f'Z = {z_factor}')

    pdf.ln(6)
    pdf.cell(190, 6, f'Геометрический объем контура ГПА и его обвязки равен:')

    pdf.ln(6)
    pdf.set_x(15)
    pdf.cell(190, 6, f'V = {volume} м3')

    pdf.ln(6)
    pdf.cell(190, 6, f'Объем стравливаемого газа')

    pdf.ln(15)
    pdf.set_x(55)
    pdf.image('formula.png', w=115, h=10, alt_text='123')

    pdf.ln(15)
    pdf.cell(20, 5, f'Начальник {object}',)
    pdf.cell(140, 5, '')
    pdf.cell(30, 5, f'{name1}',align='R')
    pdf.ln(5)
    pdf.cell(20, 5, f'Head of {change_object_name(object)}',)
    pdf.cell(140, 5, '')
    pdf.cell(30, 5, f'{translit(f"{name1}", 'ru', reversed=True)}', align='R')

    pdf.ln(15)
    pdf.cell(20, 5, f'Зам. начальник {object}')
    pdf.cell(140, 5, '')
    pdf.cell(30, 5, f'{name2}', align='R')
    pdf.ln(5)
    pdf.cell(20, 5, f'Deputy Head of {change_object_name(object)}')
    pdf.cell(140, 5, '')
    pdf.cell(30, 5, f'{translit(f"{name2}", 'ru', reversed=True)}', align='R')

    pdf.ln(15)
    pdf.cell(20, 5, f'Сменный инженер {object}')
    pdf.cell(140, 5, '')
    pdf.cell(30, 5, f'{name3}', align='R')
    pdf.ln(5)
    pdf.cell(20, 5, f'Shift engineer of {change_object_name(object)}')
    pdf.cell(140, 5, '')
    pdf.cell(30, 5, f'{translit(f"{name3}", 'ru', reversed=True)}', align='R')


    pdf.output('pdf_1.pdf')


create_pdf('СКС-5', '', 33, 33, 230, 0.8, '4524','Тань Сэньяо', 'Туктубаев А', 'Тулегенов Б')
