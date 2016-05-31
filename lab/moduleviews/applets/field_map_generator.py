# Generates a field map when passed an appropriately formatted CSV with pre-filled row and range information
# www.github.com/slin63
# slin63@illinois.edu
from openpyxl import Workbook, PatternFill
from openpyxl.utils import _get_column_letter
from datetime import datetime
import csv


class PlotCell(object):
    def __init__(self, coordinate, experiment, plot_id, field):
        self.coordinate = coordinate
        self.experiment = experiment
        self.plot_id = plot_id

    def __repr__(self):
        return self.plot_id


def compile_info(info, response):
    """
    :param info: Tuple containing [0]-PlotCell Object, [1]-Domains/Ranges
    :return: CSV containing a field map of the passed plots.
    """
    wb = Workbook()
    worksheet = wb.active
    plot_objects = info[0]
    domain = info[1]
    experiment_current = plot_objects[0].experiment
    experiment_colors = iter(['00ccff', '00ffcc', 'ff6600'])

    for plot in plot_objects:
        if plot.experiment != experiment_current:
            experiment_current = plot.experiment
            # Cycles through three experiment colors so the spreadsheet doesn't look incredibly dull
            try:
                experiment_color = experiment_colors.next()
            except StopIteration:
                experiment_colors = iter(['00ccff', '00ffcc', 'ff6600'])
                experiment_color = experiment_colors.next()

        cell_fill = PatternFill(start_color=experiment_color,
                   end_color=experiment_color,
                   fill_type='solid')
        worksheet[plot.coordinate] = plot.plot_id
        worksheet[plot.coordinate].fill = cell_fill

    add_axes(worksheet, domain)

    return convert_to_csv(worksheet, response)


def convert_to_csv(worksheet, response):
    """
    :func: Opens an empty csvfile and copies over information from the Excel sheet into the new csvfile.
    :return: A csv identical to the earlier generated worksheet containing the fieldmaps.
    """
    writer = csv.writer(response)
    for row in worksheet.rows:
        writer.writerow([cell.value for cell in row])

    return response


def add_axes(worksheet, domain):
    """
    :param worksheet: Worksheet we will be appending with information.
    :param domain: Rows and ranges.
    :return: Excel file with row and range axes.
    """
    axes = generate_axes(domain)
    for axis in axes:
        for coordinate in axis.keys():
            worksheet[coordinate] = axis[coordinate]

    worksheet['A1'] = 'FieldMapper / slin63@illinois.edu / FCPathology / Rendered: {}'.format(datetime.now())

    return 0


def generate_axes(domain):
    """
    :param domain: Rows and ranges.
    :return: Dictionaries formatted {ExcelIndex (e.g. H23): Row or range value} to use as axes.
    """
    row_max = (max(domain[0]))
    row_min = (min(domain[0]))

    ranges = [letter_to_number(e) for e in domain[1]]
    range_max = _get_column_letter(max(ranges))
    range_min = _get_column_letter(min(ranges))

    range_min_sub_one = _get_column_letter(letter_to_number(range_min) - 1)
    range_max_plus_one = _get_column_letter(letter_to_number(range_max) + 1)
    row_min_sub_one = row_min - 1
    row_max_plus_one = row_max + 1

    labels = {range_min_sub_one + str(row_min_sub_one): 'Rows/Ranges'}

    row_axes = {}
    for e in xrange(row_min, row_max + 1):
        row_axes[range_min_sub_one + str(e)] = e
        row_axes[range_max_plus_one + str(e)] = e

    range_axes = {}
    for e in xrange(letter_to_number(range_min), letter_to_number(range_max) + 1):
        range_axes[_get_column_letter(e) + str(row_min_sub_one)] = e
        range_axes[_get_column_letter(e) + str(row_max_plus_one)] = e

    # experiment_tags = {}
    # row_current = row_max_plus_one + 1
    # for exp in experiments:
    #     experiment_tags[range_min + str(row_current)] = 'EXP: {} - {}. Owner: {}. Field: {}. Purpose: {}. Comments = {}'.format(exp.name, exp.start_date, exp.user, exp.field, exp.purpose, exp.comments)
    #     row_current += 1

    return row_axes, range_axes, labels


def letter_to_number(letter):
    letter = letter.lower()
    l_to_n = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
        'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
        'z': 26, 'aa': 27, 'ab': 28, 'ac': 29, 'ad': 30, 'ae': 31, 'af': 32, 'ag': 33, 'ah': 34, 'ai': 35, 'aj': 36,
        'ak': 37, 'al': 38, 'am': 39, 'an': 40
    }
    return l_to_n[letter]


def error_message(response):
    wb = Workbook()
    worksheet = wb.active
    worksheet['C3'] = 'Error: Mapper can only map one field at a time.'
    worksheet['C4'] = 'Reselect experiments and try again!'

    return convert_to_csv(worksheet, response)

