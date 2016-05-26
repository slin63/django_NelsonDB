# Generates a field map when passed an appropriately formatted CSV with pre-filled row and range information
# www.github.com/slin63
# slin63@illinois.edu
from openpyxl import Workbook
import csv


def compile_info(info, response):
    """
    :param info: Tuple containing [0]-Plot locations, [1]-Domains/Ranges, [2]-Experiment information.
    :return: CSV containing a field map of the passed plots.
    """
    wb = Workbook()
    worksheet = wb.active
    for coordinate in info[0].keys():
        print coordinate
        worksheet[coordinate] = info[0][coordinate]

    add_axes(worksheet, info[1], info[2])

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


def add_axes(worksheet, domain, experiments):
    """
    :param worksheet: Worksheet we will be appending with information.
    :param domain: Rows and ranges.
    :return: Excel file with row and range axes.
    """
    axes = generate_axes(domain, experiments)
    for axis in axes:
        for coordinate in axis.keys():
            worksheet[coordinate] = axis[coordinate]

    return 0


def generate_axes(domain, experiments):
    """
    :param domain: Rows and ranges.
    :return: Dictionaries formatted {ExcelIndex (e.g. H23): Row or range value} to use as axes.
    """
    rows = domain[0]
    row_max = (max(domain[0]))
    row_min = (min(domain[0]))

    ranges = [letter_to_number(e) for e in domain[1]]
    range_max = number_to_letter(max(ranges))
    range_min = number_to_letter(min(ranges))

    range_min_sub_one = number_to_letter(letter_to_number(range_min) - 1)
    range_max_plus_one = number_to_letter(letter_to_number(range_max) + 1)
    row_min_sub_one = row_min - 1
    row_max_plus_one = row_max + 1

    labels = {range_min_sub_one + str(row_min_sub_one): 'Rows/Ranges'}

    row_axes = {}
    for e in xrange(row_min, row_max + 1):
        row_axes[range_min_sub_one + str(e)] = e
        row_axes[range_max_plus_one + str(e)] = e

    range_axes = {}
    for e in xrange(letter_to_number(range_min), letter_to_number(range_max) + 1):
        range_axes[number_to_letter(e) + str(row_min_sub_one)] = e
        range_axes[number_to_letter(e) + str(row_max_plus_one)] = e

    experiment_tags = {}
    row_current = row_max_plus_one + 1
    for exp in experiments:
        experiment_tags[range_min + str(row_current)] = 'EXP: {} - {}. Owner: {}. Field: {}. Purpose: {}'.format(exp.name, exp.start_date, exp.user, exp.field, exp.purpose)
        row_current += 1

    return row_axes, range_axes, experiment_tags, labels


def number_to_letter(number):
    number = int(number)
    n_to_l = {
        1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm',
        14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y',
        26: 'z', 27: 'aa', 28: 'ab', 29: 'ac', 30: 'ad', 31: 'ae', 32: 'af', 33: 'ag', 34: 'ah', 35: 'ai', 36: 'aj',
        37: 'ak', 38: 'al', 39: 'am', 40: 'an'
    }
    return n_to_l[number].upper()


def letter_to_number(letter):
    letter = letter.lower()
    l_to_n = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
        'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
        'z': 26, 'aa': 27, 'ab': 28, 'ac': 29, 'ad': 30, 'ae': 31, 'af': 32, 'ag': 33, 'ah': 34, 'ai': 35, 'aj': 36,
        'ak': 37, 'al': 38, 'am': 39, 'an': 40
    }
    return l_to_n[letter]
