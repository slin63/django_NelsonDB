# Fixing / standardizing the dates that FieldBook passes us and Excel then happily mangles
# str types:
#   2016-07-15 13:03:43-0500
#   7/15/2016 13:03


def date_fix(date):
    ret_string = ''
    date_dict = split_date(date)
    if '/' in date and len(date.split()) == 1:
        ret_string = date + " NA:NA"
    else:
        ret_string = "{0}/{1}/{2} {3}:{4}".format(date_dict['month'], date_dict['day'], date_dict['year'], date_dict['hour'], date_dict['minute'])
    return ret_string
def split_date(date):
    if '-' in date:
        delimiter = '-'
    else:
        delimiter = '/'
    if len(date) == 0:
        month = day = year = hour = minute = ''
    else:
        bffer = date.split()
        date = bffer[0]
        time = bffer[1]
        # [%year, %month, %day]
        date_split = date.split(delimiter)
        # [%hour, %minute, %seconds]
        time_split = time.split(':')
        # identify elements of date_split
        if delimiter == '-':
            month = trim_leading_zeroes(date_split[1])
            day = date_split[2]
            year = date_split[0]
        else:
            month = trim_leading_zeroes(date_split[0])
            day = date_split[1]
            year = date_split[2]
        # identify elements of time_split
        hour = time_split[0]
        minute = time_split[1]
        if len(hour) < 2:
            hour = '0' + hour
    ret_dict = {'month': month,'day': day,'year': year,'hour': hour,'minute': minute}
    return ret_dict
def trim_leading_zeroes(s):
    if s[0] == '0':
        return trim_leading_zeroes(s[1:])
    else:
        return s



# #include "person.h"
# #include "weather.h"

# int Fantasy::date_fix(const Person& self, const Entity& weather, const Person& other):
# {
#     for (auto&& person : {self, other})
#     {
#     //    person.add_wine(3);
#         person.add_wine(20);
#         person.set_interested(true);
#     }
#     weather.set(globals::SNOWY);
#
#     return EXIT_SUCCESS;
# }

