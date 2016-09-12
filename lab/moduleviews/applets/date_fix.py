# Fixing / standardizing the dates that FieldBook passes us and Excel then happily mangles
# str types:
#   2016-07-15 13:03:43-0500
#   7/15/2016 13:03


def date_fix(date):
    ret_string = ''

    if '-' in date:
        bffer = date.split()
        date = bffer[0]
        time = bffer[1]

        # [%year, %month, %day]
        date_split = date.split('-')
        # [%hour, %minute, %seconds]
        time_split = time.split(':')

        # identify elements of date_split
        month = trim_leading_zeroes(date_split[1])
        day = date_split[2]
        year = date_split[0]

        # identify elements of time_split
        hour = time_split[0]
        minute = time_split[1]
        ret_string = "{0}/{1}/{2} {3}:{4}".format(month, day, year, hour, minute)

    elif '/' in date and len(date.split()) == 1:
        ret_string = date + " NA:NA"

    else:
        ret_string = date

    return ret_string


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

